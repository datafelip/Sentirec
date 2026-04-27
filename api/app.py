import sys
import os

# Adiciona a pasta src ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, HTTPException
from api.coletar import coletar_avaliacoes
from api.preprocess import aplicar_processamento
from api.recomendacoes import gerar_recomendacoes

app = FastAPI(title="API Sentirec")

@app.get("/")
def raiz():
    
    return{
        "mensagem": "API de avaliação de sentimentos Sentirec funcionando com sucesso."
    }

@app.get("/recomendar")
def recomendar(id_usuario: int, top_n: int = 5):
    df = coletar_avaliacoes()

    if df.empty:
        # A família 400 é significado de bad request, caso o df de avaliações esteja vazio.
        raise HTTPException(status_code=400, detail="Nenhuma avaliação encontrada.")

    df_processado = aplicar_processamento(df)

    try:
        recomendacoes = gerar_recomendacoes(df_processado, id_usuario, top_n)
    except ValueError as e:
        # A família 500 é erro interno de servidor.
        raise HTTPException(status_code=500, detail=str(e))
    
    if not recomendacoes:
        return {
            "mensagem": "Nenhuma recomendação gerada para este usuário"
        }
    
    lista_final = []

    for id_produto, peso in recomendacoes:
        nome = df.loc[df["id_produto"] == id_produto, "nome_produto"].values[0]
        lista_final.append({
            "id_produto": int(id_produto),
            "nome": nome,
            "nota_sentimento": round(float(peso), 2)
        })

    return {
        "usuario": id_usuario,
        "recomendacoes": lista_final
    }

#Endereço da API: http://127.0.0.1:8000/docs/
