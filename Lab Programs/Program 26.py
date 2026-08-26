"""
Program 26: Implement a machine translation program using the
Hugging Face Transformers library to translate English text to French.

Install requirement:
    pip install transformers sentencepiece torch
"""

from transformers import MarianMTModel, MarianTokenizer


def translate_en_to_fr(texts):
    model_name = "Helsinki-NLP/opus-mt-en-fr"

    print(f"Loading model '{model_name}' (this may take a moment on first run)...")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the input text batch
    encoded = tokenizer(texts, return_tensors="pt", padding=True)

    # Generate translation
    translated_tokens = model.generate(**encoded)

    # Decode the generated tokens back to text
    translated_texts = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]

    return translated_texts


def main():
    english_sentences = [
        "Hello, how are you today?",
        "Natural language processing is a fascinating field.",
        "I would like to learn French.",
        "The weather is very nice today.",
    ]

    translations = translate_en_to_fr(english_sentences)

    print("\nTranslation Results (English -> French):")
    print("-" * 55)
    for en, fr in zip(english_sentences, translations):
        print(f"EN: {en}")
        print(f"FR: {fr}\n")


if __name__ == "__main__":
    main()
