import mysql.connector as sql
from mysql.connector import Error
from db import conectar, executar_comando, executar_consulta

if __name__ == "__main__":
    print("<<<<Testando conexao e comandos>>>>")

    #Testando a conexão com o banco
    conexao = conectar()
    if conexao:
        print('conectado com sucesso')

#Testando execução de consulta com o comando INSERT INTO
def testar_insert():
    nome_teste = "Usuario teste"
    email_teste = "email@teste.com"

    print("Inserindo o usuario no banco")

    inserir_usuario =  '''
            INSERT INTO tbl_usuarios(nome_usuario, email)
            VALUES(%s, %s)
'''
    executar_comando(inserir_usuario, (nome_teste, email_teste))

#Testando execução de consulta com o comando SELECT
def testar_select():
    email_teste = "email@teste.com"

    print("Consultando usuario no banco")

    verificar_select = '''
        SELECT * FROM tbl_usuarios 
        WHERE email = %s
    '''

    resultados = executar_consulta(verificar_select, (email_teste,))
    if resultados:
        print("A consulta funcionou perfeitamente. Resultado: ")
        for linha in resultados:
            print(linha)
            id_teste = linha['id_usuario']
    else:
        print("Nenhum resultado encontrado.")

def testar_delete():
    email_teste = "email@teste.com"

    print("Limpando teste (removendo usuário)")

    excluir = """
        DELETE FROM tbl_usuarios WHERE email = %s
    """
    executar_comando(excluir, (email_teste,))
    print("Teste finalizado.")

#Testes em blocos

# testar_insert()
# testar_select()
# testar_delete()
