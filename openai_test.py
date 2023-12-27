from openai import OpenAI
import os
client = OpenAI()

completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role' : 'system', 'content': 'You are a poetic assistant, skilled in explaining complex programming concepts with creative flair'},
        {'role': 'user', 'content': 'compose a poem that explains the concepts of recursion in programming'}
    ]
)

x = (completion.choices[0].message)  
print(x)