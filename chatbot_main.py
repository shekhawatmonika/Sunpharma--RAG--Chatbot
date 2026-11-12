from ntpath import join
import os
import re

DATA_FOLDER = "data"

def normalize_spelling(word):
    word = word.replace("licencing", "licensing")
    word = word.replace("licence", "license")
    word = word.replace("licenc", "licens")
    return word

def stem(word):
    word = normalize_spelling(word.lower())
    if word.endswith("ings"):
        word = word[:-4]
    elif word.endswith("ing"):
        word = word[:-3]
    elif word.endswith("ies"):
        word = word[:-3] + "y"
    elif word.endswith("es"):
        word = word[:-2]
    elif word.endswith("s") and len(word) > 3:
        word = word[:-1]
    elif word.endswith("ed"):
        word = word[:-2]
    return word

SYNONYMS = {
    "founder": ["founder", "founded", "established", "started", "creator"],
    "headquarter": ["headquarter", "headquarters", "head", "office", "located", "based"],
    "licensing": ["licensing", "licencing", "license", "licence", "agreement"],
    "license": ["licensing", "licencing", "license", "licence", "agreement"],
    "product": ["product", "products", "medicine", "medicines", "drug", "drugs", "brand"],
    "medicine": ["product", "products", "medicine", "medicines", "drug", "drugs"],
    "opening": ["opening", "openings", "vacancy", "vacancies", "job", "jobs", "hiring", "career"],
    "career": ["opening", "openings", "vacancy", "job", "jobs", "career", "careers"],
}

def expand_query(tokens):
    expanded = set(tokens)
    for t in tokens:
        if t in SYNONYMS:
            expanded.update(SYNONYMS[t])
    return expanded

def tokenize(text):
    words = re.findall(r"[a-z]+", text.lower())
    return [stem(w) for w in words]

def load_chunks():
    chunks = []
    if not os.path.exists(DATA_FOLDER):
        return chunks
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(DATA_FOLDER, filename)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            parts = re.split(r"\n\s*\n", text)
            for part in parts:
                part = part.strip()
                if len(part) > 30:
                    chunks.append({"text": part, "source": filename})
    return chunks

CHUNKS = load_chunks()

def get_answer(question):
    query_tokens = set(tokenize(question))
    query_tokens = expand_query(query_tokens)
    best_score = 0
    best_chunk = None
    for chunk in CHUNKS:
        chunk_tokens = set(tokenize(chunk["text"]))
        if not chunk_tokens:
            continue
        common = query_tokens.intersection(chunk_tokens)
        score = len(common) / max(len(query_tokens), 1)
        if score > best_score:
            best_score = score
            best_chunk = chunk
    if best_chunk and best_score > 0.50:
        text = best_chunk["text"]
        sentences=text.split(". ")
        short_answer = ".".join(sentences[:2]) + "." if len(sentences) > 1 else sentences[0]


        return short_answer, best_score, best_chunk["source"]
    return "Sorry, I could not find this information in the provided data.", 0.0, "No Source"
