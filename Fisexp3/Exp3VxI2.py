import matplotlib.pyplot as plt
import scipy.optimize as sp
import numpy as np

Tensão = [9.16,9.13,9.11,9.08,9.06,9.04,9.01,8.98,8.96,8.92]
Corrente = [0.1,0.2,0.3,0.4,0.51,0.6,0.7,0.83,0.9,1.06]
ErroT = [0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07]
ErroC = [0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.01,0.01]

Tdata = np.array(Tensão)
Cdata = np.array(Corrente)
ETdata = np.array(ErroT)
ECdata = np.array(ErroC)

def linear(x,a,b):
    return x*a +b

w, u = sp.curve_fit(linear,Corrente, Tensão )
Tfit = linear(Cdata, *w)
print('o valor de a e b é: ' + str(w))

plt.figure( figsize = (8,12))
plt.errorbar(Cdata, Tdata,xerr=ECdata, yerr=ETdata, fmt= 'none') 
plt.title('Tensão (V) x Corrente (A)', fontsize = 20)
plt.xlabel('Corrente (A)', fontsize = 15)
plt.ylabel('Tensão (V)', fontsize= 15)
plt.plot(Cdata, Tfit, 'ro-', label ='Curva de ajuste linear, ', markersize = '2' )
plt.legend(fontsize='8')
plt.grid(True)
plt.show()