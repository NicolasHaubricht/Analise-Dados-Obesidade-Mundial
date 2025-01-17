import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 03 #

Quais são os 5 países com a maior e a menor taxa de aumento nos índices de obesidade no período observado?

'''

# Acessar arquivo
df_obesity = pd.read_csv('obesity_data.csv')

# Tratar os dados
del df_obesity['Unnamed: 0']
df_obesity['Obesity'] = df_obesity['Obesity (%)'].apply(lambda x: x.split(' ')[0])
df_obesity.loc[df_obesity['Obesity'] == 'No', 'Obesity'] = np.nan
df_obesity.dropna(inplace=True)
df_obesity["Obesity"] = df_obesity["Obesity"].apply(float)
df_obesity['Year'] = df_obesity['Year'].apply(int)

# Criar DataFrame reduzido
df_obesity_dataframe = df_obesity[['Obesity', 'Year', 'Country']].set_index('Country')

# Obter países únicos
unique_countries = df_obesity_dataframe.index.unique()

# Calcular a variação de obesidade para cada país
variacoes = {}

for country in unique_countries:
    country_data = df_obesity_dataframe.loc[country]
    country_data_sorted = country_data.sort_values('Year')  # Ordenar por ano
    obesidade_inicial = country_data_sorted['Obesity'].iloc[0]
    obesidade_final = country_data_sorted['Obesity'].iloc[-1]
    variacoes[country] = obesidade_final - obesidade_inicial

# Ordenar os países por variação de obesidade
sorted_variacoes = dict(sorted(variacoes.items(), key=lambda x: x[1]))

# 5 países com os menores aumentos
menores_aumentos = dict(list(sorted_variacoes.items())[:5])

# 5 países com os maiores aumentos
maiores_aumentos = dict(list(sorted_variacoes.items())[-5:])


# Gráfico de barras para os maiores aumentos
plt.figure(figsize=(10, 5))
plt.bar(maiores_aumentos.keys(), maiores_aumentos.values(), color='lightcoral')
plt.title('5 Países com Maiores Aumentos no Índice de Obesidade')
plt.xlabel('Países')
plt.ylabel('Variação no Índice de Obesidade (%)')
plt.show()

# Gráfico de barras para os menores aumentos
plt.figure(figsize=(10, 5))
plt.bar(menores_aumentos.keys(), menores_aumentos.values(), color='skyblue')
plt.title('5 Países com Menores Aumentos no Índice de Obesidade')
plt.xlabel('Países')
plt.ylabel('Variação no Índice de Obesidade (%)')
plt.show()