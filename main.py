from fastapi import FastAPI  # type: ignore

from chatbot_main import get_answer, CHUNKS  # type: ignore[reportMissingImports]

app = FastAPI(title="Sun Pharma Chatbot API")

@app.get("/")
def home():
    return {"message": "Sun Pharma Chatbot API is running"}

@app.get("/chat")
def chat(q: str):
    answer, score, source = get_answer(q)
    return {
        "question": q,
        "answer": answer,
        "score": round(score, 2),
        "source": source
    }
