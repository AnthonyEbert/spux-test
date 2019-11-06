
import sympy

xi = sympy.Symbol ('xi')
xi0 = sympy.Symbol ('xi0')
s = sympy.Symbol ('s')
xi_1 = sympy.Symbol ('xi_1')

f = sympy.exp (- (xi - xi0) ** 2 / (2 * s ** 2) )

integral = sympy.integrate (f, (xi, -sympy.oo, xi_1))

print (integral)