import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_openai_response(messages):
    MODEL = "gpt-3.5-turbo"

    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message['content'] if response.choices else None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def main():
    messages = [
        {"role": "system", "content": "You are an AI research assistant. You use a tone that is technical and scientific."},
        {"role": "user", "content": "Hello, who are you?"},
        {"role": "assistant", "content": "Greeting! I am an AI research assistant. How can I help you today?"},
        {"role": "user", "content": "Can you explain machine learning in simple terms?"}
    ]

    response_content = get_openai_response(messages)
    if response_content:
        print(f"Assistant's Response: {response_content}")
    else:
        print("Failed to get response from OpenAI.")

if __name__ == "__main__":
    main()
