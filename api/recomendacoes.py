import pandas as pd
from api.db import conectar

def carregar_dados():
  
    conexao = conectar()
    if not conexao:
        print("Erro ao conectar no banco.")
        return None, None

    query_avaliacoes = '''
        SELECT a.id_usuario, a.id_produto, a.nota, s.polaridade
        FROM tbl_avaliacoes AS a
        JOIN tbl_sentimentos AS s ON a.id_avaliacao = s.id_avaliacao
    '''
    df = pd.read_sql(query_avaliacoes, conexao)
    conexao.close()
    return df


def gerar_recomendacoes(df, usuario_id, top_n=5):
    if df is None or df.empty:
        return []

    if not {'id_usuario', 'nome_produto', 'nota', 'polaridade'}.issubset(df.columns):
        raise ValueError("O DataFrame precisa conter as colunas: id_usuario, nome_produto, nota e polaridade.")

    df['peso'] = df['nota'] * (1 + df['polaridade'])

    produtos_avaliados = df[df['id_usuario'] == usuario_id]['nome_produto'].unique()
 
    df_filtrado = df[~df['nome_produto'].isin(produtos_avaliados)]

    recomendacoes_df = df_filtrado.groupby('nome_produto')['peso'].mean().reset_index()
    
    recomendacoes_df = recomendacoes_df.sort_values(by='peso', ascending=False).head(top_n)
    
    recomendacoes = list(recomendacoes_df.itertuples(index=False, name=None))

    return recomendacoes


if __name__ == "__main__":
    usuario_alvo = 1
    df = carregar_dados()
    recomendados = gerar_recomendacoes(df, usuario_alvo)
    print(f"Produtos recomendados para o usuário {usuario_alvo}: {recomendados}")
