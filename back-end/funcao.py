from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE  TABLE IF NOT EXISTS filmes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INT NOT NULL,
                nota FLOAT  
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()

def cadastrar_filme(titulo, genero, ano, nota):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, nota) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, nota)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastar o filme {erro}")
        finally:
            cursor.close()
            conexao.commit()

def listar_filmes():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao cadastrar o filme {erro}")
            return []
        finally:
            cursor.close()
            conexao.commit()

def atualizar_filme(id_filme, nota):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET nota = %s WHERE id = %s",
                (nota, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar a nota do filme {erro}")
        finally:
            cursor.close()
            conexao.commit()



