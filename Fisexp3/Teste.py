import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# 1. Leitura dos dados
df3 = pd.read_csv("Parte(B)exp5.CSV", sep=';', decimal=',')
df3.columns = df3.columns.str.strip()

lista = []
for coluna in df3.columns:
    lista.append(pd.to_numeric(df3[coluna], errors='coerce').dropna().values)

# ==============================================================================
# 2. DEFINE A FUNÇÃO MATEMÁTICA DESEJADA
# ==============================================================================
# Exemplo 1: Modelo Inversamente Proporcional (D = A/I + B)
def modelo_inverso(I, A, B):
    return (A / I) + B

# Exemplo 2: Modelo Geométrico de Arco Circular (D = R - sqrt(R^2 - L^2))
def modelo_arco(I, K, L):
    R = K / I
    return R - np.sqrt(np.maximum(0, R**2 - L**2))

# *** Escolha qual função usar aqui ***
f_fit = modelo_inverso  

# ==============================================================================
# 3. FUNÇÃO DE AJUSTE NÃO-LINEAR
# ==============================================================================
def fit_nao_linear(x, y, funcao):
    # popt contém os parâmetros otimizados (A, B, etc.)
    popt, _ = curve_fit(funcao, x, y, p0=[1.0, 0.0])
    
    # Cálculo do R² para o fit não-linear
    residuos = y - funcao(x, *popt)
    ss_res = np.sum(residuos**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_quadrado = 1 - (ss_res / ss_tot)
    
    return popt, r_quadrado

# ==============================================================================
# 4. EXECUTAR OS FITS E PLOTAR
# ==============================================================================
tensoes = ['300V', '400V', '500V', '600V']
indices_x = [0, 4, 8, 12]
indices_y = [1, 5, 9, 13]

plt.figure(figsize=(10, 6))

for i in range(4):
    x = lista[indices_x[i]]
    y = lista[indices_y[i]]
    
    # Ajuste não-linear
    params, r2 = fit_nao_linear(x, y, f_fit)
    
    # Gera pontos suaves para desenhar a curva contínua
    x_curva = np.linspace(min(x), max(x), 100)
    y_curva = f_fit(x_curva, *params)
    
    # Plot dos dados e da curva
    plt.scatter(x, y, label=f'Dados {tensoes[i]}')
    plt.plot(x_curva, y_curva, label=f'Fit {tensoes[i]} (r² = {r2:.4f})')

plt.title("Deflexão X Corrente nas Bobinas (Ib)")
plt.xlabel("Corrente nas bobinas (A)")
plt.ylabel("Deflexão (cm)")
plt.legend()
plt.grid(True)
plt.show()