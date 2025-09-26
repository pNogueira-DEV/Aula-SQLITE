#Criar um banco de dados com SQLTITE# e uma tabela
import sqlite3

# criar um banco de dados  chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#criar o objeto chamado de "cursor" que sera usado para executar os comandos SQL
cursor = conexao.cursor()



# #criar uma tabela mo banco de dados
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT
#     )
# """)
# nome = input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno:").lower()

# #Inserir um dado na tabela
# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """,
# (nome, idade, curso)
# )


# #confirmar as alterações no banco
# conexao.commit()


#Inserir varios alunos uma vez só
alunos =[
    ("Yago", 28, "Direito"),
    ("Jessica", 24, "computação"),
    ("Breno", 22, "Computação")
]
#executemany pemite inserir multiplas linhas de uma vez só
cursor.executemany("""
INSERT INTO alunos(nome, idade, curso)
VALUES(?, ?, ?)
""",
(alunos)
)
conexao.commit()