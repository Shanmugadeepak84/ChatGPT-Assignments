import os
from openai import OpenAI

def get_openai_response(messages):
    MODEL = "gpt-3.5-turbo"
    try:
        # read API key from environment variable instead of hard-coding it
        api_key = "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"
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable not set")

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0,
        )

        # --- FIX: use attribute access on the message object ---
        if response.choices:
            return response.choices[0].message.content
        else:
            return None

    except Exception as e:
        # print a helpful error message (avoid printing secrets)
        print(f"Error occurred: {e}")
        return None

def main():
    messages = [
        {"role": "system", "content": "You are an AI research assistant. Use a technical, scientific tone."},
        {"role": "user", "content": "Hello, who are you?"},
        {"role": "assistant", "content": "Greeting! I am an AI research assistant. How can I help you today?"},
        {"role": "user", "content": "Can you explain machine learning in simple terms?"}
    ]

    response_content = get_openai_response(messages)
    if response_content:
        print("Assistant's Response:\n")
        print(response_content)
    else:
        print("Failed to get response from OpenAI.")

if __name__ == "__main__":
    main()
