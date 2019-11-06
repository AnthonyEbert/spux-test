# # # # # # # # # # # # # # # # # # # # # # # # # #
# Hydrological linear bucket model
# Based on: Del Giudice, Albert, Rieckermann, Reichert.
# Water Resour. Res., 52, 3162–3186, doi:10.1002/2015WR017871.
#
# Jonas Sukys
# Eawag, Switzerland
# jonas.sukys@eawag.ch
# All rights reserved.
# # # # # # # # # # # # # # # # # # # # # # # # # #

import numba
import numpy

from spux.models.model import Model
from spux.utils.annotate import annotate

from spux.processes.ornsteinuhlenbeck import OrnsteinUhlenbeck, OrnsteinUhlenbeck_numba_spec
from spux.processes.precipitation import Precipitation, Precipitation_numba_spec
from spux.processes.wastewater import Wastewater, Wastewater_numba_spec

def dS (t, S, rng, A, h, xi, x_gw, K):

    x = h.evaluate (xi.evaluate (t, rng))
    y = S / K
    dS = A * x + x_gw - y
    return numpy.float64 (dS), numpy.float64 (x), numpy.float64 (y)

def integrate_FE (dS, t0, time, dt, S0, rng, A, h, xi, x_gw, K):

    t = t0
    S = S0
    cx = 0
    cy = 0
    while t < time:
        dt = min (dt, time - t)
        dSv, x, y = dS (t, S, rng, A, h, xi, x_gw, K)
        S += dt * dSv
        cx += dt * x
        cy += dt * y
        t += dt
    return numpy.float64 (S), numpy.float64 (cx), numpy.float64 (cy)

def integrate_RKSSP (dS, t0, time, dt, S0, rng, A, h, xi, x_gw, K):

    t = t0
    S = S0
    cx = 0
    cy = 0
    while t < time:
        dt = min (dt, time - t)
        dS1v, x1, y1 = dS (t, S, rng, A, h, xi, x_gw, K)
        S1 = S + dt * dS1v
        dS2v, x2, y2 = dS (t + dt, S1, rng, A, h, xi, x_gw, K)
        S2 = S1 + dt * dS2v
        cx += dt * 0.5 * (x1 + x2)
        cy += dt * 0.5 * (y1 + y2)
        S = 0.5 * (S + S2)
        t += dt
    return numpy.float64 (S), numpy.float64 (cx), numpy.float64 (cy)

class Hydro (Model):

    sandboxing = 0

    # construct model
    def __init__ (self, precipitation_coefficients, initial, dt, tau=None, integrator='FE', numbify=1):

        self.tau = numpy.float64 (tau) if tau is not None else None
        self.precipitation_coefficients = precipitation_coefficients
        self.initial = initial
        self.dt = numpy.float64 (dt)
        self.integrator = integrator
        self.numbify = numbify

    # initialize model using specified 'inputset' and 'parameters'
    def init (self, inputset, parameters):

        # base class 'init (...)' method
        Model.init (self, inputset, parameters)

        # get initial time and make sure it is a float
        self.t = numpy.float64 (inputset)

        # store inputset and parameters
        self.parameters = parameters

        # create a precipitation instance
        if self.numbify:
            self.h = numba.jitclass (Precipitation_numba_spec) (Precipitation) (*self.precipitation_coefficients)
        else:
            self.h = Precipitation (*self.precipitation_coefficients)

        # generate random initial values for \xi and y using the observed (uncertain) initial values and the associated error model
        initial = self.initial.draw (self.rng)
        if self.verbosity >= 2:
            print ('Drawing initial values:')
            print (initial)

        # generate a random initial value for \xi with observed value as the mean and parameter r'\sigma_\xi' as the spread
        xi0 = initial [r'$\xi$']

        # determine tau
        if self.tau is not None:
            tau = self.tau
        else:
            tau = numpy.float64 (self.parameters [r'$\tau$'])

        # create and initialize OU process
        if self.numbify:
            self.ou = numba.jitclass (OrnsteinUhlenbeck_numba_spec) (OrnsteinUhlenbeck) (tau)
        else:
            self.ou = OrnsteinUhlenbeck (tau)
        self.ou.init (self.t, numpy.float64 (xi0))

        # initialize wastewater process
        zeta = numpy.array ([ -self.parameters [r'$-\zeta_1$'], -self.parameters [r'$-\zeta_2$'] ], dtype=numpy.float64)
        chi = numpy.array ([ -self.parameters [r'$-\chi_1$'], self.parameters [r'$\chi_2$'] ], dtype=numpy.float64)
        if self.numbify:
            self.w = numba.jitclass (Wastewater_numba_spec) (Wastewater) (zeta, chi)
        else:
            self.w = Wastewater (zeta, chi)

        # generate a random initial value for y with observed value as the mean and parameter r'\sigma_y' as the spread
        y0 = initial ['y']
        if self.verbosity >= 2:
            print ('y0: ', y0)

        # compute initial S from initial discharge
        self.S = numpy.float64 (self.parameters ['K'] * (y0 - self.w.evaluate (self.t)))

        # initialize the the right hand side 'dS' of the ODE and its args
        if self.numbify:
            self.dS = numba.njit (dS)
        else:
            self.dS = dS
        self.dS_args = (self.parameters ['A'], self.h, self.ou, self.parameters [r'$x_{gw}$'], self.parameters ['K'])

        # set integrator
        integrate = None
        if self.integrator == 'FE':
            integrate = integrate_FE
        if self.integrator == 'RKSSP':
            integrate = integrate_RKSSP
        assert integrate, ' :: ERROR: The requested integrator is not implemented.'
        if self.numbify:
            self.integrate = numba.njit (integrate)
        else:
            self.integrate = integrate

    # run model up to specified 'time' and return the prediction
    def run (self, time):

        # base class 'run (...)' method
        Model.run (self, time)

        # make sure time is float
        time = numpy.float64 (time)

        # compute time window
        window = time - self.t

        # record current reservoir level
        S = self.S

        # check if temporal evolution of self.S is needed
        if time > self.t:

            # integrate S up to the specified 'time'
            self.S, cx, cy = self.integrate (self.dS, self.t, time, self.dt, self.S, self.rng, *self.dS_args)

            # update time and S
            self.t = time

        else:
            cx = 0
            cy = 0

        # make sure reservoir level is non-negative
        if self.S < 0:
            if self.verbosity:
                print (' :: WARNING: hydro model encountered negative reservoir level:', self.S)
                print ('  : -> setting to 0')
            self.S = numpy.float64 (0)

        # evaluate rainfall potential at time t
        xi = self.ou.evaluate (self.t, self.rng)

        # evaluate rainfall at time t
        x = self.h.evaluate (xi)

        # compute discharge at time t
        y = self.S / self.parameters ['K'] + self.w.evaluate (time)

        # make sure discharge is non-negative
        if y < 0:
            if self.verbosity:
                print (' :: WARNING: hydro model encountered negative discharge:', y)
                print ('  : -> setting to 0')
            y = numpy.float64 (0)

        # return results
        DeltaV = self.parameters ['A'] * cx + window * self.parameters [r'$x_{gw}$'] - cy - (self.S - S)
        return annotate ([x, y, xi, self.S, DeltaV], ['x', 'y', r'$\xi$', 'S', r'$\Delta V$'], time)
