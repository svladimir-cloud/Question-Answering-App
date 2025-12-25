from transformers import pipeline

def pipe():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")