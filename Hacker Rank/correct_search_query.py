import re
from collections import Counter

# Sample inline dictionary corpus (expand for better accuracy)
corpus = """china going to india president was winner match food america
first of the and is are be have had who what where
"""
WORDS = Counter(corpus.split())

def words_from_text(text):
    return re.findall(r'\w+', text.lower())

def known(words):
    return set(w for w in words if w in WORDS)

def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def candidates(word):
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]

def correct_word(word):
    return max(candidates(word), key=WORDS.get, default=word)

def correct_query(query):
    words = query.split()
    corrected = [correct_word(word) for word in words]
    return ' '.join(corrected)

if __name__ == "__main__":
    n = int(input().strip())
    queries = [input().strip() for _ in range(n)]

    for query in queries:
        print(correct_query(query))
