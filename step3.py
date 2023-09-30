import spacy
import requests

nlp = spacy.load("en_core_web_md")

            import spacy

. . .

def chatbot(statement):
  weather = nlp("Current weather in a city")
            statement = nlp(statement)
