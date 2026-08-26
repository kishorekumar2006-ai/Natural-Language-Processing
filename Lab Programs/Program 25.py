"""
Program 25: Utilize the GPT-3 model (via OpenAI API) to generate text
based on a given prompt.

Install requirement:
    pip install openai

Before running, set your API key as an environment variable:
    export OPENAI_API_KEY="your-api-key-here"      (Linux / Mac)
    setx OPENAI_API_KEY "your-api-key-here"         (Windows)

Note: This program requires a valid OpenAI API key and network access.
The OpenAI Python SDK syntax below uses the modern client-based API
(openai>=1.0.0). If you are using an older SDK version, refer to the
legacy `openai.Completion.create(...)` interface instead.
"""

import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def generate_text(prompt, max_tokens=100):
    if OpenAI is None:
        print("The 'openai' library is not installed. Run: pip install openai")
        return None

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set.")
        print("Set it before running this program to use the GPT-3 API.")
        return None

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-instruct",  # GPT-3 style completion model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"API call failed: {e}")
        return None


def main():
    prompt = "Write a short paragraph explaining Natural Language Processing to a beginner."

    print("Prompt:", prompt)
    result = generate_text(prompt)

    if result:
        print("\nGenerated text:\n", result)
    else:
        print("\nNo output generated. Please check your API key and network connection.")


if __name__ == "__main__":
    main()
