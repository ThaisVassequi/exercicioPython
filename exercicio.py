import os
import psycopg2
from psycopg2 import OperationalError


# Recuperar variáveis de ambiente
host = os.getenv("HOST_NAME")
port = os.getenv("PORT")
database = os.getenv("DATABASE_DB")
user = os.getenv("USER_DB")
password = os.getenv("PASSWORD_DB")

# Imprimir os valores das variáveis de ambiente para depuração (exceto a senha por segurança)
print(f"Conectando ao banco de dados com os seguintes detalhes:")
print(f"Host: {host}")
print(f"Port: {port}")
print(f"Database: {database}")
print(f"User: {user}")

try:
    # Conecta ao banco de dados
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    print("Conexão estabelecida com sucesso!")
    
    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Define a consulta SQL
    query = "SELECT * FROM minha_tabela"

    # Executa a consulta
    cursor.execute(query)

    # Recupera todos os resultados da consulta
    results = cursor.fetchall()

    # Itera sobre os resultados e imprime cada linha
    for row in results:
        print(row)

    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()

except OperationalError as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
