import pymorphy2
from matplotlib import pyplot
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer

punc_str = "!()-[]{};:@#$%^',.\|/*-<>_~'"
morph = pymorphy2.MorphAnalyzer()
raw_text = input("Введите текст\n")
sentences = sent_tokenize(raw_text, language='russian')
stop_words = set(stopwords.words('russian'))


def stemming(text):
    words = word_tokenize(text, language='russian')
    snowball = SnowballStemmer(language='russian')
    filtered_words = list()

    for w in words:
        if (w not in stop_words) and (w not in punc_str):
            filtered_words.append(w)

    unique_stemms = list()
    ps = PorterStemmer()
    for filt_word in filtered_words:
        Word=snowball.stem(filt_word)
        if Word not in unique_stemms:
            unique_stemms.append(Word)
    return unique_stemms


count_vectorizer = CountVectorizer()
string = [''.join(line) for line in sentences]
bag_of_words = count_vectorizer.fit_transform(string)
feature_names = count_vectorizer.get_feature_names_out()
print('\nТокен Векторизция')
print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names[:50]))


count_stemming_lemms=CountVectorizer(tokenizer=stemming)
bag_of_words = count_stemming_lemms.fit_transform(string)
feature_names = count_stemming_lemms.get_feature_names_out()
print('Стемма Векторизация')
print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names[:37]))