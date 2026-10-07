import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


df2 = pd.read_csv("Parte(A.2)exp5.CSV", sep=';', decimal=',')
df2.columns = df2.columns.str.strip()
lista=[]
for coluna in df2.columns:
    lista.append(pd.to_numeric(df2[coluna], errors = 'coerce'))


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

#fazer os fits
ab1 , r1 = fitasso(lista[0],lista[1])
a1, b1 = ab1
fit1= f(lista[0], ab1)
print(a1, b1, r1)



#Montanddo o grafico
plt.plot(lista[0],fit1, label='A = 0.006; R² = 0.96215')

plt.scatter(lista[0],lista[1])
plt.title("Deflexão X Tensão de aceleração do eletron (Va) ")
plt.xlabel("tensão de aceleração do eletron (V)")
plt.ylabel("Deflexão(cm)")
plt.legend()
plt.grid(False)
plt.show()
