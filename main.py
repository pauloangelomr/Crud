import mysql.connector


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
   password = 'P@ulo020185',
   database = 'bdyoutube',
)

cursor = conexao.cursor()


#CRUD
nome_produto = 'pangaia'
valor =190
comando = f"DELETE  FROM vendas WHERE nome_produto = '{nome_produto}' "
cursor.execute(comando)
conexao.commit() # edita o banco de dados




cursor.close()
conexao.close()


#CREATE
#nome_produto = 'pamonha'
#valor = 150
#comando = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}' ,{valor})"
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

#READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


#UPDATE
#nome_produto = "pangaia"
#valor =190
#comando = f'UPDATE vendas SET  valor = {valor} WHERE nome_produto = "{nome_produto}" '
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

#DELETE
#nome_produto = 'pangaia'
#valor =190
#comando = f"DELETE  FROM vendas WHERE nome_produto = '{nome_produto}' "
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados
