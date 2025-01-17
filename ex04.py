import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 04 #

Quais os países com maiores e menores níveis percetuais de obesidade em 2015?

'''

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
df_obesity_2015 = pd.DataFrame(df_obesity[df_obesity['Year'] == 2015])
df_obesity_2015 = df_obesity_2015.set_index('Country')

# Obter os países únicos
unique_country = df_obesity_2015.index.unique()

# Armazenar Series com dados por país
series_unique_country = {}

# Percorrer o DataFrame por países
for country in unique_country:
    filtered_df = df_obesity_2015.loc[country]
    total_obesity = filtered_df['Obesity'].sum()
    series_unique_country[country] = pd.Series({'sum': total_obesity})

# Ordenar Series
sorted_series = dict(sorted(series_unique_country.items(), key=lambda x: x[1].loc['sum'], reverse=False))

# Encontrar os países com maior obesidade
maiores_indices = dict(list(sorted_series.items())[-5:])

# Encontrar os países com menor obesidade
menores_indices = dict(list(sorted_series.items())[:5])

# Armazenar os resultados em DataFrames
df_maiores = pd.DataFrame.from_dict(maiores_indices, orient='index')
df_menores = pd.DataFrame.from_dict(menores_indices, orient='index')

# Gráfico de barras para os países com maiores níveis percentuais de obesidade em 2015
plt.figure(figsize=(10, 5))
plt.bar(df_maiores.index, df_maiores['sum'], color='lightcoral')
plt.title('5 Países com Maiores Índices de Obesidade')
plt.xlabel('Países')
plt.ylabel('Obesidade (%)')
plt.show()

# Gráfico de barras para os países com menores níveis percentuais de obesidade em 2015
plt.figure(figsize=(10, 5))
plt.bar(df_menores.index, df_menores['sum'], color='skyblue')
plt.title('5 Países com Menores Índices de Obesidade')
plt.xlabel('Países')
plt.ylabel('Obesidade (%)')
plt.show()