import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Lana Andrade - Experiências e Escolaridade", layout="wide")

# Carregando o CSS personalizado
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Oooh+Baby&family=Pacifico&display=swap" rel="stylesheet">
    <style>
        .custom-font {
            font-family: "Pacifico", cursive;
            font-size: 28px;
            color: #e0218a;
            text-align: center;
        }
        h1.custom-font {
            font-family: 'Pacifico', cursive;
            font-size: 36px;
            color: #e0218a;
            text-align: center;
        }
        .section-box {
            background: linear-gradient(135deg, #f9f9f9, #ffffff);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .section-title {
            font-family: 'Pacifico', cursive;
            font-size: 24px;
            color: #e0218a;
            margin-bottom: 10px;
        }
        .section-content {
            font-family: "Pacifico", cursive;
            font-size: 16px;
            color: #333;
            text-align: justify;
        }
        .highlight {
            font-weight: bold;
            color: #e0218a;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="custom-font">Experiências e Escolaridade</h1>', unsafe_allow_html=True)

# Seção de Experiências Profissionais
st.markdown("""
    <div class="section-box">
        <div class="section-content">
            <p><span class="highlight">Estagiária em Data & AI/Devops pra Z</span> | IBM | MAI 2024 - Presente</p>
            <p>Desenvolvimento de modelos de machine learning, RPA, aprendizagem de Devops para Mainframe.</p>
            <p><span class="highlight">Estagiária em Desenvolvimento de Sofware</span> | Hitachi | Out 2023 - Mai 2024 </p>
            <p>Desenvolvimento de sistemas em C# e VBA.</p>
            <p><span class="highlight">Jovem Aprendiz em Customer Care</span> | Johnson & Johnson | Mar 2022 - Out 2023</p>
            <p>Atendimento ao cliente, gerenciamento de manutenções preventivas</p>
        </div>
    </div>
""", unsafe_allow_html=True)


# Seção de Escolaridade
st.markdown("""
    <div class="section-box">
        <div class="section-title">Escolaridade</div>
        <div class="section-content">
            <p><span class="highlight">Bacharelado em Engenharia de Software</span> | FIAP | 2023 - 2027</p>
            <p>Formação em Engenharia de Software com foco em desenvolvimento de sistemas e inteligência artificial.</p>
            <p><span class="highlight">Técnica em Desenvolvimento de Sistemas</span> | Etec Prof. Horácio Augusto da Silveira | 2019 - 2021</p>
            <p>Curso técnico integrado ao ensino médio, com foco em desenvolvimento de sistemas web e mobile.</p>
        </div>
    </div>
""", unsafe_allow_html=True)


# Seção de Escolaridade
st.markdown("""
    <div class="section-box">
        <div class="section-title">Certificados</div>
        <div class="section-content">
            <p><span class="highlight">Interskill - Mainframe Operator - CICS v5.6 Operations by IBM</p>
            <p>Deep Learning using TensorFlow by IBM</p>
            <p><span class="highlight">Introduction to responsible AI by Google</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Seção de Escolaridade
st.markdown("""
    <div class="section-box">
        <div class="section-title">Skills</div>
        <div class="section-content">
            <p><span class="highlight">Java - Javascript - Spring Boot - Python - C# - C++</p>
        </div>
    </div>
""", unsafe_allow_html=True)