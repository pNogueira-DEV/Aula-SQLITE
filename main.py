#Criar um banco de dados com SQLTITE# e uma tabela
import sqlite3

# criar um banco de dados  chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#criar o objeto chamado de "cursor" que sera usado para executar os comandos SQL
cursor = conexao.cursor()



#criar uma tabela mo banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
    )
""")
