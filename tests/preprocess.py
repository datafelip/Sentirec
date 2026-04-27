import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def limpar_texto(texto):
    texto = texto.lower() 
    texto = re.sub(r'[^a-z\s]', '', texto)  
    tokens = nltk.word_tokenize(texto)  
    tokens = [palavra for palavra in tokens if palavra not in stop_words]  
    tokens = [lemmatizer.lemmatize(palavra) for palavra in tokens]  
    texto_limpo = ' '.join(tokens)
    return texto_limpo 


def aplicar_processamento(lista_de_texto):
    return [limpar_texto(texto) for texto in lista_de_texto]