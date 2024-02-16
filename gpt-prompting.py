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

# Example: 1 (Use delimiters to clearly indicate distinct parts of the input Delimiters can be anything like: ```, """, < >, <tag> </tag>, :)

# text = f"""
# Lorem ipsum dolor sit amet
# """
# prompt = f"""
# Summarize the text and also give me a joke about this text
# ```{text}```
# """
# response = get_completion(prompt)
# print(response)

# Example: 2 (Ask for a structured output)

# prompt = f"""
# Generate a list of 5 made-up book titles along \ 
# with their authors and genres. 
# Provide them in JSON format with the following keys: 
# book_id, title, author, genre.
# """
# response = get_completion(prompt)
# print(response)

# Example: 3 (Ask the model to check whether conditions are satisfied)

# text_1 = f"""
# Making a cup of tea is easy! First, you need to get some \ 
# water boiling. While that's happening, \ 
# grab a cup and put a tea bag in it. Once the water is \ 
# hot enough, just pour it over the tea bag. \ 
# Let it sit for a bit so the tea can steep. After a \ 
# few minutes, take out the tea bag. If you \ 
# like, you can add some sugar or milk to taste. \ 
# And that's it! You've got yourself a delicious \ 
# cup of tea to enjoy.
# """
# prompt = f"""
# You will be provided with text delimited by triple quotes. 
# If it contains a sequence of instructions, \ 
# re-write those instructions in the following format:

# Step 1 - ...
# Step 2 - …
# …
# Step N - …

# If the text does not contain a sequence of instructions, \ 
# then simply write \"No steps provided.\"

# \"\"\"{text_1}\"\"\"
# """
# response = get_completion(prompt)
# print("Completion for Text 1:")
# print(response)


# Example: 4 same as the example 3 But For only when the steps is not provided

text_2 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \ 
walk in the park. The flowers are blooming, and the \ 
trees are swaying gently in the breeze. People \ 
are out and about, enjoying the lovely weather. \ 
Some are having picnics, while others are playing \ 
games or simply relaxing on the grass. It's a \ 
perfect day to spend time outdoors and appreciate the \ 
beauty of nature.
"""
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided.\"

\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 2:")
print(response)