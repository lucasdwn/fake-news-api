import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib

# Caminho do dataset
dataset_path = 'datasets/pre-processed.csv'

# Carregar dataset
df = pd.read_csv(dataset_path)

# Verificar dados carregados (opcional)
print(f"Linhas no dataset: {len(df)}")
print(df.head())

# Separar features e labels
X = df['preprocessed_news']
y = df['label']

# Vetorização TF-IDF (como texto já está pré-processado, não passa stopwords)
vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Treinar modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Avaliar modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Salvar modelo e vetorizador
joblib.dump(model, 'app/classifier/model.pkl')
joblib.dump(vectorizer, 'app/classifier/vectorizer.pkl')

print("✅ Modelo e vetorizador salvos com sucesso!")
