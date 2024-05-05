import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import emoji

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from joblib import load

import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('spanish'))
nltk.download('punkt')
nltk.download('wordnet')

import re
import pickle
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def Db_Analisis(route: str) -> str:
    df = pd.read_csv(route)
    df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y")
    df["Palabras"] = [len(msg.split()) for msg in df["tweet"]]
    df.drop("time", axis = 1, inplace = True)

    #demojize
    for i in range(len(df)):
        df.loc[i,'tweet'] = emoji.demojize(df.loc[i,'tweet'], language='es')
    
    # Función para preprocesar el texto
    def preprocess_text(text):
        # Tokenize the text
        tokens = word_tokenize(text.lower())

        # Remove stop words
        filtered_tokens = [token for token in tokens if token not in stopwords.words('spanish')]

        # Lemmatize the tokens
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

        # Join the tokens back into a string
        processed_text = ' '.join(lemmatized_tokens)
    
    
        # ----------- LIMPIAR CARACTERES Y PALABRAS ----------------
        processed_text = processed_text.replace(',', '')
        processed_text = processed_text.replace('.', '')
        processed_text = processed_text.replace(':', '')
        processed_text = processed_text.replace(',', '')
        processed_text = processed_text.replace('!', '')
        processed_text = processed_text.replace('¡', '')
        #processed_text = processed_text.replace('gracias', '')
        #processed_text = processed_text.replace('muchas', '')
    
        #processed_text = processed_text.replace('_', ' ')
        #processed_text = processed_text.replace('cara', '')
    

        return processed_text
    
    df['procTweet'] = df['tweet'].apply(preprocess_text)
    # Eliminar las filas con texto vacío
    df = df.loc[df['procTweet'] != '', :]

    #predecir sentimiento
    modelSentiment = load(r'data\modelSentiment.joblib')
    scaler = load(r'data\scaler.joblib')
    vectorizer = load(r'data\vectorizer.joblib')

    corpus = []
    stemmer = PorterStemmer()
    for i in range(0, df.shape[0]):
        review = re.sub('[^a-zA-Z]', ' ', df.iloc[i]['procTweet'])
        review = review.lower().split()
        review = [stemmer.stem(word) for word in review if not word in STOPWORDS]
        review = ' '.join(review)
        corpus.append(review)
    
    #Storing independent and dependent variables in X and y
    X = vectorizer.transform(corpus).toarray()

    X = scaler.transform(X)

    df['Sentimiento'] = modelSentiment.predict(X)

    #predecir relevancia
    modelRel = load(r'data\modelRel.joblib')
    df['relevance'] = modelRel.predict(X)

    #predecir topic
    modelTopic = load(r'data\modelTopic.joblib')
    df['topic'] = modelTopic.predict(X) 
    df.to_csv('OUT\dbParaAnalisis.csv', index = False)
    return 'OUT\dbParaAnalisis.csv'