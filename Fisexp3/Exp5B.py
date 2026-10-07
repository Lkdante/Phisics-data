import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df3= pd.read_csv("Parte(B)exp5.CSV", sep=';', decimal=',')
df3.columns= df3.columns.str.strip()
lista=[]
for coluna in df3.columns:
    lista.append(pd.to_numeric(df3[coluna], errors='coerce'))

def fitasso(x,y):
    resultado = linregress(x, y)
    a = resultado.slope
    b = resultado.intercept
    r = resultado.rvalue**2
    return (a,b),r 
def f(x,ab):
    a =ab[0]
    b =ab[1]
    return x*a +b

#corrigir a coleta mal feita de dados feitas por mim
indices_x=[0,4,8,12]
indices_y=[1,5,9,13]
y_certo=[]

for i in range(4):
    x = lista[indices_x[i]]
    y = lista[indices_y[i]]
    y_corrigido = y*np.sign(x)
    y_certo.append(y_corrigido)
    
    

#fazer os fits
ab1 , r1 = fitasso(lista[0],y_certo[0])
a1, b1 = ab1
fit1= f(lista[0], ab1)
print(a1, b1, r1)

ab2, r2 = fitasso(lista[4],y_certo[1])
a2, b2 =ab2
fit2 = f(lista[4], ab2)
print(a2, b2, r2)

ab3, r3 = fitasso(lista[8],y_certo[2])
a3, b3 = ab3
fit3= f(lista[8], ab3)
print(a3, b3, r3)

ab4, r4 = fitasso(lista[12],y_certo[3])
a4, b4 = ab4
fit4 = f(lista[12], ab4)
print( a4, b4, r4)

#montando esse grafico nessa pora

plt.plot(lista[0], fit1, label= '300 V, a = 0.70, r² = 0.99935')

plt.scatter(lista[0],y_certo[0])
plt.plot(lista[4], fit2, label='400V, a = 0.83, r² = 0.99882')

plt.scatter(lista[4], y_certo[1])
plt.plot(lista[8],fit3, label='500V, a = 0.92 , r² = 0.9999')

plt.scatter(lista[8], y_certo[2])
plt.plot(lista[12], fit4, label='600V, a = 1.01, r² =0.99953')

plt.scatter(lista[12],y_certo[3])

#trocar cor da errobar, tamanho dos plots, e adcionar informações dos plots
#em suma terminado

plt.title("Deflexão X Corrente nas bobinas(Ib) ")
plt.xlabel("Corrente nas bobinas(A)")
plt.ylabel("Deflexão(cm)")
plt.legend()
plt.grid(False)
plt.show()
