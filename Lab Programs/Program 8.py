"""
Program 8: Implement a simple stochastic part-of-speech tagging algorithm
using a basic probabilistic (bigram HMM-style) model to assign POS tags.
"""

from collections import defaultdict


# A small manually tagged training corpus (word, tag) sequences
training_data = [
    [("the", "DET"), ("dog", "NOUN"), ("runs", "VERB")],
    [("the", "DET"), ("cat", "NOUN"), ("sleeps", "VERB")],
    [("a", "DET"), ("dog", "NOUN"), ("barks", "VERB")],
    [("the", "DET"), ("cat", "NOUN"), ("runs", "VERB")],
    [("a", "DET"), ("cat", "NOUN"), ("sleeps", "VERB")],
]


def train_model(data):
    # emission counts: P(word | tag)
    emission_counts = defaultdict(lambda: defaultdict(int))
    # transition counts: P(tag_i | tag_i-1)
    transition_counts = defaultdict(lambda: defaultdict(int))
    tag_counts = defaultdict(int)

    for sentence in data:
        prev_tag = "<s>"
        for word, tag in sentence:
            emission_counts[tag][word] += 1
            transition_counts[prev_tag][tag] += 1
            tag_counts[tag] += 1
            prev_tag = tag

    return emission_counts, transition_counts, tag_counts


def emission_prob(word, tag, emission_counts, tag_counts):
    count_word_tag = emission_counts[tag].get(word, 0)
    total_tag = tag_counts[tag]
    # simple add-one smoothing
    return (count_word_tag + 1) / (total_tag + len(emission_counts[tag]) + 1)


def transition_prob(tag, prev_tag, transition_counts, tag_counts):
    count = transition_counts[prev_tag].get(tag, 0)
    total = sum(transition_counts[prev_tag].values())
    return (count + 1) / (total + len(tag_counts) + 1)


def stochastic_tag(sentence, emission_counts, transition_counts, tag_counts):
    tags = list(tag_counts.keys())
    result = []
    prev_tag = "<s>"

    for word in sentence:
        best_tag = None
        best_score = -1
        for tag in tags:
            e = emission_prob(word, tag, emission_counts, tag_counts)
            t = transition_prob(tag, prev_tag, transition_counts, tag_counts)
            score = e * t
            if score > best_score:
                best_score = score
                best_tag = tag
        result.append((word, best_tag))
        prev_tag = best_tag

    return result


def main():
    emission_counts, transition_counts, tag_counts = train_model(training_data)

    test_sentence = ["the", "cat", "barks"]
    tagged_result = stochastic_tag(test_sentence, emission_counts, transition_counts, tag_counts)

    print("Training data (word/tag pairs):")
    for s in training_data:
        print(" ", s)

    print("\nTest sentence:", test_sentence)
    print("Stochastic POS tagging result:")
    for word, tag in tagged_result:
        print(f"  {word:<10} -> {tag}")


if __name__ == "__main__":
    main()
