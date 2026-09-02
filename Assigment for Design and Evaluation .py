"""
End-to-End Sentiment Analysis Pipeline (NLTK)
Compares a Rule-Based lexicon classifier with a Naive Bayes classifier
on the NLTK movie_reviews corpus.
"""
import re, random
import nltk
from nltk.corpus import movie_reviews,stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.classify import NaiveBayesClassifier, accuracy as nltk_accuracy
from nltk.probability import FreqDist
 
nltk.download(['movie_reviews','punkt','punkt_tab',
                'stopwords','averaged_perceptron_tagger'], quiet=True)
 
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
 
POSITIVE_WORDS = {'good','great','excellent','love','best','amaz',
                   'wonder','enjoy','fantast','perfect','brilliant'}
NEGATIVE_WORDS = {'bad','worst','hate','poor','terribl','wast',
                   'bore','aw','disappoint','dull','fail'}
 
def normalise(text):
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'http\\S+', ' ', text)
    text = re.sub(r'[^a-zA-Z\\s]', ' ', text)
    return text.lower()
 
def preprocess(text):
    tokens = word_tokenize(normalise(text))
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]
    return [stemmer.stem(t) for t in tokens]
 
def rule_based_predict(tokens):
    score = sum(1 for t in tokens if t in POSITIVE_WORDS)
    score -= sum(1 for t in tokens if t in NEGATIVE_WORDS)
    return 'pos' if score >= 0 else 'neg'
 
def extract_features(tokens, top_words):
    word_set = set(tokens)
    return {f'contains({w})': (w in word_set) for w in top_words}
 
def main():
    docs = [(preprocess(' '.join(movie_reviews.words(fileid))), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
    random.seed(42)
    random.shuffle(docs)
    split = int(0.8 * len(docs))
    train_docs, test_docs = docs[:split], docs[split:]
 
    all_words = FreqDist(w for tokens, _ in train_docs for w in tokens)
    top_words = [w for w, _ in all_words.most_common(2000)]
 
    train_features = [(extract_features(t, top_words), c) for t, c in train_docs]
    test_features  = [(extract_features(t, top_words), c) for t, c in test_docs]
    nb_classifier = NaiveBayesClassifier.train(train_features)
 
    nb_correct = sum(1 for (feat, gold) in test_features
                     if nb_classifier.classify(feat) == gold)
    rb_correct = sum(1 for (tokens, gold) in test_docs
                     if rule_based_predict(tokens) == gold)
 
    print(f'Naive Bayes accuracy : {nb_correct/len(test_docs):.3f}')
    print(f'Rule-based accuracy  : {rb_correct/len(test_docs):.3f}')
    nb_classifier.show_most_informative_features(10)
 
    demo_reviews = [
        'An absolutely wonderful film with a brilliant lead performance.',
        'This was a terrible waste of time, I hated every minute.',
    ]
    for review in demo_reviews:
        tokens = preprocess(review)
        feats = extract_features(tokens, top_words)
        print(review, '->',
              'NB:', nb_classifier.classify(feats),
              '| Rule:', rule_based_predict(tokens))
 
if __name__ == '__main__':
    main()
