💊 Sun Pharma Chatbot

A smart, retrieval-based chatbot that answers questions about Sun Pharma using only the provided company data. No hallucination - if information is not in the data, it clearly says so.

Built with Python, TF-IDF + Cosine Similarity, and Streamlit.

---

✨ Features

- **Accurate Answers:** Answers only from `data/` files
- **No Hallucination:** If data not found, returns: `Sorry, I could not find this information in the provided data.`
- **Short & Clean Answers:** Shows only first 4 sentences, not full paragraphs
- **Source + Score:** Every answer shows its source file and confidence score
- **Simple UI:** Clean chat interface built with Streamlit

---

🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** - Web UI
- **Scikit-learn** - TF-IDF Vectorizer + Cosine Similarity
- **NumPy / Pandas**

---

📁 Project Structure

Sun-Pharma-Chatbot/
├── http://app.py                  # Streamlit UI
├── chatbot_main.py         # Core logic - search + answer
├── http://requirements.txt        # Dependencies
├── http://README.md
└── data/
    ├── about_us.txt
    ├── http://careers.txt
    ├── http://products.txt
    └── http://news.txt

---

🚀 How to Run

1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/Sun-Pharma-Chatbot.git
cd Sun-Pharma-Chatbot
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
Open in browser: `http://localhost:8501`

---

🧠 How It Works

1. User types a question, e.g. `what is sun pharma`
2. Question is converted to TF-IDF vector
3. Cosine Similarity is calculated with all chunks in `data/` files
4. Best matching chunk is selected
5. *If Score > 0.50* → Show short answer (first 4 sentences)
6. *If Score <= 0.50* → Show `Sorry, I could not find this information...`

This threshold prevents the bot from guessing wrong answers.

---

💬 Example
Question	Answer
`what is sun pharma`	Sun Pharma is a leading global specialty generic company... `Source: about_us.txt \| Score: 1.00`
`current opening`	Careers \| Work with Us - Sun Pharmaceutical... `Source: careers.txt \| Score: 1.00`
`who is founder`	Sorry, I could not find this information in the provided data. `Source: No Source \| Score: 0.00`
---

🔮 Future Improvements

- [ ] Add PDF / Website scraping
- [ ] Use Sentence Embeddings instead of TF-IDF
- [ ] Add Chat History
- [ ] Deploy on Streamlit Cloud

---

👨‍💻 Author
Dr. Monika Shekhawat

Made  as a RAG Chatbot Mini-Project