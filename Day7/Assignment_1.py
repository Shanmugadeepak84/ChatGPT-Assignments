import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Check current rate limit usage
usage = openai.Usage.retrieve()
print("Current Rate Limit Usage:\n", usage)
