from emotions import classify_emotion
from essential_words import get_important_words
from llm_call import llm_call
from sentiment import analyze_sentiment

# Sample list of comments
comments = [
    "I love this product! It's amazing.",
    "This is the worst experience I've had.",
    "It's okay, but could be better.",
    "Absolutely fantastic service!",
    "I don't know what to think about this."
]

# Process each comment
for comment in comments:
    print(f"Comment: {comment}")
    print(f"Emotion: {classify_emotion(comment)}")
    print(f"Important Words: {get_important_words(comment)}")
    print(f"LLM Output: {llm_call(comment)}")
    print(f"Sentiment: {analyze_sentiment(comment)}")
    print("-" * 150)
