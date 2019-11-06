
import numpy

g = numpy.array ([0, 1.561, 4.435], dtype=numpy.float64)
a = numpy.array ([0 / 60, 0.02 / 60, 0.001 / 60], dtype=numpy.float64) # converted to L/(s*m^2) from [0, 0.02, 0.001] in [mm/min]
b = numpy.array ([0, -1.736, -1.022], dtype=numpy.float64)
c = numpy.array ([0 / 60, 0 / 60, 0.074 / 60], dtype=numpy.float64) # converted to L/(s*m^2) from [0, 0, 0.074] in [mm/min]
xi_1 = numpy.float64 (-1.736)
xi_2 = numpy.float64 (1.079)

precipitation_coefficients = (g, a, b, c, xi_1, xi_2)
