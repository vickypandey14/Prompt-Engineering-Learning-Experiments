## Model Limitations: Hallucinations ##
## - meta is a real company, the product name is not real. ##

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

dotenv_loaded = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

prompt = f"""
Tell me about toothbrush by meta
"""
response = get_completion(prompt)
print(response)