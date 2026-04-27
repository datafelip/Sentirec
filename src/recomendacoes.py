import pandas as pd
from db import conectar

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

    # Garante que as colunas existam
    if not {'id_usuario', 'nome_produto', 'nota', 'polaridade'}.issubset(df.columns):
        raise ValueError("O DataFrame precisa conter as colunas: id_usuario, nome_produto, nota e polaridade.")

    # Adiciona a coluna 'peso' (nota ajustada pela polaridade)
    df['peso'] = df['nota'] * (1 + df['polaridade'])

    # Produtos que o usuário já avaliou
    produtos_avaliados = df[df['id_usuario'] == usuario_id]['nome_produto'].unique()

    # Produtos ainda não avaliados por esse usuário
    df_filtrado = df[~df['nome_produto'].isin(produtos_avaliados)]

    # Agrupa por produto, tirando a média dos pesos
    recomendacoes_df = df_filtrado.groupby('nome_produto')['peso'].mean().reset_index()

    # Ordena pelas maiores médias
    recomendacoes_df = recomendacoes_df.sort_values(by='peso', ascending=False).head(top_n)

    # Converte para lista de tuplas
    recomendacoes = list(recomendacoes_df.itertuples(index=False, name=None))

    return recomendacoes


if __name__ == "__main__":
    usuario_alvo = 1
    df = carregar_dados()
    recomendados = gerar_recomendacoes(df, usuario_alvo)
    print(f"Produtos recomendados para o usuário {usuario_alvo}: {recomendados}")
