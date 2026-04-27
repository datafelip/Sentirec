from textblob import TextBlob
from deep_translator import GoogleTranslator
from db import conectar

def analisar_sentimento(texto):
    if not isinstance(texto, str) or not texto.strip():
        return "neutro", 0.0, 0.0

    try:
        # Traduz o texto de português para inglês usando Deep Translator
        texto_em_ingles = GoogleTranslator(source='auto', target='en').translate(texto)
        blob = TextBlob(texto_em_ingles)

        polaridade = blob.sentiment.polarity
        subjetividade = blob.sentiment.subjectivity

        if polaridade > 0.1:
            sentimento = "positivo"
        elif polaridade < -0.1:
            sentimento = "negativo"
        else:
            sentimento = "neutro"

        return sentimento, polaridade, subjetividade

    except Exception as e:
        print(f"Erro ao analisar sentimento: {e}")
        return "neutro", 0.0, 0.0

def processar_sentimentos(limite=None):
    print("Coletando avaliações do banco de dados...")
    conexao = conectar()
    if not conexao:
        print("Não foi possível conectar ao banco.")
        return

    cursor = conexao.cursor(dictionary=True)

    consulta = "SELECT id_avaliacao, texto FROM tbl_avaliacoes WHERE texto IS NOT NULL"
    if limite:
        consulta += f" LIMIT {limite}"
    cursor.execute(consulta)
    avaliacoes = cursor.fetchall()

    print(f"Analisando {len(avaliacoes)} avaliações...")

    dados_para_inserir = []

    for i, avaliacao in enumerate(avaliacoes, 1):
        id_avaliacao = avaliacao['id_avaliacao']
        texto = avaliacao['texto']
        sentimento, polaridade, subjetividade = analisar_sentimento(texto)

        dados_para_inserir.append(
            (id_avaliacao, sentimento, polaridade, subjetividade)
        )

        if i % 1000 == 0 or i == len(avaliacoes):
            print(f"{i} avaliações analisadas...")

    comando = '''
        INSERT INTO tbl_sentimentos (id_avaliacao, sentimento, polaridade, subjetividade)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            sentimento = VALUES(sentimento),
            polaridade = VALUES(polaridade),
            subjetividade = VALUES(subjetividade)
    '''

    try:
        cursor.executemany(comando, dados_para_inserir)
        conexao.commit()
        print("Todos os sentimentos foram salvos no banco com sucesso.")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao salvar os dados: {e}")
    finally:
        cursor.close()
        conexao.close()


if __name__ == '__main__':
    processar_sentimentos(limite=100)
