import os
import re
from collections import Counter


# Common words that should be ignored
STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "be", "been", "being", "to", "of", "in", "on",
    "for", "with", "and", "or", "but", "as", "at",
    "by", "from", "this", "that", "it", "its",
    "they", "them", "their", "he", "she", "his",
    "her", "we", "you", "i", "me", "my", "our",
    "your", "what", "which", "who", "where", "when",
    "how", "why", "do", "does", "did", "can",
    "could", "would", "should"
}


# Load document
def load_document(filename):
    try:
        # Get the folder where this Python file is located
        project_folder = os.path.dirname(os.path.abspath(__file__))

        # Create the complete path to the document
        file_path = os.path.join(project_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Error: document.txt not found.")
        print("Make sure document.txt is in the same folder as qa_bot.py.")
        return ""


# Split document into sections
def split_sections(document):
    sections = re.split(r'\n\s*\n', document.strip())

    return [
        section.strip()
        for section in sections
        if section.strip()
    ]


# Extract keywords from text
def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]


# Build keyword index
def build_keyword_index(sections):
    index = {}

    for section_number, section in enumerate(sections):

        keywords = extract_keywords(section)

        for keyword in keywords:

            if keyword not in index:
                index[keyword] = []

            if section_number not in index[keyword]:
                index[keyword].append(section_number)

    return index


# Find the section that best matches the question
def find_best_answer(question, sections, keyword_index):

    question_keywords = extract_keywords(question)

    if not question_keywords:
        return None, 0

    scores = Counter()

    # Count matching keywords for every section
    for keyword in question_keywords:

        if keyword in keyword_index:

            for section_number in keyword_index[keyword]:
                scores[section_number] += 1

    if not scores:
        return None, 0

    # Get the section with the highest score
    best_section_number, best_score = scores.most_common(1)[0]

    return sections[best_section_number], best_score


# Main program
def main():

    print("====================================")
    print("              Q&A BOT")
    print("====================================")
    print()

    print("Loading document...")

    document = load_document("document.txt")

    if not document:
        return

    # Split document into sections
    sections = split_sections(document)

    # Build keyword index
    keyword_index = build_keyword_index(sections)

    print(f"Loaded {len(sections)} sections.")
    print()
    print("Ask questions about the document.")
    print("Type 'quit' or 'exit' to stop.")
    print()

    while True:

        question = input("You: ").strip()

        # Quit command
        if question.lower() in ["quit", "exit"]:
            print("Bot: Goodbye!")
            break

        # Empty question
        if not question:
            print("Bot: Please enter a question.")
            print()
            continue

        # Find best matching section
        answer, score = find_best_answer(
            question,
            sections,
            keyword_index
        )

        if answer:

            print()
            print("Bot:")
            print(answer)
            print()
            print(f"Keyword matches: {score}")

        else:

            print()
            print(
                "Bot: Sorry, I couldn't find relevant "
                "information in the document."
            )

        print()


# Run the program
if __name__ == "__main__":
    main()