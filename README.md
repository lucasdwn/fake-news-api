
# Fake News Classifier API

Este projeto é uma API REST desenvolvida em FastAPI para classificação automática de notícias em **fake** ou **true** (falsas ou verdadeiras). O modelo é treinado utilizando um dataset de notícias em português.

---

## Dataset Utilizado

Para o treinamento do modelo, utilizamos o dataset disponível no repositório:

[Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

Este dataset contém notícias em português com rótulos **fake** e **true**, além de textos pré-processados para facilitar o uso em modelos de aprendizado de máquina.

No projeto, o arquivo utilizado foi `pre-processed.csv`, com as seguintes colunas:

- `index`: índice da notícia  
- `label`: rótulo da notícia (fake ou true)  
- `preprocessed_news`: texto da notícia já pré-processado  

---

## Estrutura do Projeto

```text
fake-news-api/
│
├── app/
│   ├── main.py            # Aplicação FastAPI principal
│   ├── models.py          # Lógica de carregamento e classificação do modelo
│   ├── routes.py          # Definição das rotas da API
│   ├── schemas.py         # Schemas Pydantic para validação
│   ├── training.py        # Script para treinamento do modelo
│   ├── classifier/        # Modelos treinados e vetorizadores (.pkl)
│   ├── database.json      # Histórico das classificações feitas
│   └── utils.py           # Funções auxiliares (opcional)
│
├── pre-processed.csv      # Dataset para treinamento (baixado do Fake.br-Corpus)
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```
---

## Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-seu-repositorio>
cd fake-news-api
````

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Treinar o modelo (opcional)

Para treinar o modelo do zero, execute:

```bash
python app/training.py
```

Isso irá gerar os arquivos `model.pkl` e `vectorizer.pkl` na pasta `app/classifier`.

### 4. Rodar a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://127.0.0.1:8000`

---

## Endpoints Disponíveis

* **POST /api/classificar-noticia**

  Envia um texto para classificação (fake ou true).

  Exemplo de corpo da requisição:

  ```json
  {
    "texto": "exemplo de texto da notícia para classificar"
  }
  ```

* **GET /api/historico**

  Retorna o histórico de classificações feitas.

* **GET /api/status**

  Retorna o status atual do modelo carregado.

---

## Requisitos do Projeto

* Python 3.10+
* fastapi
* uvicorn
* scikit-learn
* joblib
* numpy
* pydantic

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

---

## Referências

* Dataset Fake.br-Corpus: [https://github.com/roneysco/Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)
