import matplotlib.pyplot as plt
import sympy

#limxtoinf = sympy.Symbol('y = -x^2+1\n \\frac{dy}{dx} = -2x')

# THE LATEX EXPRESSION TO BE PRINTED
#expr = sympy.latex(limxtoinf)
# OR
y = r'y = x^3-3x^2 + 2x'
dy = r'\frac{dy}{dx} = 3x^2 - 6x + 2'


#add text
plt.text(0.1, 0.6, r"$%s$" % y, fontsize = 50)
plt.text(0.1, 0.3, r"$%s$" % dy, fontsize = 50)

#hide axes
fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.draw() #or savefig
plt.show()
