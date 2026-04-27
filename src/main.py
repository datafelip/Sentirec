from coletar import coletar_avaliacoes
from preprocess import aplicar_processamento
from recomendacoes import gerar_recomendacoes

def main():
    print("Carregando dados...")
    df = coletar_avaliacoes()

    if df.empty:
        print("Nenhum dado encontrado. Verifique a tabela no banco de dados.")
        return

    df.rename(columns={
        "id_produto": "nome_produto",
        "texto": "comentario"
    }, inplace=True)

    print("Dados carregados com sucesso!")

    print("\nPré-processando os dados...")
    df_processado = aplicar_processamento(df)
    print("Pré-processamento concluído!")

    try:
        usuario_id = int(input("\nDigite o ID do usuário para recomendações: "))
    except ValueError:
        print("ID inválido. Digite um número inteiro.")
        return

    print(f"\nGerando recomendações para o usuário {usuario_id}...")
    try:
        recomendacoes = gerar_recomendacoes(df_processado, usuario_id, top_n=5)

        if not recomendacoes:
            print("Nenhuma recomendação encontrada para este usuário.")
        else:
            print("\nRecomendações:")
            for produto, nota in recomendacoes:
                print(f"Produto {produto} (peso ajustado: {nota:.2f})")
    except ValueError as e:
        print(f"Erro ao gerar recomendações: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
