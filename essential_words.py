from transformers import pipeline

def get_important_words(text, model_name="distilbert-base-uncased"):
    # Load the model and tokenizer
    nlp = pipeline("feature-extraction", model=model_name)
    
    # Get the model outputs
    outputs = nlp(text)
    
    # Sum the outputs across the token dimension to get the importance of each word
    word_importance = [sum(token) for token in outputs[0]]
    
    # Get the words from the tokenizer
    tokenizer = nlp.tokenizer
    tokens = tokenizer.tokenize(text)
    
    # Pair the words with their importance
    important_words = list(zip(tokens, word_importance))
    
    # Sort the words by importance
    important_words.sort(key=lambda x: x[1], reverse=True)
    
    return important_words
