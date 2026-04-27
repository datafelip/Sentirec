import unittest
import pandas as pd
from recomendacoes import gerar_recomendacoes  # Certifique-se de importar corretamente

class TestRecomendacoes(unittest.TestCase):
    
    def setUp(self):
        # (opcional) configurações para todos os testes
        pass

    def test_dataframe_vazio(self):
        # Seu teste de DataFrame vazio
        pass

    def test_gerar_recomendacoes_usuario_1(self):
        # Seu teste de recomendações para usuário 1
        pass

    def test_gerar_recomendacoes_usuario_inexistente(self):
        # Seu teste de usuário inexistente
        pass

    def test_recomendacoes_reais(self):
        """
        Testa a geração de recomendações reais com um DataFrame de avaliações.
        Verifica se os produtos recomendados para o usuário 1 são corretos.
        """
        dados = {
            'id_usuario': [1, 1, 1, 2, 2, 3, 3, 3],
            'id_produto': [101, 102, 103, 101, 104, 105, 102, 106],
            'nota':  [5.0, 3.0, 4.0, 5.0, 4.0, 2.0, 3.0, 4.0],
            'polaridade': [0.8, 0.2, 0.5, 0.9, 0.4, 0.1, 0.3, 0.6]
        }
        df_simulado = pd.DataFrame(dados)

        resultado = gerar_recomendacoes(df_simulado, usuario_id=1, top_n=2)

        avaliados_usuario_1 = set(df_simulado[df_simulado['id_usuario'] == 1]['id_produto'])
        recomendados = resultado

        for prod_id in recomendados:
            self.assertNotIn(prod_id, avaliados_usuario_1)

        self.assertEqual(len(resultado), 2)
        print("✅ Teste com recomendações reais passou com sucesso.")

if __name__ == '__main__':
    unittest.main()
