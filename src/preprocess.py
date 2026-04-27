import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-z\s]', " ", texto)
    tokens = nltk.word_tokenize(texto)
    tokens = [palavra for palavra in tokens if palavra not in stop_words]
    tokens = [lemmatizer.lemmatize(palavra) for palavra in tokens]
    return ' '.join(tokens)


def aplicar_processamento(df):
    df = df.copy()
    df['texto_limpo'] = df['comentario'].apply(limpar_texto)  
    df['polaridade'] = df['texto_limpo'].apply(lambda texto: TextBlob(texto).sentiment.polarity)
    return df
