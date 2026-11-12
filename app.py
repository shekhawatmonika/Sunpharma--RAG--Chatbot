import sys
from pathlib import Path

import streamlit as st  # type: ignore[reportMissingImports]

# Add the project directory's parent so Python can resolve the `chatbot` package.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from chatbot_main import get_answer, CHUNKS  # type: ignore[reportMissingImports]

st.set_page_config(page_title="Sun Pharma Chatbot", page_icon="💊")
st.title("💊 Sun Pharma Chatbot")
st.write("Ask anything about Sun Pharma - products, careers, news, licensing and more.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Type your question here... e.g. current opening")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    answer, score, source = get_answer(question)
    reply = f"{answer}\n\n*Source: {source} | Score: {score:.2f}*"
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

with st.sidebar:
    st.header("About")
    st.write("This chatbot answers only from the provided Sun Pharma data files.")
    st.write(f"Total chunks loaded: {len(CHUNKS)}")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()