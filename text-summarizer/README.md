# Text Summarizer

A simple **text summarization tool built with Python** that identifies important sentences based on **word frequency** and generates a concise summary from the input text.

## Features

* Accepts multi-line text input
* Splits text into individual sentences
* Tokenizes text into individual words
* Calculates word frequencies
* Filters common stop words
* Scores sentences based on important word frequency
* Returns the top `N` highest-scoring sentences
* Preserves the original order of selected sentences
* Handles invalid input and empty text

## Technologies Used

* **Python 3**
* `re` module for text processing
* `collections.Counter` for word-frequency calculation

## How It Works

The summarizer follows these steps:

```text
Input Text
    ↓
Split Text into Sentences
    ↓
Tokenize Words
    ↓
Remove Common Stop Words
    ↓
Count Word Frequencies
    ↓
Score Each Sentence
    ↓
Select Top N Sentences
    ↓
Generate Summary
```

### Sentence Scoring

Each sentence receives a score based on the frequency of its meaningful words.

For example:

```text
artificial → 4
intelligence → 4
technology → 2
learning → 1
```

A sentence containing frequently occurring words receives a higher score and is considered more important.

## Example

### Input

```text
Artificial intelligence is transforming modern technology.
Artificial intelligence is being used in healthcare.
Technology companies are investing heavily in artificial intelligence.
Machine learning is an important part of artificial intelligence.
```

### Output

```text
SUMMARY

Artificial intelligence is transforming modern technology.
Technology companies are investing heavily in artificial intelligence.
```

The exact output depends on the word frequencies in the provided text and the requested number of summary sentences.

## How to Run

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project:

```bash
cd text-summarizer
```

Run the program:

```bash
python text_summarizer.py
```

Enter the text when prompted.

Press **Enter twice** after finishing the text, then specify the number of sentences you want in the summary.

Example:

```text
Enter number of summary sentences: 3
```

## Project Structure

```text
text-summarizer/
│
├── text_summarizer.py
└── README.md
```

## Learning Objectives

This project demonstrates:

* Natural language text processing
* Sentence splitting
* Word tokenization
* Frequency analysis
* Stop-word filtering
* Sentence scoring
* Basic extractive text summarization
* Python dictionaries and `Counter`
* Regular expressions

## Type of Summarization

This project uses **extractive summarization**.

Instead of generating new sentences, it selects important sentences directly from the original text based on their word-frequency scores.

## Author

**Kaivalya**