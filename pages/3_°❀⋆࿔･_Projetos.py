import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *

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

st.markdown('<h1 class="custom-font">OceanBlue - GS2 - Edge Computing</h1>', unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=4Wb967PrX48")

st.markdown('<h1 class="custom-font">Arduíno - Challenge - Sprint 3</h1>', unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=dyoQjkK6Q2E")

st.markdown('<h1 class="custom-font">GS1 - Mobile Assist</h1>', unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=GrdHiHn2XyU")

st.markdown('<h1 class="custom-font">GS1 - Mobile Assist (Arduino)</h1>', unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=WCP_qn4kbSU")

st.markdown('<h1 class="custom-font">GS1 - Mobile Assist - Python</h1>', unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=BWvOTK_oH4Q&t=4s")
