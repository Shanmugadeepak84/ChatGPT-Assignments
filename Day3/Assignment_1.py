from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained ChatGPT model and tokenizer
model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Prompt for ChatGPT text generation
prompt = "Write a short story about a magical adventure."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs, max_length=200, num_return_sequences=1, temperature=0.7)

# Decode and print the generated story
generated_story = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Story:\n", generated_story)
