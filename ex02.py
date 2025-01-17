import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 02 #

Qual o percentual médio de obesidade por sexo no mundo no ano de 2015?

'''

# Acessar arquivo
df_obesity = pd.read_csv('obesity_data.csv')

# Tratar os dados
del df_obesity['Unnamed: 0']
df_obesity['Obesity'] = df_obesity['Obesity (%)'].apply(lambda x: x.split(' ')[0])
df_obesity.loc[df_obesity['Obesity'] == 'No', 'Obesity'] = np.nan
df_obesity.dropna(inplace=True)
df_obesity['Obesity'] = df_obesity['Obesity'].apply(lambda x: float(x))
df_obesity['Year'] = df_obesity['Year'].apply(lambda x: int(x))

# Variáveis
medias_obesity = []
sexos_obesity = df_obesity['Sex'].unique()

# Dados do sexo masculino
df_obesity_male = df_obesity[(df_obesity['Sex'] == 'Male') & (df_obesity['Year'] == 2015)]
media_male_obesity = df_obesity_male['Obesity'].mean()
medias_obesity.append(media_male_obesity)

# Dados do sexo feminino
df_obesity_female = df_obesity[(df_obesity['Sex'] == 'Female') & (df_obesity['Year'] == 2015)]
media_female_obesity = df_obesity_female['Obesity'].mean()
medias_obesity.append(media_female_obesity)

# Dados de ambos os sexos
df_obesity_both = df_obesity[(df_obesity['Sex'] == 'Both sexes') & (df_obesity['Year'] == 2015)]
media_both_obesity = df_obesity_both['Obesity'].mean()
medias_obesity.append(media_both_obesity)

# Gerar Gráfico
plt.bar(sexos_obesity, medias_obesity, color='skyblue')
plt.title('Percentual Médio de Obesidade por Sexo no Mundo no Ano de 2015')
plt.xlabel('Sexo do Indivíduo')
plt.ylabel('Obesidade (%)')
plt.show()