# .venv\Scripts\activate
import joblib
import numpy as np

from gensim.models import Word2Vec

from preprocess import preprocess

model = joblib.load("models/sentiment_model.pkl")


word2vec = Word2Vec.load("models/word2vec.model")

def document_vector(words, model):

    vectors = []

    for word in words:

        if word in model.wv:

            vectors.append(model.wv[word])

    if len(vectors) == 0:

        return np.zeros(model.vector_size)

    return np.mean(vectors, axis=0)

def predict_sentiment(review):

    processed_review = preprocess(review)

    tokens = processed_review.split()

    vector = document_vector(tokens, word2vec)

    vector = vector.reshape(1, -1)

    prediction = model.predict(vector)

    probability = model.predict_proba(vector)

    confidence = probability.max()

    result = "Positive" if prediction[0] == 1 else "Negative"

    return result, confidence