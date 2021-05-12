from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):


    analyser = SentimentIntensityAnalyzer()
    sentiment_scores = analyser.polarity_scores(text)
    return sentiment_scores
    