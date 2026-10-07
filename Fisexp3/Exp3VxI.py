import matplotlib.pyplot as plt
import scipy.optimize as sp
import numpy as np

Tensão = [1.235,1.228,1.221,1.216,1.21,1.204,1.199,1.192,1.185,1.18]
Corrente = [12,22.1,31.6,41,50.6,60.7,70.3,80.8,91.6,101.1]
ErroT = [0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006]
ErroC = [0.1,0.2,0.3,0.3,0.4,0.5,0.6,0.6,0.7,0.8]

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
plt.title('Tensão (V) x Corrente (mA)', fontsize = 20)
plt.xlabel('Corrente (mA)', fontsize = 15)
plt.ylabel('Tensão (V)', fontsize= 15)
plt.plot(Cdata, Tfit, 'ro-', label ='Curva de ajuste linear, a =-6.11 +/- 0.57, b = 1.241 +/- 0.004, R^2 = 0,998973403760973', markersize = '2' )
plt.legend(fontsize='8')
plt.grid(True)
plt.show()


