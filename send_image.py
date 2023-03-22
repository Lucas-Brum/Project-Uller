import psycopg2

with open("imagem.jpg", "rb") as arquivo:
    dados_imagem = arquivo.read()
    
# Define as informações de conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="teste",
    password="duffowned123"
)

# insere a imagem na tabela
cur = conn.cursor()
cur.execute("INSERT INTO imagens (dados_imagem) VALUES (%s)", (dados_imagem,))
conn.commit()

# fecha a conexão
conn.close()