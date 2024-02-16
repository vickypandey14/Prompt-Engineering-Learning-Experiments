import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

dotenv_loaded = load_dotenv(find_dotenv())

# if dotenv_loaded:
#     openai_api_key = os.getenv('OPENAI_API_KEY')
#     if openai_api_key:
#         print("Dotenv file loaded and OPENAI_API_KEY is set.")
#     else:
#         print("Dotenv file loaded but OPENAI_API_KEY is not set.")
# else:
#     print("Dotenv file not found.")


openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# this is an example of Tactic 4: "Few-shot" prompting
# here in this example the model will always answer in the provided consistent style

prompt = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \ 
valley flows from a modest spring; the \ 
grandest symphony originates from a single note; \ 
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about importance of water.
"""
response = get_completion(prompt)
print(response)