import matplotlib.pyplot as plt                                                 
import sympy

limxtoinf = sympy.Symbol('\lim_{x\\to\infty}')

# THE LATEX EXPRESSION TO BE PRINTED
expr = sympy.latex(limxtoinf)
# OR
#expr = '\lim_{x\\to\infty}'

#add text
plt.text(0.2, 0.7, r"$%s$" % expr, fontsize = 50)                            

#hide axes                                                           
fig = plt.gca()                                  
fig.axes.get_xaxis().set_visible(False)                                         
fig.axes.get_yaxis().set_visible(False)

plt.draw() #or savefig                                                          
plt.show()