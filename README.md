# 🎬 Movie Review Sentiment Analysis

A complete NLP project for classifying movie reviews as Positive or Negative using Word2Vec and Logistic Regression.

---

## Features

- Text Cleaning
- Tokenization
- Stopword Removal
- POS Tagging
- Lemmatization
- Word2Vec Embeddings
- Logistic Regression Classification
- Streamlit Web Application

---

## Dataset

IMDb Movie Reviews Dataset

25000 reviews

Binary Classification:
- Positive
- Negative

---

## Technologies

- Python
- NLTK
- Gensim
- Scikit-learn
- Streamlit
- NumPy

---

## Model

Word2Vec (Skip-Gram)

↓

Average Word Embeddings

↓

Logistic Regression

Accuracy: **86.1%**

---

## Project Structure

```text
app.py
predict.py
preprocess.py
models/
```

---

## Run

```bash
pip install -r requirements.txt

streamlit run app.py
```