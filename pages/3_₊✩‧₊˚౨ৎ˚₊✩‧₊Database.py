import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dados",
    page_icon="🏃🏼",
    layout="wide"
)

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# Título
st.title("Análise de Lucratividade de Músicas no Spotify")

# Introdução
st.markdown("""
Disclaimer: 
        A análise dos dados foi feita totalmente no Colab, sendo a versão completa e mais confiável neste link:
            https://colab.research.google.com/drive/1UDratcANHBPvHB9sfhSPBISDfPq9CUaU?usp=sharing            

Este projeto tem como objetivo analisar as características das músicas mais lucrativas do Spotify, como dançabilidade, duração e positividade, para identificar padrões que levam ao sucesso financeiro.
""")

# Carregamento dos dados
dados = pd.read_csv("dataset.csv", sep=",")

# Exibição dos dados
st.subheader("Dados")
st.dataframe(dados.head())

# Análise de Dançabilidade
st.subheader("Análise de Dançabilidade")
st.markdown("""
A dançabilidade é uma métrica que varia de 0 a 1, indicando o quão adequada uma música é para dançar. Vamos analisar como a dançabilidade influencia a lucratividade das músicas.
""")

# Média de dançabilidade
n_danceability_mean = dados['danceability'].mean()
st.write(f"Média de dançabilidade: {n_danceability_mean:.2f}")

# Gráfico de distribuição de dançabilidade
st.markdown("### Distribuição de Dançabilidade")
fig, ax = plt.subplots()
sns.boxplot(y=dados['danceability'], ax=ax)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Título
st.title("Análise de Lucratividade por Faixa de Dançabilidade")

# Carregar os dados (substitua pelo seu DataFrame)
dados = pd.read_csv("dataset.csv", sep=",")

# Explicação em Markdown
st.markdown("""
### Análise de Dançabilidade vs Lucratividade
Abaixo está o gráfico que mostra a lucratividade média por faixa de dançabilidade.
""")

# Criar as faixas de dançabilidade
bins = np.arange(0, 1.1, 0.1)  # 0.0 to 1.0 em passos de 0.1
labels = [f"{round(bins[i], 1)}-{round(bins[i+1], 1)}" for i in range(len(bins)-1)]

# Atribuir cada música a uma faixa de dançabilidade
dados['danceability_range'] = pd.cut(dados['danceability'], bins=bins, labels=labels, include_lowest=True)

# Agrupar por faixa de dançabilidade e calcular a lucratividade média
danceability_profit = dados.groupby('danceability_range')['profit'].mean().reset_index()

# Criar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=danceability_profit, x='danceability_range', y='profit', marker='o', color='b', ax=ax)

# Configurações do gráfico
ax.set_xlabel('Faixa de Dançabilidade')
ax.set_ylabel('Lucratividade Média')
ax.set_title('Lucratividade Média por Faixa de Dançabilidade')
plt.xticks(rotation=45)
ax.grid(True)

# Exibir o gráfico no Streamlit
st.pyplot(fig)

st.markdown("""
### Conclusão sobre Dançabilidade e Lucratividade

Bom, podemos ver que o **range de 0.5-0.6 de dançabilidade** é o melhor para obtermos lucro, chegando a uma média de **1300**.

Podemos também ver que é uma **distribuição assimétrica** com **concentração à direita** e **calda à esquerda**.
""")

# Análise de Duração
st.subheader("Análise de Duração")
st.markdown("""
A duração das músicas é medida em milissegundos. Vamos analisar como a duração influencia a lucratividade.
""")

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Título
st.title("Gráfico de Dispersão: Duração vs Lucratividade")

# Carregar os dados (substitua pelo seu DataFrame)
dados = pd.read_csv("dataset.csv", sep=",")

# Explicação em Markdown
st.markdown("""
### Análise de Duração vs Lucratividade
Abaixo está o gráfico de dispersão que mostra a relação entre a duração das músicas (em minutos) e a lucratividade.
""")

# Criar o gráfico
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(y=dados['profit'], x=dados['duration_ms'], color='blue', alpha=0.7, ax=ax)

# Função para formatar os valores em minutos
def minutos(x, pos):
    return f'{x/60000:.1f}'  # Converter para minutos e exibir com 1 casa decimal

# Aplicar a formatação ao eixo x
formatter = FuncFormatter(minutos)
ax.xaxis.set_major_formatter(formatter)  # Formatar eixo x

# Ajustar o intervalo do eixo X entre 0 e 7 minutos (0 a 420.000 ms)
ax.set_xlim(0, 420000)  # Limite entre 0 e 420.000 milissegundos (7 minutos)

# Configurações do gráfico
ax.set_xlabel("Duração da Música (minutos)")
ax.set_ylabel("Lucratividade (em milhares)")
ax.set_title("Relação entre Duração da Música e Lucratividade")
ax.grid(True)

# Exibir o gráfico no Streamlit
st.pyplot(fig)

st.markdown("""
### Análise de Duração vs Lucratividade

Como podemos ver, as durações com maior lucratividade estão entre **2.5 e 4.2 minutos**. Os dados estão distribuídos de forma homogênea, com uma **calda à esquerda** devido à exclusão dos dados com duração igual a 0.
""")

# Análise de Positividade (Valence)
st.subheader("Análise de Positividade (Valence)")
st.markdown("""
A positividade (valence) é uma métrica que varia de 0 a 1, indicando o quão positiva é uma música. Vamos analisar como a positividade influencia a lucratividade.
Há uma distribuição assimétrica com concentração à esquerda e cauda a direita.
            """)

# Gráfico de linha: Positividade vs Lucratividade
st.markdown("### Positividade vs Lucratividade")
bins = np.arange(0, 1.1, 0.1)
labels = [f"{round(bins[i], 1)}-{round(bins[i+1], 1)}" for i in range(len(bins)-1)]
dados['valence_range'] = pd.cut(dados['valence'], bins=bins, labels=labels, include_lowest=True)
valence_profit = dados.groupby('valence_range')['profit'].mean().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=valence_profit, x='valence_range', y='profit', marker='o', color='b', ax=ax)
ax.set_xlabel("Faixa de Positividade")
ax.set_ylabel("Lucratividade Média")
ax.set_title("Lucratividade Média por Faixa de Positividade")
plt.xticks(rotation=45)
st.pyplot(fig)

# Distribuição Normal e Binomial
st.subheader("Distribuição Normal e Binomial")
st.markdown("""
A probabilidade de o lucro ser acima de 3000 é muito baixa, e abaixo de 0 também. Já de cerca de 1000 à 1800 é bem alta, sendo o seu pico.
""")

# Distribuição Normal
st.markdown("### Distribuição Normal")
mu = dados['profit'].mean()
sigma = dados['profit'].std()
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
pdf = norm.pdf(x, mu, sigma)
cdf = norm.cdf(x, mu, sigma)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
sns.lineplot(x=x, y=pdf, color='blue', ax=ax1)
ax1.set_title("PDF (Função de Densidade de Probabilidade)")
ax1.set_xlabel("Lucro")
ax1.set_ylabel("Densidade")

sns.lineplot(x=x, y=cdf, color='red', ax=ax2)
ax2.set_title("CDF (Função de Distribuição Acumulada)")
ax2.set_xlabel("Lucro")
ax2.set_ylabel("Probabilidade Acumulada")

st.pyplot(fig)

# Distribuição Binomial
st.markdown("### Distribuição Binomial")
n = 10  # Número de tentativas
k = 5   # Número de sucessos
p = 0.41  # Probabilidade de sucesso

x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)
df_binomial = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y)}).set_index("X")

st.write("Tabela de Probabilidades:")
st.dataframe(df_binomial)

fig, ax = plt.subplots()
sns.barplot(x=x, y=y, color='blue', alpha=0.7, ax=ax)
ax.set_title("Distribuição Binomial")
ax.set_xlabel("Número de Sucessos")
ax.set_ylabel("Probabilidade")
st.pyplot(fig)

st.markdown("""
Utilizei a distribuição binomial para descobrir as chances das canções terem sucesso financeiro ou não as vezes que consegui os resultados que eu quero é 46674 e as tentativas totais foram 114000, então a probabilidade é 40,94%, e o numero de sucesso é acima de 1552.26. - a distribuição binomial calcula essa probabilidade de conseguir com x tentativas, os numeros foram substituidos por seus equivalentes.

n_max = 50 - A quantidade de tentativas máxima é 50

n = 10 - o número de tentativas setado é 10

k = 1552.26 é o valor definido como sucesso, sendo cerca de 50% do valor total, portanto, o valor desse parâmetro é 5.

p = 0.41 pois a probabilidade de atingir lucro é de 41%

Portanto com 10 tentativas, a probabilidade de atingir 2 com sucesso é de 0.10 e de atingir 4 com sucesso é a maior, 0,25%.

""")


# Conclusão
st.subheader("Conclusão")
st.markdown("""
Com base na análise, podemos concluir que:
- Músicas com dançabilidade entre 0.5 e 0.6 tendem a ser mais lucrativas.
- Durações entre 2.5 e 4.2 minutos são as mais lucrativas.
- A positividade (valence) tem um impacto moderado na lucratividade, com valores médios sendo mais eficazes.
""")