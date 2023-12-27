import openai

# Set your API key
openai.api_key = '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'

# Define a prompt
prompt = "Translate the following English text to French: '{}'"
english_text = "Hello, how are you?"

# Call the OpenAI API to generate a completion
response = openai.Completion.create(
    engine="text-davinci-003",  # Choose the engine (check the OpenAI documentation for available engines)
    prompt=prompt.format(english_text),
    max_tokens=50,  # Set the maximum number of tokens in the generated text
    n=1,  # Number of completions to generate
)

# Extract the generated text from the response
generated_text = response['choices'][0]['text']

# Print the generated text
print(generated_text)
