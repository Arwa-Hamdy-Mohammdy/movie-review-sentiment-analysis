import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    else:
        return wordnet.NOUN

def pos_lemmatize(tokens):

    tagged = pos_tag(tokens)

    lemmas = []

    for word, tag in tagged:

        pos = get_wordnet_pos(tag)

        lemma = lemmatizer.lemmatize(word, pos)

        lemmas.append(lemma)

    return lemmas

def preprocess(text):

    text = text.lower()

    text = re.sub(r"<.*?>", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    text = text.translate(str.maketrans("", "", string.punctuation))

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]

    tokens = pos_lemmatize(tokens)

    processed_text = " ".join(tokens)

    return processed_text

