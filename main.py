import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard de Bestsellers", layout="wide")

@st.cache_data
def carregar_dados():
    data = pd.read_csv('bestsellers.csv')
    return data

data = carregar_dados()

#inicio tratamento de dados -----------------------------------------

# 1 distribuição por genero %
distribuicao = (data['Genre'].value_counts(normalize=True) * 100).round(0).reset_index()
distribuicao.columns = ['Gênero', 'Porcentagem']


# 2 faixas de preço
#estudar mais para deixar mais legivel
data['Faixa_Preco'] = pd.cut(data['Price'], bins=5)
faixa = data['Faixa_Preco'].value_counts().sort_index().reset_index()

#3 preco medio
preco_medio = data['Price'].mean()

#4 autores com mais aparições
top_authors = data['Author'].value_counts().head(10)
top_authors.columns = ['Autor', 'Contagem']


#5 contagem de autores mais bem avaliados
contagem = data['Author'].value_counts()

# Filtra autores com mais de 5 aparições
autores_frequentes = contagem[contagem > 5].index

# Faz a média apenas para esses autores
ranking_elite = data[data['Author'].isin(autores_frequentes)].groupby('Author')['User Rating'].mean().sort_values(ascending=False)

autor_avaliacao = ranking_elite.round(2).reset_index()
autor_avaliacao.columns = ['Autor', 'Nota_Média']

#6 total entradas e livros unicos
total_livros_unicos = data['Name'].nunique() 
total_entradas = len(data)

#7 nota media
nota_media = data['User Rating'].mean().round(2)

#8total de reviews
total_reviews = data['Reviews'].sum()

#Inicio st ---------------------------------------

st.title("📚 Análise de Livros Bestsellers (Amazon)")
st.markdown("Este dashboard apresenta uma análise visual dos dados tratados via Pandas.")