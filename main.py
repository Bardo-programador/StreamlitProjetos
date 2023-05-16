import streamlit as st
import gerador

caixa_seletora = st.sidebar.selectbox("Quis projetos deseja navegar:",
                                      ("Home","Gerador de senha",))

if caixa_seletora == "Home":
    st.title("Página inicial")

if caixa_seletora == "Gerador de senha":
    caracteres = ""
    st.title("Geradora de senhas")
    with st.sidebar:
        maiusculos = st.checkbox("Letras maiusculas")
        minusculos = st.checkbox("Letras minusculas")
        numeros = st.checkbox("Números")
        especiais = st.checkbox("Especias")
        opcoes = [maiusculos, minusculos, numeros, especiais]
        slider = st.slider("Quantos números", 1, 128, 8)
        botao = st.button('Gerar Senha')

    if botao:
        try:
            for opcao, escolha in zip(gerador.opcoes, opcoes):
                if escolha:
                    caracteres += opcao
            senha = gerador.gerador_de_senha(slider, caracteres).encode('utf-8').decode('utf-8')
            caracteres = ""
            st.write(f"A senha é:\n{senha}")
        except:
            st.write("Escolha uma opcao")







