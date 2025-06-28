import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import json
import os
from app.schemas import ClassificacaoOutput, HistoricoItem

# Carregar modelo e vetorizador
model = joblib.load('app/classifier/model.pkl')
vectorizer = joblib.load('app/classifier/vectorizer.pkl')

# Caminho do banco de dados local
historico_path = 'app/database.json'

# Se o arquivo não existir, cria vazio
if not os.path.exists(historico_path):
    with open(historico_path, 'w') as f:
        json.dump([], f)

# Função para carregar o histórico
def carregar_historico():
    try:
        with open(historico_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Caso arquivo vazio ou inválido, retorna lista vazia
        return []

# Função para salvar no histórico
def salvar_historico(historico_atual):
    with open(historico_path, 'w') as f:
        json.dump(historico_atual, f, ensure_ascii=False, indent=4)

# Carregar histórico inicial
historico = carregar_historico()

def classificar_texto(texto):
    vetor = vectorizer.transform([texto])
    prob = model.predict_proba(vetor)[0]
    classe = model.classes_[np.argmax(prob)]
    probabilidade = np.max(prob)

    # Extrair palavras influentes dinamicamente
    indices_texto = vetor.nonzero()[1]
    class_index = list(model.classes_).index(classe)
    coef = model.feature_log_prob_[class_index]
    feature_names = vectorizer.get_feature_names_out()

    palavras_pesos = []
    for i in indices_texto:
        palavra = feature_names[i]
        peso = vetor[0, i] * coef[i]
        palavras_pesos.append((palavra, peso))

    palavras_pesos.sort(key=lambda x: x[1], reverse=True)
    palavras_influentes = [p[0] for p in palavras_pesos[:3]]

    resultado = {
        "classe": classe,
        "probabilidade": round(probabilidade, 2),
        "palavras_influentes": palavras_influentes
    }

    # Atualizar e salvar no histórico
    historico.append({
        "texto": texto,
        "classe": classe,
        "probabilidade": round(probabilidade, 2)
    })
    salvar_historico(historico)

    return resultado

def get_model_status():
    return {"status": "modelo carregado", "modelo": str(model)}
