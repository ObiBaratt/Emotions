from textblob import TextBlob


def basic_text_sentiment(text):
    blob = TextBlob(text)
    print(blob.sentiment)


text = 'I had a really horrible day. It was the worst day ever! ' \
       'But every now and then I have a really good day that makes me happy.'

basic_text_sentiment(text)
