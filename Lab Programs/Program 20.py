"""
Program 20: Implement a basic Information Retrieval system using
TF-IDF (Term Frequency-Inverse Document Frequency) for document ranking.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    "The cat sat on the mat and looked outside the window",
    "Dogs are loyal animals and are considered man's best friend",
    "Natural language processing helps computers understand human language",
    "Cats and dogs are common household pets around the world",
    "Machine learning is a subset of artificial intelligence",
]


def search(query, documents, top_n=3):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

    ranked_indices = scores.argsort()[::-1][:top_n]

    print(f"\nQuery: '{query}'")
    print("Ranked results (by relevance):")
    for rank, idx in enumerate(ranked_indices, start=1):
        print(f"  {rank}. (score={scores[idx]:.4f}) {documents[idx]}")

    return vectorizer, tfidf_matrix


def show_tfidf_matrix(vectorizer, tfidf_matrix):
    feature_names = vectorizer.get_feature_names_out()
    print("\nSample TF-IDF matrix (first document):")
    dense = tfidf_matrix.todense()
    row = dense[0].tolist()[0]
    nonzero_terms = [(feature_names[i], round(val, 3)) for i, val in enumerate(row) if val > 0]
    print(sorted(nonzero_terms, key=lambda x: -x[1]))


def main():
    print("Document collection:")
    for i, doc in enumerate(documents, start=1):
        print(f"  D{i}: {doc}")

    vectorizer, tfidf_matrix = search("dogs and cats as pets", documents)
    show_tfidf_matrix(vectorizer, tfidf_matrix)

    search("computers understanding language", documents)


if __name__ == "__main__":
    main()
