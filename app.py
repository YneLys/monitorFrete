import streamlit as st
from scraper import calcular_frete_jadlog

st.set_page_config(page_title="Freight Monitor", layout="centered")
st.title("Freight Monitor - Jadlog")

with st.form("formulario_frete"):
    origem = st.text_input("CEP de Origem", placeholder="Ex: 01001-000")
    destino = st.text_input("CEP de Destino", placeholder="Ex: 20040-000")
    peso = st.number_input("Peso (kg)", min_value=0.1, step=0.1)
    enviar = st.form_submit_button("Calcular Frete")

if enviar:
    if not origem or not destino:
        st.warning("Por favor, preencha todos os campos.")
    else:
        resultado = calcular_frete_jadlog(origem, destino, peso)
        if "erro" in resultado:
            st.error(resultado['erro'])
        else:
            st.success("Frete encontrado com sucesso!")
            st.write(f"**Transportadora:** {resultado['transportadora']}")
            st.write(f"**Valor estimado:** {resultado['valor_frete']}")
            st.write(f"**Prazo estimado:** {resultado['prazo_estimado']}")