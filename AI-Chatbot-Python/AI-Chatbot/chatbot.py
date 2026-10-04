"""Knowledge-base chatbot engine (no API). TF-IDF style scoring + typo tolerance."""
import math
import re

STOP = set(
    "a an the is are was were be am do does did of to in on at for and or with it its this that "
    "what whats how can could would should please tell me about i you my your we us there any some "
    "much many explain give know want need like".split()
)


def stem(w):
    return re.sub(r"(ing|ed|s)$", "", w) if len(w) > 4 else w


def normalize(text):
    return " ".join(re.findall(r"[a-z0-9]+", text.lower().replace("'", "").replace("’", "")))


def tokens(text):
    return [stem(w) for w in normalize(text).split() if w not in STOP]


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def sim(a, b):
    if a == b:
        return 1.0
    if len(a) < 4 or len(b) < 4:
        return 0.0
    m, e = max(len(a), len(b)), lev(a, b)
    return 1 - e / m if e <= (2 if m >= 7 else 1) else 0.0


class Chatbot:
    def __init__(self, kb, threshold=0.45):
        self.kb, self.threshold = kb, threshold
        self.docs = [sorted(set(tokens(e["t"] + " " + e["k"]))) for e in kb]
        self.phrases = {normalize(p): i for i, e in enumerate(kb) for p in e.get("p", [])}
        df = {}
        for d in self.docs:
            for w in d:
                df[w] = df.get(w, 0) + 1
        self.idf = lambda w: math.log(1 + len(kb) / df.get(w, 1))
        self.starters = ["What is AI?", "Explain machine learning", "What is deep learning?",
                         "What is Big-O?", "Good morning", "Difference between AI, ML and DL"]

    def rank(self, query):
        qt = sorted(set(tokens(query)))
        if not qt:
            return []
        q_tot = sum(max(self.idf(w), 1) for w in qt)
        out = []
        for i, d in enumerate(self.docs):
            m = 0.0
            for w in qt:
                best, bw = 0.0, None
                for x in d:
                    s = sim(w, x)
                    if s > best:
                        best, bw = s, x
                if bw:
                    m += best * self.idf(bw)
            d_tot = sum(self.idf(w) for w in d)
            out.append((i, (m / q_tot) * (0.8 + 0.2 * min(1, m / d_tot))))
        return sorted(out, key=lambda r: -r[1])

    def answer(self, query):
        phrase = self.phrases.get(normalize(query))
        if phrase is not None:
            return self._hit(phrase, 1.0)
        ranked = self.rank(query)
        if ranked and ranked[0][1] >= self.threshold:
            return self._hit(*ranked[0])
        near = ["Tell me about " + self.kb[i]["t"] for i, s in ranked[:3] if s > 0.15]
        return {
            "answer": "I couldn't find a relevant answer in this knowledge base. I cover AI, machine "
                      "learning, deep learning, programming and algorithms. Try one of these topics.",
            "topic": None, "confidence": 0, "suggestions": near or self.starters[:4],
        }

    def _hit(self, i, score):
        e = self.kb[i]
        return {"answer": e["a"], "topic": e["t"],
                "confidence": round(min(1, score) * 100), "suggestions": self.starters}
