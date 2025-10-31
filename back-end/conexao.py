import mysql.connector
from dotenv import load_dotenv
import os


#Cerregar .env
load_dotenv()

def conector():
    try:
        conexao = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexao {erro}")
        return None, None