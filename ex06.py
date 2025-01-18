import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 06 #

Você conseguiria plotar um gráfico mostrando a evolução da obesidade para ambos sexos no mundo?

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

# Definir SetIndex como Year e Filtrar por ambos os sexos
df_obesity_mundial = pd.DataFrame(df_obesity[df_obesity['Sex'] == 'Both sexes'].set_index('Year'))

# Somar os dados por ano
new_df_obesity_mundial = pd.DataFrame(df_obesity_mundial.groupby('Year').sum())

# Organizar dados para o gráfico de barras
years = new_df_obesity_mundial.index
obesity_data = new_df_obesity_mundial['Obesity']

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.plot(years, obesity_data, marker='o', color='blue', label='Obesidade (%)')

# Criar as barras
plt.xlabel('Ano')
plt.ylabel('Obesidade (%)')
plt.title('Evolução da Obesidade Mundial (Ambos os Sexos)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years, rotation=45)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()