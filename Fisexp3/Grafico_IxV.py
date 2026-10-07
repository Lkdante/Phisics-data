import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp 

Voltagem = [1.5,3.01,4.51,6.01,7.53,9.03,10.52,12.01,13.5,14.98,-1.5,-3.1,-4.51,-6.2,-7.53,-9.03,-10.53,-12.02,-13.51,-14.97]
Corrente = [1.51 , 3.04 , 4.55 , 6.08,  7.62 , 9.16 , 10.69 , 12.23 , 13.76 , 15.3 , -1.52 , -3.04 , -4.56,  -6.09 , -7.63 , -9.16 , -10.7 , -12.24,  -13.77 , -15.32]

Vdata =np.array(Voltagem)
Cdata= np.array(Corrente)
y1= np.sin(Vdata)

def f(x,a,b):
    return x*a + b

w,u = sp.curve_fit(f, Voltagem, Corrente )

Cfit = f(Cdata,*w)

#linha simples de plot (configurações da saída)
plt.figure(figsize= (8,10)) #tamanho de largura e altura de uma figura
plt.title('Corrente X Tensão', fontsize = 25)
plt.xlabel('Tensão (V)', fontsize= 10)
plt.ylabel('Corrente (mA)', fontsize = 10)

#plots essenciais que vão estar no grafico (saída)
plt.plot(Cdata, y1,'co-' , label='seno da corrente')
# valor x, valor y, cor/formato/linhas, legenda, tamanho do formato olhar dicionario dps
plt.plot(Vdata, Cfit,'ro-', label= 'linear fit de resistencia', markersize = 5)

#legendas habilitadas, grids, mostra (configurações de saiída)
plt.legend(fontsize = 8) #Aumenta as legendas colocadas no plot :D
plt.grid(True)
plt.show()



