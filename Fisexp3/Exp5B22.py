import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df4= pd.read_csv("ParteFudida.CSV", sep=';', decimal=',')
df4.columns= df4.columns.str.strip()
lista=[]
for coluna in df4.columns:
    lista.append(pd.to_numeric(df4[coluna], errors='coerce'))

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
        

#fazer os fits
ab1 , r1 = fitasso(lista[0],lista[1])
a1, b1 = ab1
fit1= f(lista[0], ab1)
print(a1, b1, r1)


#montando esse grafico nessa pora

plt.plot(lista[0], fit1, label= 'Ib = 4 A , a = -0.0056, r² = 0.0.970754')
plt.scatter(lista[0],lista[1])


#trocar cor da errobar, tamanho dos plots, e adcionar informações dos plots
#em suma terminado

plt.title("Deflexão X Tensão do acelerador ")
plt.xlabel("Tensão do acelerador (V)")
plt.ylabel("Deflexão(cm)")
plt.legend()
plt.grid(False)
plt.show()
plt.savefig(0)