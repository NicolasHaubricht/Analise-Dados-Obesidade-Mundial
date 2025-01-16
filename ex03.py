import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Acessar arquivo
df_obesity = pd.read_csv('obesity_data.csv')

# Tratar os dados
del df_obesity['Unnamed: 0']
df_obesity['Obesity'] = df_obesity['Obesity (%)'].apply(lambda x: x.split(' ')[0])
df_obesity.loc[df_obesity['Obesity'] == 'No', 'Obesity'] = np.nan
df_obesity.dropna(inplace=True)
df_obesity["Obesity"] = df_obesity["Obesity"].apply(lambda x: float(x))
df_obesity['Year'] = df_obesity['Year'].apply(lambda x: int(x))

# Criar DataFrame reduzido
df_obesity_dataframe = pd.DataFrame(df_obesity[['Obesity', 'Year', 'Country']])
df_obesity_dataframe = df_obesity_dataframe.set_index('Country')
df_paises = df_obesity_dataframe.groupby('Country')

# Armazenar variações
variacoes = {}

# Percorrer o DataFrame por países
for country, group in df_paises:
    group_sorted = group.sort_values('Year')
    obesidade_inicial = group_sorted['Obesity'].iloc[0]
    obesidade_final = group_sorted['Obesity'].iloc[-1]
    variacoes[country] = obesidade_final - obesidade_inicial

# Ordenar variações
maiores_aumentos = sorted(variacoes.items(), key=lambda x: x[1], reverse=True)[:5]
menores_aumentos = sorted(variacoes.items(), key=lambda x: x[1])[:5]

# Gráfico de barras para os maiores aumentos
countries_maiores = [item[0] for item in maiores_aumentos]
variacoes_maiores = [item[1] for item in maiores_aumentos]

plt.figure(figsize=(10, 5))
plt.bar(countries_maiores, variacoes_maiores, color='lightcoral')
plt.title('5 Países com Maiores Aumentos no Índice de Obesidade')
plt.xlabel('Países')
plt.ylabel('Variação no Índice de Obesidade (%)')
plt.show()

# Gráfico de barras para os menores aumentos
countries_menores = [item[0] for item in menores_aumentos]
variacoes_menores = [item[1] for item in menores_aumentos]

plt.figure(figsize=(10, 5))
plt.bar(countries_menores, variacoes_menores, color='skyblue')
plt.title('5 Países com Menores Aumentos no Índice de Obesidade')
plt.xlabel('Países')
plt.ylabel('Variação no Índice de Obesidade (%)')
plt.show()