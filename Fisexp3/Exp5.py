import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


df1 = pd.read_csv("Parte(A)exp5.CSV", sep=';', decimal=',')
df2 = pd.read_csv("Parte(A.2)exp5.CSV", sep=';', decimal=',')
df3= pd.read_csv("Parte(B)exp5.CSV", sep=';', decimal=',')

# 2. Limpar espaços antes e depois dos nomes das colunas
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()
df3.columns= df3.columns.str.strip()

#botar todos os dados da lista em numericos nessa porra
lista=[]
for coluna in df1.columns:
    lista.append(pd.to_numeric(df1[coluna], errors='coerce'))
lista1=[]
for coluna in df2.columns:
    lista1.append(pd.to_numeric(df2[coluna], errors = 'coerce'))
lista2=[]
for coluna in df3.columns:
    lista2.append(pd.to_numeric(df3[coluna], errors='coerce'))
Inverso = lista[2]*-1



# 5. Executar a regressão linear
#OBS: ISSO TEM COMO SER IMPORTADO DA OUTRA FUNÇÃO, MAS TO COM PREGUIÇA :p
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

#Dale nos fits
ab1, r1 = fitasso(lista[1],Inverso)
a1, b1 = ab1
fit1 = f(lista[1],ab1)
print(a1, b1, r1)

ab2, r2 = fitasso(lista[5],lista[6])
a2, b2 =ab2
fit2 = f(lista[5], ab2)
print(a2, b2, r2)

ab3, r3 = fitasso(lista[9],lista[10])
a3, b3 = ab3
fit3= f(lista[9], ab3)
print(a3, b3, r3)

ab4, r4 = fitasso(lista[13],lista[14])
a4, b4 = ab4
fit4 = f(lista[13], ab4)
print( a4, b4, r4)

# Hora de agrupar esses dados
plt.plot(lista[1], fit1, label= '300 V, a = 0.058, r² = 0.9985')

plt.scatter(lista[1],Inverso)
plt.plot(lista[5], fit2, label='400V, a = 0.044, r² = 0.9989')

plt.scatter(lista[5], lista[6])
plt.plot(lista[9],fit3, label='500V, a = 0.037, r² = 0.9987')

plt.scatter(lista[9], lista[10])
plt.plot(lista[13], fit4, label='600V, a = 0.031, r² =0.9991')

plt.scatter(lista[13],lista[14])

#trocar cor da errobar, tamanho dos plots, e adcionar informações dos plots
#em suma terminado

plt.title("Deflexão X Tensão do Campo elétrico ")
plt.xlabel("tensão nas placas (V)")
plt.ylabel("Deflexão(cm)")
plt.legend()
plt.grid(False)
plt.show()
