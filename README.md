# Projeto Integrador: Análise de Tendências dos Bestsellers Amazon (2009-2019)

## 1. Tema do Projeto
Análise descritiva, identificação de tendências de mercado e desenvolvimento de painel gerencial a partir do dataset de livros mais vendidos da Amazon (Top 50 anuais) no período de 2009 a 2019.

## 2. Integrantes (Grupo 53)
* MICHAEL DE SOUZA TEIXEIRA
* KAUAN RIBEIRO TERUEL
* FILIPE PINHEIRO
* GIUSLENE GONCALVES DA SILVA
* MAR DO NASCIMENTO MORAES
* VITOR HENRIQUE RIBAS
* ISAQUE ROCHA VENANCIO
* JOAO PEDRO DE ALMEIDA ABREU

## 3. Objetivo da Análise
O objetivo central deste projeto é realizar uma **análise descritiva** para compreender como o comportamento de consumo literário na Amazon evoluiu ao longo de uma década. Através da aplicação de ciência de dados, respondemos a dobras estratégicas do mercado:

* **Preferência de Gênero:** Proporção e dominância entre Ficção e Não-Ficção ao longo dos anos.
* **Comportamento de Preços:** Variação e evolução dos preços médios praticados pelos bestsellers.
* **Engajamento do Público:** Volume acumulado de avaliações (*Reviews*) recebidas pelos títulos.
* **Fidelidade e Popularidade:** Identificação dos autores recorrentes e livros de maior destaque.

---

## 4. Arquitetura do Dashboard e Funcionalidades
Com a conclusão da Etapa 2, o projeto transformou os dados brutos em uma aplicação analítica utilizando **Streamlit**:


### 📊 Painel Principal de Insights
1. **Cards de Métricas Gerais:** Exibição responsiva do total de registros, soma de reviews formatada, nota média global e preço médio do período filtrado.
2. **Visão de Mercado (Gêneros):** Gráfico de pizza (*Pie Chart*) do Plotly mapeando a distribuição percentual das categorias.
3. **Visão de Influência (Autores):** Gráfico de barras exibindo os 10 autores com maior recorrência no ranking.
4. **Tendências Temporais:** Gráfico de linha nativo demonstrando a flutuação histórica de preços e gráfico de barras customizado com o *Top 10* livros mais bem avaliados e caros da plataforma.

---

## 5. Metodologia e Ferramentas
* **Figma:** Concepção do Mockup e UI/UX design das telas para guiar o desenvolvimento visual.
* **Python & Pandas:** Limpeza, transformação, tratamento de dados e otimização de performance com cache de dados (`@st.cache_data`).
* **Plotly Express:** Construção de gráficos dinâmicos, responsivos e dotados de *tooltips* informativas.
* **Streamlit & Streamlit Cloud:** Framework para a interface web corporativa e infraestrutura para hospedagem pública do app.

---

## 6. Estrutura do Dataset Local
O arquivo `bestsellers.csv` consumido pela aplicação contém:
* `Name`: Título do livro.
* `Author`: Autor da obra.
* `User Rating`: Avaliação média dos usuários (0 a 5).
* `Reviews`: Número de avaliações recebidas.
* `Price`: Preço de venda na plataforma (U$).
* `Year`: Ano em que o livro figurou no ranking.
* `Genre`: Categoria original (*Fiction* / *Non Fiction*).

---

## 7. Status do Cronograma
* **Etapa 1 (Concluído):** Planejamento, design de telas no Figma e estruturação inicial do repositório.
* **Etapa 2 (Concluído):** Desenvolvimento do pipeline em Pandas, Design e estilo com Streamlit, HTML/CSS renderização dos gráficos do Plotly e publicação (*deploy*) no Streamlit Community Cloud.

---

## 8. Como Executar o Projeto

**1. Acesso online na Streamlit Cloud:**

https://top-amazon-books.streamlit.app/

Ou, se quiser rodar o dashboard na sua máquina, siga os passos abaixo:

 **2. Clone o repositório:**
   ```bash
   git clone https://github.com/Grupo53-Senac/PI_Grupo_53_DataScience_Senac
   cd seu-repositorio
   pip install -r requirements.txt
   streamlit run main.py
