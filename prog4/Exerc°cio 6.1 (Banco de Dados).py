import sqlite3

# Iniciar conexão com o Banco de Dados
conexao = sqlite3.connect("brasil.db")
cursor = conexao.cursor()

# Criar tabela estados com nome e população
cursor.execute('''
CREATE TABLE estados (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    populacao INTEGER
    );
''')

# Inserir dados na tabela estados
cursor.execute('''
    INSERT INTO estados (nome, populacao) 
    values (?, ?)''', ("Acre", "869 265"))

# criando uma lista de dados
lista = [(
        'São Paulo', '45 538 936'),
        ('Minas Gerais', '21 040 662'),
        ('Rio de Janeiro', '17 159 960'),
        ('Bahia', '14 812 617'
    )]

# inserindo dados na tabela
cursor.executemany("""
    INSERT INTO estados (nome,populacao)
    VALUES (?,?)
    """, lista)



conexao.commit()
cursor.close()
conexao.close()
