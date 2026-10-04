# AI-Chatbot

A lightweight, offline knowledge-base chatbot for exploring artificial intelligence and programming topics. Built with Python and Flask, it matches questions against a curated set of answers—no external AI service or API key required.

## Highlights

- **Works offline** — answers come from the project’s built-in knowledge base.
- **Simple chat interface** — a centered dark chat card with colorful accents, conversation history, and a *New chat* control.
- **Flexible question matching** — recognizes key phrases, scores related terms, and tolerates common typos.
- **Easy to extend** — add topics and example phrases directly to the knowledge base.

## Topics

The knowledge base covers:

- Artificial intelligence and its applications
- Machine learning, including supervised and unsupervised learning
- Deep learning and neural networks
- Programming concepts and tools
- Algorithms and data structures
- Greetings and conversational basics

## Requirements

- Python 3.9 or newer
- pip

## Get started

From the project directory, install the dependencies and start the app:

```bash
pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Run the tests

```bash
python -m unittest discover -s tests
```

## How it works

1. The browser sends a message to the Flask endpoint `POST /api/chat`.
2. The chatbot normalizes the question, removes common filler words, and checks configured exact phrases.
3. It scores knowledge-base entries using TF-IDF-style weights and fuzzy matching for likely typos.
4. If the best match meets the 45% threshold, the corresponding answer is returned. Otherwise, the chatbot explains that it could not find a relevant answer and offers related topics.

## Add a knowledge-base entry

Open `knowledge_base.py` and add an entry to the `KB` list:

```python
e(
    "Topic title",
    "keywords people may use",
    "Answer text",
    ["optional exact question"],
)
```

The fourth argument is optional. Answers can include `**bold text**`, `` `inline code` ``, and `\n` line breaks.

## Project structure

| Path | Purpose |
| --- | --- |
| `app.py` | Flask application and chat endpoint |
| `chatbot.py` | Question matching and response selection |
| `knowledge_base.py` | Topics, keywords, and answers |
| `templates/index.html` | Chat page markup |
| `static/style.css` | Responsive chat interface and styling |
| `static/script.js` | Browser-side chat interactions |
| `tests/` | Automated tests |
| `requirements.txt` | Python dependencies |
