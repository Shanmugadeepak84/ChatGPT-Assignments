from transformers import GPT3Model, GPT4Model

# Load pre-trained GPT-3 and GPT-4 models
gpt3_model = GPT3Model.from_pretrained('gpt-3')
gpt4_model = GPT4Model.from_pretrained('gpt-4')

# Compare number of parameters between GPT-3 and GPT-4
params_gpt3 = sum(p.numel() for p in gpt3_model.parameters())
params_gpt4 = sum(p.numel() for p in gpt4_model.parameters())

print("Number of parameters in GPT-3:", params_gpt3)
print("Number of parameters in GPT-4:", params_gpt4)
print("Parameter difference:", params_gpt4 - params_gpt3)
