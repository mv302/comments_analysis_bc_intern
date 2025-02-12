from transformers import pipeline

# Load the emotion classification pipeline
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def classify_emotion(text):
    result = emotion_classifier(text)
    return result
