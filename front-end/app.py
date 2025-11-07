#pip install streamlit requests
import streamlit as st
import requests

#URL DA API Fastapi
API_URL = "http://127.0.0.1:8000"


st.set_page_config(page_title="Filmes", layout="wide")
st.title("Gerenciador de Filmes")

menu = st.sidebar.radio("Menu",
    ["Catálogo", "Cadastar Filmes", "Deletar Filmes", "Atualizar filmes"]
    )
if menu == "Catálogo":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            st.dataframe(filmes)
        else:
            st.info("Nenhum filmes cadastrado ainda ")

    else:
        st.error("Deu erro ao conectar com a API.")

elif menu == "Cadastar Filmes":
    st.subheader("➕ Adicionar filmes ")
    titulo = st.text_input("Titulo do Filme")
    genero = st.text_input("Gênero do Filme")
    ano = st.number_input("Ano de Lançamento", min_value=1900, max_value=2100, step=1)
    nota = st.number_input("Avaliação do Filme (0 a 10)", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Salvar filme"):
        dados = {"titulo": titulo, "genero": genero, "ano": ano, "nota": nota}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar filme.")

elif menu == "Deletar Filmes":
    st.subheader(" 🗑 Deletar filmes")
    id_filme = st.number_input("Id do filme a excluir", min_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/filmes/{id_filme}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Filme excluido  com sucesso!")
            else:
                st.error("Erro ao tentar excluir filme.")
        else:
            st.error("Erro ao excluir o filme")

elif menu == "Atualizar filmes":
    st.subheader(" Atualizar filmes")
    id_filme = st.number_input("Id do filme que deseja atualizar", min_value=1, step=1)
    nova_nota = st.number_input("Digite a nova nota do Filme", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Atualizar"):
        dados = {
            "id_filme": id_filme,
            "nova_nota": nova_nota
        }
        response = requests.put(f"{API_URL}/filmes/{id_filme}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Filme atualizado com sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error("Erro ao atulizar o filme.")
        