import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df1 = pd.read_csv("Força_magnetica - Página1 (1).csv", decimal=',')
df2 = pd.read_csv("GpC25.csv", decimal=',')

# 2. Limpar espaços antes e depois dos nomes das colunas
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# 3. Converter as colunas para numérico (forçando números válidos)
XBp = pd.to_numeric(df1['IL p(A)'], errors='coerce')
YBp = pd.to_numeric(df1['Fm1'], errors='coerce')
XBG = pd.to_numeric(df2['IL G(A)'], errors='coerce')
YBG = pd.to_numeric(df2['Fm3'])
XBm = pd.to_numeric(df1['IL m(A)'], errors='coerce')
YBm = pd.to_numeric(df1['Fm2'], errors='coerce')
XBP = pd.to_numeric(df2['IL P(A)'])
YBP = pd.to_numeric(df2['Fm4'])


# 4. Juntar e remover linhas com valores nulos/mismatches
dados1 = pd.concat([XBp, YBp], axis=1).dropna()
xb1_clean = dados1['IL p(A)']
yb1_clean = dados1['Fm1']
dados2 = pd.concat([XBm, YBm], axis=1).dropna()
xbm_limpo = dados2['IL m(A)']
ybm_limpo= dados2['Fm2']

# 5. Executar a regressão linear
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

#concatenar os dados
ab1 , r1= fitasso(xb1_clean,yb1_clean)
a1 , b1 = ab1
fit1 = f(xb1_clean, ab1)

ab2, r2 = fitasso(XBG, YBG)
a2, b2 = ab2
fit2= f(XBG,ab2)

ab3, r3 = fitasso(xbm_limpo,ybm_limpo)
a3, b3 =ab3
fit3= f(xbm_limpo,ab3)

ab4, r4 = fitasso(XBP, YBP)
a4, b4 = ab4
fit4 =  f(XBP, ab4)


plt.plot(XBP, fit4, label = f"25mm a={a4:.3f}, b={b4:.3f}")
plt.plot(xbm_limpo,fit3, label= f"50mm a={a3:.3f}, b={b3:.3f}")
plt.plot(XBG,fit2, label= f"100mm a={a2:.3f}, b={b2:.3f}")
plt.plot(xb1_clean, fit1, label= f"12,5mm a={a1:3f}  b={b1:3f}")
plt.title("Força Magnetica X corrente do filamento")
plt.xlabel("Corrente IL (A)")
plt.ylabel("Força magnética (mT)")
plt.legend()
plt.grid()
plt.show()

print(r1, r2)



