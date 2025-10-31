#pip install streamlit requests
import streamlit as st
import requests

#URL DA API Fastapi
API_URL = "http://127.0.0.1:8000"

st.title("Gerenciador de Filmes")

menu = st.sidebar.radio("Menu",
    ["Catálogo", "Cadastar Filmes"]
    )
if menu == "Catálogo":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])

    else:
        st.error("Deu erro ao conectar com a API.")