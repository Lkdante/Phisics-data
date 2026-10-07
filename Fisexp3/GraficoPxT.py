from math import sqrt
import numpy as np
import scipy.optimize as sp
import matplotlib.pyplot as mp

Pressão= [-649,-639,-628,-604,-576,-537,-498,-426,-392,-289]
Temperatura= [10.5 , 20.5,29,39.5,46.5,53,59,66,68,75.5]
ErroT=[x/(2*x) for x in range(1,11)]
ErroP=[x/x for x in range(1,11)]
#Essa porra associa cada elemento da pressão, com um elemento da temperatura

print("Dados que relacionam Pressão com sua respectiva Temperatura:")
for i in range(len(Pressão)):
    print("Pressão: " + str(Pressão[i]) + " -+ " + str(ErroP[i]) + "mmhg à "+ str(Temperatura[i]) + " -+ " + str(ErroT[i])+" °C")

#Usar biblioteca numpy para escrever os dados brutos como uma matrix n dimensional

Pdata= np.array(Pressão)
Tdata= np.array(Temperatura)
Perro= np.array(ErroP)
Terro= np.array(ErroT)
#Hora de definir a função linear para um ajuste

def f(x,a,b):
    return a*x +b

#w contem informação para a inclinação do eixo e a interceptação de b
# Quem caralhos é o u?????
w,u = sp.curve_fit(f, Tdata, Pdata)

#Vamos usar nossa função para ter o fit da pressão (eixo y)
Pfit = f(Tdata,*w)

#hora de criar a linha do nosso melhor ajuste de função
mp.errorbar(Tdata,Pdata, xerr=Terro, yerr=Perro, fmt='o', ms=3)
mp.plot(Tdata,Pdata,'o-',label="ajuste linear, a= 5.1499005, b= -764.55784847", linewidth=1.5, linestyle='dashed',)

#Adcionar o titulo do grafico, e suas etiquetas dos eixos
mp.title('Pressão X Temperatura')
mp.xlabel('temperatura(°C)')
mp.ylabel('pressão(mmHg)')
mp.legend()
mp.grid(True)

#Mostrar nosso 'a' e nosso 'b'
print("valor de 'a' e 'b':" + str(w))

#para salvar o grafico
mp.savefig('PxT.jpg')

#para mostrarz
mp.show()
           



 
    

