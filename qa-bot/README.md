# Q&A Bot

A simple **document-based Question & Answer bot built with Python**. The bot reads a text document, divides it into sections, creates a keyword index, and answers user questions by finding the section with the most matching keywords.

## Features

* Loads information from a text document
* Splits the document into separate sections
* Extracts keywords from each section
* Builds a keyword index
* Matches user questions against document sections
* Returns the section with the highest number of matching keywords
* Ignores common stop words
* Displays the number of matching keywords
* Supports `quit` and `exit` commands
* Handles missing documents and empty questions

## Technologies Used

* **Python 3**
* Regular Expressions (`re`)
* `collections.Counter`
* File Handling
* Keyword Matching

## How It Works

The Q&A bot follows these steps:

```text
Document
    ↓
Load Document
    ↓
Split into Sections
    ↓
Extract Keywords
    ↓
Build Keyword Index
    ↓
User Question
    ↓
Extract Question Keywords
    ↓
Compare Keywords
    ↓
Find Best Matching Section
    ↓
Return Answer
```

## Example Document

The included `document.txt` contains information about:

* Python
* Artificial Intelligence
* Machine Learning
* OpenCV
* GitHub

## Example

### Question

```text
You: What is Python?
```

### Response

```text
Bot:
Python

Python is a high-level, interpreted programming language known
for its simple and readable syntax. It was created by Guido van
Rossum and first released in 1991. Python is widely used in web
development, data science, artificial intelligence, automation,
and software development.

Keyword matches: 1
```

Another example:

```text
You: What is OpenCV used for?
```

The bot identifies the **OpenCV** section because it contains several keywords related to the question.

## How to Run

Make sure Python 3 is installed.

Navigate to the project directory:

```bash
cd qa-bot
```

Run the program:

```bash
python qa_bot.py
```

The program will automatically locate `document.txt` from the same directory as `qa_bot.py`.

## Usage

After starting the program, enter questions related to the document:

```text
You: What is machine learning?

You: What is GitHub?

You: What is OpenCV used for?
```

To exit:

```text
You: quit
```

or:

```text
You: exit
```

## Project Structure

```text
qa-bot/
│
├── qa_bot.py
├── document.txt
└── README.md
```

### Files

| File           | Description                        |
| -------------- | ---------------------------------- |
| `qa_bot.py`    | Main Q&A bot program               |
| `document.txt` | Knowledge document used by the bot |
| `README.md`    | Project documentation              |

## Keyword Matching

The bot extracts meaningful words from both the document and the user's question.

Common words such as:

```text
the
is
a
and
of
to
what
how
```

are ignored using a stop-word list.

The remaining keywords are compared with the document's keyword index. The section containing the most matching keywords is returned as the answer.

## Learning Objectives

This project demonstrates:

* File handling in Python
* Text processing
* Regular expressions
* Keyword extraction
* Dictionary-based indexing
* Frequency counting
* Basic information retrieval
* Question and answer systems
* Natural language processing fundamentals

## Limitations

This is a **keyword-based Q&A system**, not a generative AI chatbot. It can only answer questions using information available in `document.txt`, and its accuracy depends on the keywords used in the question and document.

## Author

**Kaivalya**
