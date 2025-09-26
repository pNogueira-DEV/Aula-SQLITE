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
# alunos =[
#     ("Yago", 28, "Direito"),
#     ("Jessica", 24, "computação"),
#     ("Breno", 22, "Computação")
# ]
# #executemany pemite inserir multiplas linhas de uma vez só
# cursor.executemany("""
# INSERT INTO alunos(nome, idade, curso)
# VALUES(?, ?, ?)
# """,
# (alunos)
# )
# conexao.commit()

#Atualizar dados no banco 
# cursor.execute("""
# UPDATE alunos
# SET idade = ?, curso = ?
# WHERE id = ?              
# """, (61, "Medicina", 2)
# )
# conexao.commit()

#Função listar dados mo banco
# cursor.execute("SELECT * FROM alunos")
# #fetchall traz todos os dados da tabela
# for linha in cursor.fetchall():
#     print(f"ID: {linha[0]} | Nome: {linha[1]} | Idade: {linha[2]} | Curso: {linha[3]}")
# print("-" * 120)

# pesquisar = input("Digite o curso que deseja pesquisar: ")
# cursor.execute("SELECT nome, idade FROM alunos WHERE curso = ?", (pesquisar,))
# for linha in cursor.fetchall():
#     print(f"Nome: {linha[0]} | Idade: {linha[1]}") 


#Deletar dados do banco
# cursor.execute("DELETE FROM alunos WHERE id = ?", (1,))
# conexao.commit()
# #Sempre fechar a conexão com o banco de dados
# conexao.close()

def deletar_aluno(id_aluno):
    try:
        conexao = sqlite3.connect("escola.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
        
        #confirmando as alterações no banco
        conexao.commit()

        #Verificando se o aluno foi deletado
        if cursor.rowcount > 0:
            print(f"Aluno com ID {id_aluno} deletado com sucesso.")
        else:
            print(f"Nenhum aluno encontrado com o ID  fornecido.")
    except sqlite3.Error as error:
        print("Erro ao deletar o aluno:", error)
    finally:
        #Sempre fechar a conexão com o banco de dados
        if conexao:
            conexao.close()

deletar_aluno = int(input("Digite o ID do aluno que deseja deletar: "))
deletar_aluno(deletar_aluno)
