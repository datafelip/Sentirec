import pandas as pd
from db import conectar

def carregar_dados():
  
    conexao = conectar()
    if not conexao:
        print("Erro ao conectar no banco.")
        return None, None

    query_avaliacoes = '''
        SELECT a.id_usuario, a.id_produto, a.nota, s.polaridade
        FROM tbl_avaliacoes a
        JOIN tbl_sentimentos s ON a.id_avaliacao = s.id_avaliacao
    '''
    df = pd.read_sql(query_avaliacoes, conexao)
    conexao.close()
    return df

def gerar_recomendacoes(df, usuario_id, top_n=5):
    
    # Gera recomendações de produtos com base na média ponderada das notas e polaridade.
    
    if df is None or df.empty:
        print("DataFrame de avaliações vazio.")
        return []

    # Cálculo da média ponderada: nota * (1 + polaridade)
    df['peso'] = df['nota'] * (1 + df['polaridade'])

    # Agrupa por produto e tira a média ponderada
    recomendacoes = df.groupby('id_produto')['peso'].mean().reset_index()

    # Remove produtos que o usuário já avaliou
    produtos_avaliados = df[df['id_usuario'] == usuario_id]['id_produto'].unique()
    recomendacoes = recomendacoes[~recomendacoes['id_produto'].isin(produtos_avaliados)]

    # Ordena pelas melhores médias e pega o top N
    recomendacoes = recomendacoes.sort_values(by='peso', ascending=False).head(top_n)

    return recomendacoes['id_produto'].tolist()

if __name__ == "__main__":
    usuario_alvo = 1
    df = carregar_dados()
    recomendados = gerar_recomendacoes(df, usuario_alvo)
    print(f"Produtos recomendados para o usuário {usuario_alvo}: {recomendados}")
