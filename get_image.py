import psycopg2

# Define as informações de conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="teste",
    password="duffowned123"
)

# consulta a imagem na tabela
cur = conn.cursor()
cur.execute("SELECT dados_imagem FROM imagens WHERE id = %s", (1,))

# recupera os dados da imagem
dados_imagem = cur.fetchone()[0]

# grava a imagem em um arquivo
with open("imagem.jpg", "wb") as arquivo:
    arquivo.write(dados_imagem)

# fecha a conexão
conn.close()