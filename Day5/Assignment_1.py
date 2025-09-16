from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained ChatGPT model and tokenizer for content generation
model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Input for social media post generation
post_input = "Exciting news! We are launching a new product that will revolutionize the industry."

# Tokenize and generate social media post
inputs = tokenizer(post_input, return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=150, num_return_sequences=1, temperature=0.9)

# Decode and print the generated social media post
generated_post = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Social Media Post:\n", generated_post)
