import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.sidebar.title('MENU')
opc = st.sidebar.selectbox("SELECIONE A OPÇÃO",["Currículo","Objetivo", "Formação", "Experiências", "Habilidades","Contato","Portifólio"])

if opc =="Currículo":
    st.markdown("<h1 style='text-align: center;'>Curriculo</h1>",unsafe_allow_html=True)
    st.markdown('''<h5 style='text-align: center;'> Matheus Heinrich </h1>''',unsafe_allow_html=True)

    image = Image.open('perfil.png')
    col1, col2, col3 = st.columns([0.2, 4, 0.2])
    col2.image(image,use_column_width=True)

    st.markdown('## Objetivo')

    st.markdown('''
    - A procura de preencher a vaga visando crescer profissionalmente.
    - Trabalhar de maneira produtiva,contribuindo com o desenvolvimento pessoal e da instituição que me emprega.
    - Auxiliando de múltiplas formas em todas as áreas necessárias da empresa.
    ''')

    st.markdown('''
    ## Formação
    ''')

    st.markdown('''
    - **Ensino Médio**, *CEM 03*.   *2019-2021*
    - **Ensino Fundamental**, *CEF 07*.   (*2015-2018*)
    ''')

    st.markdown('''
    ## Experiências
    ''')

    st.markdown('''
    - **Tribunal de Justiça do DF - TJDFT:**
    *Estágiario Administrativo*.
    *03/03/2020 - 19/12/2021*
    - **Defensoria Pública do DF - DPDF:**
    *Estágiario Administrativo*.
    *17/12/2019 - 13/03/2020*
    - **Original Dogguis|Delícias da Praça|Padaria Julipan:**
    *Auxiliar Geral - Freelancer*.
    *4 Meses*
    ''')

    st.markdown('''
    ## Habilidades
    ''')

    st.markdown('''
    - **Inglês Intermediário**
    - **Informática Intermediária**
    - **Sistema Operacional - Windows e Linux**
    - **Aplicativos LibreOffice e Microsoft Office**
    - **Crianção e Edição de Imagens e Vídeos**
    - **Logística Almoxarifado**
    ''')

    st.markdown('''
    ## Contato
    ''')

    st.markdown('''
    - **Email** : *matheusheinrichcontato@gmail.com*
    - **Telefone** : *+55 61 99456-0592*
    - **Instagram** : *www.instagram.com/offheinrich/*
    - **Linkedin** : *www.linkedin.com/in/matheus-heinrich-888b62228/*
    ''')

if opc =="Objetivo":
    st.markdown("<h1 style='text-align: center;'>Objetivo</h1>",unsafe_allow_html=True)
    st.markdown('''
    - A procura de preencher a vaga visando crescer profissionalmente.
    - Trabalhar de maneira produtiva,contribuindo com o desenvolvimento pessoal e da instituição que me emprega.
    - Auxiliando de múltiplas formas em todas as áreas necessárias da empresa.
    ''') 
    
    objetivo = Image.open('objetivo.png')
    col1, col2, col3 = st.columns([0.2, 4, 0.2])
    col2.image(objetivo,use_column_width=True)

if opc =="Formação":
    st.markdown("<h1 style='text-align: center;'>Formação</h1>",unsafe_allow_html=True)
    st.markdown('''
    - **Ensino Médio**, *CEM 03*.   *2019-2021*
    - **Ensino Fundamental**, *CEF 07*.   (*2015-2018*)
    ''')

    formacao = Image.open('formação.png')
    col1, col2, col3 = st.columns([0.2, 4, 0.2])
    col2.image(formacao,use_column_width=True)

if opc =="Experiências":
    st.markdown("<h1 style='text-align: center;'>Experiências</h1>",unsafe_allow_html=True)
    st.markdown('''
    - **Tribunal de Justiça do DF - TJDFT:**
    *Estágiario Administrativo*.
    *03/03/2020 - 19/12/2021*
    - **Defensoria Pública do DF - DPDF:**
    *Estágiario Administrativo*.
    *17/12/2019 - 13/03/2020*
    - **Original Dogguis|Delícias da Praça|Padaria Julipan:**
    *Auxiliar Geral - Freelancer*.
    *4 Meses*
    ''')

    experiencias = Image.open('experiências.png')
    col1, col2, col3 = st.columns([0.2, 4, 0.2])
    col2.image(experiencias,use_column_width=True)

if opc =="Habilidades":
    st.markdown("<h1 style='text-align: center;'>Habilidades</h1>",unsafe_allow_html=True)
    st.markdown('''
    - **Inglês Intermediário**
    - **Informática Intermediária**
    - **Sistema Operacional - Windows e Linux**
    - **Aplicativos LibreOffice e Microsoft Office**
    - **Crianção e Edição de Imagens e Vídeos**
    - **Logística Almoxarifado**
    ''')

    habilidades = Image.open('habilidades.png')
    col1, col2, col3 = st.columns([0.2, 4, 0.2])
    col2.image(habilidades,use_column_width=True)

if opc=="Contato":
    st.markdown("<h1 style='text-align: center;'>Contato</h1>",unsafe_allow_html=True)
    st.markdown('''
    - **Email** : *matheusheinrichcontato@gmail.com*
    - **Telefone** : *+55 61 99456-0592*
    - **Instagram** : *www.instagram.com/offheinrich/*
    - **Linkedin** : *www.linkedin.com/in/matheus-heinrich-888b62228/*
    ''')

    contato = Image.open('contato.png')
    col1, col2, col3 = st.columns([0.2, 4, 0.2])
    col2.image(contato,use_column_width=True)

if opc=="Portifólio":
    st.markdown("<h1 style='text-align: center;'>Portifólio</h1>",unsafe_allow_html=True)

    img1 = Image.open('1.png')
    img2 = Image.open('2.png')
    img3 = Image.open('3.png')
    col1, col2, col3 = st.columns([4, 4, 4])
    col1.image(img1,use_column_width=True)
    col2.image(img2,use_column_width=True)
    col3.image(img3,use_column_width=True)