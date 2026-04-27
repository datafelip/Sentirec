import mysql.connector as sql
from mysql.connector import Error


def conectar():
    try:
        return sql.connect(
                host = 'localhost',
                port = '3306',
                user = 'root',
                password = '#Fvaf221205',
                database = 'db_sistemas_recomendacao' 
            )
    except Error as e:
        print(f"Erro ao se conectar: {e}")
        return None

def executar_consulta(consulta, parametros=None):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(consulta, parametros or ())
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados
    
def executar_comando(consulta, parametros=None):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute(consulta, parametros or ())
            conexao.commit()
        except Error as e:
            print(f"Erro ao executar comando: {e}")
            conexao.rollback()
        finally:
            cursor.close()
            conexao.close()