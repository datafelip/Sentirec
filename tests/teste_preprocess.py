import pandas as pd
from preprocess import aplicar_processamento

dados = {
    'id_avaliacao': [1, 2, 3],
    'texto': ["This product is AMAZING! I've used it for 2 weeks and it's fantastic.",
              "Terrible quality... Broke after 1 use. Never buying again",
              "Okay, but not the best but does the job. Worth the price?"
              ]
}

df = pd.DataFrame(dados)

print("Textos originais: ")
print(df[['id_avaliacao', 'texto']])
print()


df['texto_limpo'] = aplicar_processamento(df['texto'])

print("Textos limpos: ")
print(df[['id_avaliacao', 'texto_limpo']])
