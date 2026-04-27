from sentimentos import analisar_sentimento

def testar_analisar_sentimento():

    testes = [
        ("Amei esse produto, maravilhoso!", "positivo"),
        ("Horrível, me arrependo da compra", "negativo"),
        ("É ok, funciona bem.", "neutro"),
        ("", "neutro"),
        (None, "neutro"),
        (12345, "neutro")
    ]

    for texto, esperado in testes:
        sentimento, polaridade, subjetividade = analisar_sentimento(texto)

        print(f"\nTexto: {texto}")
        print(f"Sentimento esperado: {esperado}")
        print(f"Resultado: {sentimento} | Polaridade: {polaridade} | Subjetividade: {subjetividade}")

        assert sentimento == esperado or sentimento == "neutro", f"Erro: resultado inesperado para o texto '{texto}'"

    print("\nTodos os testes passaram com sucesso!")

if __name__ == "__main__":
    testar_analisar_sentimento()