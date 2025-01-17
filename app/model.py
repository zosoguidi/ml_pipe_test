import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

class SentimentModel:
    def get_sentimentanalysis(self, text):
        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe("spacytextblob")
        doc = nlp(text)
        polarity = doc._.polarity
        subjectivity = doc._.subjectivity
        if polarity>0:
            result = 'POSITIVE'
        elif polarity<0:
            result= 'NEGATIVE'
        else:
            result= 'NEUTRAL'
        return polarity, subjectivity, result