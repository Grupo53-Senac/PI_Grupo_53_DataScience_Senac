import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de Bestsellers", layout="wide")

@st.cache_data
def carregar_dados():
    data = pd.read_csv('data/bestsellers.csv')
    return data

data = carregar_dados()

#inicio tratamento de dados -----------------------------------------

# 1 distribuição por genero %
distribuicao = (data['Genre'].value_counts(normalize=True) * 100).round(0).reset_index()
distribuicao.columns = ['Gênero', 'Porcentagem']

distribuicao_fim = distribuicao.replace({
    'Fiction': 'Ficção',
    'Non Fiction': 'Não Ficção'
})
# 2 faixas de preço
#estudar mais para deixar mais legivel
data['Faixa_Preco'] = pd.cut(
    data['Price'],
    bins=[0, 10, 20, 30, 40, 50],
    labels=['0-10', '10-20', '20-30', '30-40', '40-50']
)

#3 preco medio
preco_medio = data['Price'].mean()

#4 autores com mais aparições
top_authors = (
    data['Author']
    .value_counts()
    .head(10)
    .reset_index()
)
top_authors.columns = ['Autor', 'Contagem']
top_authors = top_authors.sort_values(by='Contagem')

#5 contagem de autores mais bem avaliados
contagem_autores = data['Author'].value_counts()

# Filtra autores com mais de 5 aparições
autores_frequentes = contagem_autores[contagem_autores > 5].index

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

#9 evolução temporal
evolucao = data.groupby('Year')['Price'].mean()

#10 top_books
top_books = data.sort_values(by=['User Rating', 'Price'], ascending=False).head(10)
#Inicio st ---------------------------------------

st.title("📚 Análise de Livros Bestsellers da Amazon (2009 - 2019)")
st.markdown("Este dashboard apresenta uma análise visual em Streamlit dos dados tratados via Pandas.")
#metricas gerais
def metric_card(label, value, color= "#FFFFFF"):
    st.markdown(
        f"""
        <div style="
            background-color: #FF8C00; 
            padding: 20px;
            margin-top: 5px; 
            border-radius: 10px; 
            border-left: 5px solid {color};
            text-align: center;
        ">
            <p style="color: #FFFFFF; font-size: 14px; margin-bottom: 5px;">{label}</p>
            <h2 style="color: {color}; margin: 0;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
  metric_card('Total de livros', total_entradas)
with col2:
  metric_card('reviews totais', total_reviews)
  
with col3:
  metric_card("nota média", nota_media)
 
with col4: 
  metric_card('preço médio', f'U$ {preco_medio}')

st.divider()

#Dashboard
tela1, tela2 = st.columns(2, border=True)
with tela1:
  st.subheader('Distribuição por gênero: Ficção vs Não ficção') 
  fig_pie = px.pie(
    distribuicao_fim,
    names='Gênero',
    values='Porcentagem',
    hole=0.5,
)
  st.plotly_chart(fig_pie)

with tela2:
  st.subheader("Autores com Mais Aparições")
  fig_bar = px.bar(
    top_authors, 
    x='Autor', 
    y='Contagem',
    text='Contagem', # Adiciona o número em cima da barra
    color='Contagem', # Muda a cor baseado no valor (opcional)
    color_continuous_scale='Blues')

  st.plotly_chart(fig_bar)

st.divider()
st.title('tendencias temporais')
tela3, tela4 = st.columns([0.4, 0.6], border=True)

with tela3:
   st.subheader('Evolução temporal do preço (U$)')
   st.line_chart(evolucao)

with tela4:
   
  fig_livros = px.bar(
    top_books,
    x='Price',
    y='Name',
    orientation='h', 
    color='User Rating',
    title='Livros mais caros e bem avaliados',
    color_continuous_scale='Blues',
    labels={'Price': 'Preço (U$)', 'Name': 'Título do Livro', 'User Rating': 'Nota'}
)
  fig_livros.update_layout(yaxis={'categoryorder':'total ascending'})

  st.plotly_chart(fig_livros)