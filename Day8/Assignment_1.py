from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained ChatGPT model and tokenizer
model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Input prompt for generating concise instructions
prompt = "Provide step-by-step instructions on how to make a chocolate cake."

# Tokenize and generate instructions based on the prompt
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=300, num_return_sequences=1, temperature=0.9)

# Decode and print the generated instructions
generated_instructions = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Instructions:\n", generated_instructions)
