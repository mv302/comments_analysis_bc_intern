import requests

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
HF_TOKEN = "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"  # Replace with your actual token

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def llm_call(input):
    output = query({"inputs": f"Analyse this LLM Input and give a very short inference for this comment : {input}"})
    print(output)
    return output
