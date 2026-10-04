import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, bot  # noqa: E402

CASES = [
    # greetings
    ("hello", "Hello"), ("Hi!", "Hello"), ("hey there", "Hello"), ("vanakkam", "Hello"),
    ("good morning", "Good morning"), ("Good Morning!", "Good morning"),
    ("good afternoon", "Good afternoon"), ("good evening", "Good evening"),
    ("good night", "Good night"), ("how are you", "How are you"), ("what's up", "How are you"),
    ("thank you", "Thanks"), ("thanks", "Thanks"), ("bye", "Goodbye"),
    ("who are you", "Who are you"), ("what can you do", "Help"),
    # AI
    ("what is AI", "Artificial Intelligence"), ("what are the types of AI", "Types of AI"),
    ("history of AI", "AI history"), ("what is generative AI", "Generative AI and LLMs"),
    ("what is NLP", "Natural Language Processing"), ("explain computer vision", "Computer Vision"),
    ("difference between AI, ML and DL", "AI vs ML vs DL"), ("AI ethics and bias", "AI ethics and bias"),
    # ML
    ("what is machine learning", "Machine learning"), ("explain machine lerning", "Machine learning"),
    ("what is supervised learning", "Supervised learning"), ("unsupervised learning", "Unsupervised learning"),
    ("what is reinforcement learning", "Reinforcement learning"), ("what is overfitting", "Overfitting and underfitting"),
    ("what is precision and recall", "Evaluation metrics"), ("random forest", "Decision tree and random forest"),
    ("what is KNN", "K-Nearest Neighbors"), ("what is regression", "Regression"),
    # DL
    ("what is deep learning", "Deep learning"), ("what is a neural network", "Neural network"),
    ("explain CNN", "CNN"), ("what is LSTM", "RNN and LSTM"), ("what is a transformer", "Transformer"),
    ("what is gradient descent", "Gradient descent and backpropagation"),
    ("pytorch vs tensorflow", "TensorFlow and PyTorch"),
    # programming
    ("what is python", "Python"), ("what is pyton", "Python"), ("what is OOP", "Object-oriented programming"),
    ("what is an API", "API"), ("what is git", "Git and GitHub"), ("what is SQL", "SQL and databases"),
    ("how to learn programming", "Learn programming"), ("how to debug", "Debugging"),
    # algorithms
    ("what is an algorithm", "Algorithm"), ("what is big o", "Big-O notation"),
    ("sorting algorithms", "Sorting algorithms"), ("what is binary search", "Searching algorithms"),
    ("what is recursion", "Recursion"), ("dynamic programming", "Dynamic programming"),
    ("what is BFS and DFS", "Graph algorithms"),
]
UNKNOWN = ["what is the capital of france", "tell me a joke", "asdfgh", "best pizza recipe", "football score"]


class EngineTests(unittest.TestCase):
    def test_known_questions(self):
        for q, topic in CASES:
            with self.subTest(q=q):
                self.assertEqual(bot.answer(q)["topic"], topic)

    def test_unknown_questions_fall_back(self):
        for q in UNKNOWN:
            with self.subTest(q=q):
                r = bot.answer(q)
                self.assertIsNone(r["topic"])
                self.assertTrue(r["suggestions"])

    def test_every_entry_reachable_by_its_title(self):
        for e in bot.kb:
            with self.subTest(t=e["t"]):
                self.assertEqual(bot.answer(e["t"])["topic"], e["t"])


class FlaskTests(unittest.TestCase):
    def setUp(self):
        self.c = app.test_client()

    def test_home_page(self):
        r = self.c.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"AI-Chatbot", r.data)

    def test_chat_ok(self):
        r = self.c.post("/api/chat", json={"message": "good morning"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["topic"], "Good morning")

    def test_chat_empty_and_bad_json(self):
        self.assertEqual(self.c.post("/api/chat", json={"message": "  "}).status_code, 400)
        self.assertEqual(self.c.post("/api/chat", data="nope").status_code, 400)

    def test_static_files(self):
        for f in ("style.css", "script.js"):
            self.assertEqual(self.c.get("/static/" + f).status_code, 200)


if __name__ == "__main__":
    unittest.main(verbosity=1)
