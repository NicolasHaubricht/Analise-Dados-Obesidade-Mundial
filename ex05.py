import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 05 #

Qual a diferença média percentual de obesidade entre sexos ao longo dos anos para o Brasil?

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
df_obesity_brazil = pd.DataFrame(df_obesity[df_obesity['Country'] == 'Brazil'].set_index('Year'))

# Criar DataFrames para cada sexo
df_obesity_brazil_male = pd.DataFrame(df_obesity_brazil[df_obesity_brazil['Sex'] == 'Male']['Obesity'])
df_obesity_brazil_female = pd.DataFrame(df_obesity_brazil[df_obesity_brazil['Sex'] == 'Female']['Obesity'])
df_obesity_brazil_both = pd.DataFrame(df_obesity_brazil[df_obesity_brazil['Sex'] == 'Both sexes']['Obesity'])

# Organizar dados para o gráfico de barras
years = df_obesity_brazil_male.index
male_data = df_obesity_brazil_male.values.flatten()
female_data = df_obesity_brazil_female.values.flatten()
both_data = df_obesity_brazil_both.values.flatten()

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
bar_width = 0.2
index = np.arange(len(years))

# Criar as barras
plt.bar(index - bar_width, male_data, bar_width, label='Masculino', color='blue')
plt.bar(index, female_data, bar_width, label='Feminino', color='purple')
plt.bar(index + bar_width, both_data, bar_width, label='Ambos', color='gray')

# Personalizar o gráfico
plt.xlabel('Ano')
plt.ylabel('Obesidade (%)')
plt.title('Obesidade ao Longo dos Anos - Brasil (Masculino, Feminino, Ambos)')
plt.xticks(index, years, rotation=45)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()