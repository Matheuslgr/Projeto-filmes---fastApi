from fastapi import FastAPI
import funcao

#Como exeutar o fastapi
# python -m uvicorn main:app --reload
app = FastAPI(title="Gerenciador de filmes")

#Criando uma rota
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filme(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return {"200": "Filme cadastrado com sucessso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filmes()
    lista = []
    for linha in filmes:
        lista.append(
            {
                "id": linha[0],
                "titulo": linha[1],
                "genero": linha[2],
                "ano": linha[3],
                "nota": linha[4]
            }
        )
    return {"filmes": lista}


