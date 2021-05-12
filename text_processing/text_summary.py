import nltk
from collections import defaultdict
import heapq

def generate_summary(article_text, sentence_list):


    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = defaultdict(int)

    for word in nltk.word_tokenize(article_text):
        if word.lower() not in stopwords:
            word_frequencies[word.lower()] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] /= maximum_frequency

    sentence_scores = defaultdict(int)

    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 30:
                    sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    return ' '.join(summary_sentences)
