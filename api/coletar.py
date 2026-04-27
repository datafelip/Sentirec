from mysql.connector import Error
import pandas as pd
from api.db import conectar
  
def coletar_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary = True)

    consulta = '''
        SELECT id_usuario, id_produto, texto, nota
        FROM tbl_avaliacoes
        WHERE texto IS NOT NULL AND nota IS NOT NULL  
'''
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    df = pd.DataFrame(resultados)

    df = df.rename(columns={
        "id_produto": "nome_produto",
        "texto": "comentario"
    })
    return df

if __name__ == "__main__":
    conectar()
    print("Conectado com sucesso.")