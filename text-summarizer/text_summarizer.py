import re
from collections import Counter


# Stop words that don't contribute much to the summary
STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "am", "be", "been", "being", "to", "of", "in",
    "on", "for", "with", "and", "or", "but", "as",
    "at", "by", "from", "this", "that", "it", "its",
    "they", "them", "their", "he", "she", "his", "her",
    "we", "you", "i", "me", "my", "our", "your",
    "do", "does", "did", "has", "have", "had",
    "will", "would", "can", "could", "should",
    "not", "so", "if", "than", "then"
}


# Split text into sentences
def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [sentence for sentence in sentences if sentence]


# Tokenize words
def tokenize(text):
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())


# Count word frequencies
def get_word_frequencies(text):
    words = tokenize(text)

    filtered_words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    return Counter(filtered_words)


# Calculate sentence scores
def score_sentences(sentences, word_frequencies):
    sentence_scores = {}

    for sentence in sentences:

        words = tokenize(sentence)

        score = sum(
            word_frequencies.get(word, 0)
            for word in words
            if word not in STOP_WORDS
        )

        sentence_scores[sentence] = score

    return sentence_scores


# Generate summary
def summarize(text, number_of_sentences=3):

    sentences = split_sentences(text)

    if len(sentences) <= number_of_sentences:
        return sentences

    word_frequencies = get_word_frequencies(text)

    sentence_scores = score_sentences(
        sentences,
        word_frequencies
    )

    # Select the highest-scoring sentences
    ranked_sentences = sorted(
        sentence_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_sentences = ranked_sentences[:number_of_sentences]

    # Keep the original order of the selected sentences
    selected_sentences = [
        sentence for sentence, score in top_sentences
    ]

    summary = [
        sentence for sentence in sentences
        if sentence in selected_sentences
    ]

    return summary


# Main program
print("====================================")
print("          TEXT SUMMARIZER")
print("====================================")
print()

print("Enter your text below.")
print("Press ENTER twice when you are finished.")
print()

lines = []

while True:

    line = input()

    if line == "":
        break

    lines.append(line)


text = " ".join(lines)

if not text.strip():

    print("\nNo text was entered.")

else:

    try:
        number_of_sentences = int(
            input("\nEnter number of summary sentences: ")
        )

        if number_of_sentences <= 0:
            print("Please enter a positive number.")

        else:

            summary = summarize(
                text,
                number_of_sentences
            )

            print("\n====================================")
            print("              SUMMARY")
            print("====================================")

            for sentence in summary:
                print(sentence)

    except ValueError:

        print("Please enter a valid number.")