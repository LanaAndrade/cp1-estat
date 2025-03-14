import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Oooh+Baby&family=Pacifico&display=swap" rel="stylesheet">

    <style>
            
        .centered-columns {
            display: flex;
            justify-content: center;
            gap: 20px; /* Adds margin between the columns */
        }
        .stColumn {
            display: inline-block;
        }

        .custom-font {
            font-family: "Oooh Baby", cursive;
            font-size: 28px;
            color: #e0218a;
            text-align: center;
        }
            
        h1.custom-font {
            font-family: 'Pacifico', cursive;
            font-size: 36px;  /* Ajuste o tamanho conforme necessário */
            color: #e0218a;
            text-align: center;
        }

    </style>
""", unsafe_allow_html=True)


if "data" not in st.session_state:
    df = pd.read_csv("dataset.csv", index_col="track_id")
    df = df.sort_values(by="popularity", ascending=False)
    st.session_state["data"] = df

df = st.session_state["data"]

# Configuração da página
st.sidebar.markdown("Desenvolvido por Lana Andrade")

# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")

# Adicionando o logo
st.logo("logo.png")

# Adicionando o logo no body
st.image("logo.png", width=250)

st.markdown('<h1 class="custom-font">Lana Andrade - Quem sou eu?</h1>', unsafe_allow_html=True)


st.markdown('<p class="custom-font">Marcos importantes na minha vida.</p>', unsafe_allow_html=True)


# Create a container to center the columns
col1, col2, col3 = st.columns(3)

image_height = 500  # Adjust this value to suit your desired height

# Place images in the columns
with col1:
    st.image("minieu.jpeg", caption="Mini eu", use_container_width=True)

with col2:
    st.image("barbieeu.jpeg", caption="Live action da Barbie", use_container_width=True)

with col3:
    st.image("maceu.jpeg", caption="Eu no Mac", use_container_width=True)


st.markdown('<h1 class="custom-font">Apresentação</h1>', unsafe_allow_html=True)

st.markdown('<p class="custom-font" style="font-size: 16px; color: black;">Me chamo Lana, tenho 21 anos e sou uma Engenheira de Software em formação, pela FIAP. Atuo como estagiária na IBM, adquirindo conhecimento em Data & AI e DevOps para Z (Mainframe), no time de Expert Labs. Já trabalhei como estagiária de tecnologia na Hitachi, desenvolvendo sistemas em C# e VBA e na àrea de Customer Care, na empresa Johnson & Johnson. Técnica em Desenvolvimento de Sistemas, pela Etec Prof. Horácio Augusto da Silveira, na modalidade Ensino Técnico Integrado ao Médio. Formada em 2021, apresentando uma aplicação web destinada ao gerenciamento de projetos e amostras para pesquisadores da área de microbiologia como Trabalho de Conclusão de Curso. Sou uma pessoa proativa e adaptável.</p>', unsafe_allow_html=True)

st.markdown('<h1 class="custom-font">Fatos sobre mim</h1>', unsafe_allow_html=True)

# Criação de três colunas com fundo bonito
col1, col2, col3 = st.columns(3)

# Texto nas colunas com fundo e bordas arredondadas
with col1:
    st.markdown('''
    <div style="background: linear-gradient(135deg, #e021c1, #ff40a9); padding: 20px; border-radius: 10px;">
        <p class="custom-font" style="font-size: 16px; color: black;">Trabalho com mainfame (vintage).</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div style="background: linear-gradient(135deg, #e021c1, #ff40a9); padding: 20px; border-radius: 10px;">
        <p class="custom-font" style="font-size: 16px; color: black;">Amo rosa e Barbie (deu pra perceber?).</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div style="background: linear-gradient(135deg, #e021c1, #ff40a9); padding: 20px; border-radius: 10px;">
        <p class="custom-font" style="font-size: 16px; color: black;">VOU APRENDER A TOCAR BAIXO (esse ano)</p>
    </div>
    ''', unsafe_allow_html=True)


