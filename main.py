import streamlit as st
import gerador
import cifra_cesar

caixa_seletora = st.sidebar.selectbox("Quis projetos deseja navegar:",
                                      ("Home","Gerador de senha","Cifra Cesar"))

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
            senha = gerador.gerador_de_senha(slider, caracteres)
            st.write(f"A senha é:\n{senha}")
        except:
            st.write("Escolha uma opcao")

if caixa_seletora == "Cifra Cesar":
    st.title("Cifra de Cesar")
    with st.sidebar:
        texto = st.text_area("Digite o texto")
        chave = st.number_input("Digite a chave", 1, 26, 3)
        cifrar = st.button("Cifrar")
        decifrar = st.button("Decifrar")

    if cifrar:
        texto = str(texto)
        st.title("Mensagem cifrada")
        st.write(cifra_cesar.cesar(texto, chave, 1))
    if decifrar:
        texto = str(texto)
        st.title("Mensagem decifrada")
        st.write(cifra_cesar.cesar(texto, chave, -1))





