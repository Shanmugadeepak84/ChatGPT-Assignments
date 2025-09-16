from transformers import GPT2CodeLMHeadModel, GPT2Tokenizer

# Load pre-trained ChatGPT model and tokenizer for code generation
model_name = "microsoft/CodeGPT-small-java"
model = GPT2CodeLMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Input task description
task_description = "Write a Python function to calculate the factorial of a given number."

# Tokenize and generate code
inputs = tokenizer(task_description, return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=100, num_return_sequences=1, temperature=0.9)

# Decode and print the generated code
generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Code:\n", generated_code)
