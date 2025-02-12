from transformers import pipeline

# Load the sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    # Perform sentiment classification
    result = classifier(text)
    # Return the result
    return result
