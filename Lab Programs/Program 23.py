"""
Program 23: Evaluate the coherence of a given text using sentence-level
similarity (TF-IDF + cosine similarity between consecutive sentences).
"""

import nltk

for pkg in ["punkt", "punkt_tab"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compute_coherence(text):
    sentences = sent_tokenize(text)

    if len(sentences) < 2:
        print("Text needs at least 2 sentences to evaluate coherence.")
        return

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(sentences)

    similarities = []
    print("Sentence-to-sentence coherence scores:")
    for i in range(len(sentences) - 1):
        sim = cosine_similarity(tfidf_matrix[i], tfidf_matrix[i + 1])[0][0]
        similarities.append(sim)
        print(f"  S{i+1} -> S{i+2}: {sim:.4f}")
        print(f"    S{i+1}: {sentences[i]}")
        print(f"    S{i+2}: {sentences[i+1]}")

    avg_coherence = np.mean(similarities)
    print(f"\nAverage coherence score: {avg_coherence:.4f}")

    if avg_coherence > 0.3:
        verdict = "The text is fairly coherent."
    elif avg_coherence > 0.1:
        verdict = "The text has moderate coherence."
    else:
        verdict = "The text has low coherence (topics may be disjointed)."
    print("Verdict:", verdict)

    return avg_coherence


def main():
    coherent_text = (
        "Climate change is a major global challenge. It affects weather "
        "patterns around the world. Rising temperatures lead to melting "
        "ice caps. This causes sea levels to rise significantly."
    )

    incoherent_text = (
        "Climate change is a major global challenge. My favorite food is "
        "pizza with extra cheese. The stock market fluctuated yesterday. "
        "Basketball is a popular sport in America."
    )

    print("=== Evaluating Coherent Text ===")
    compute_coherence(coherent_text)

    print("\n=== Evaluating Less Coherent Text ===")
    compute_coherence(incoherent_text)


if __name__ == "__main__":
    main()
