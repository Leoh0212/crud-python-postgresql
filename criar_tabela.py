# pip install faker
# pip install tk

import psycopg
import psycopg2

# Criar conexão
conexao = psycopg.connect(
            host="localhost",
            dbname="crud_db",
            user="postgres",
            password="admin123",
            port=5432
        )
print("Conexão com o Banco de Dados aberta com sucesso!")

# Criação do cursor
meu_cursor = conexao.cursor()

if __name__ == '__main__':
    # Criação da tabela
    meu_cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY UNIQUE,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
        );
    ''')

    # just in case
    conexao.commit()
    print("Tabela criada com sucesso!")
    conexao.close()