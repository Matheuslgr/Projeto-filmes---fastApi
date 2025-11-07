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


@app.delete("/filmes/{id_filme}")
def deletar_filme(id_filme: int):
    filmes = funcao.buscar_filme(id_filme)
    if filmes:
        funcao.remover_filme(id_filme)
        return {"200": "Filme excluido com sucesso!"}
    else:
        return {"erro": "Filme não encontrado"}


@app.put("/filmes/{id_filme}")
def atualizar_filmes(id_filme: int, nova_nota: float):
    filme =  funcao.buscar_filme(id_filme)
    if filme:
        funcao.atualizar_filme(id_filme, nova_nota)
        return{"200": "Filmes atualizado."}
    else:
        return{"Erro": "Filme não foi encontrado"}


