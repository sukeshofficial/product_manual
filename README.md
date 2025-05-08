# 🛠️ Product Manual Assistant

**Product Manual Assistant** is an AI-powered assistant that helps users quickly find answers from electronic or gadget product manuals using natural language queries. Built using **Retrieval-Augmented Generation (RAG)**, it leverages **Qdrant** for vector search and **Streamlit** for a user-friendly interface.

---

## 🚀 Features

- 🔍 **Natural Language Querying**: Ask questions like “How do I reset this device?” or “What is the warranty period?”
- 📚 **Manual Upload Support**: Upload product manuals (PDF or text) to index.
- ⚡ **Fast Retrieval**: Uses Qdrant vector database for efficient semantic search.
- 🧠 **Contextual Answering**: Combines retrieved chunks with an LLM to generate accurate, human-like responses.
- 🌐 **Web Interface**: Simple and intuitive Streamlit-based frontend.

---

## 📂 Project Structure

```
product-manual-assistant/
│
├── app.py                # Main Streamlit app
├── rag_pipeline.py       # Handles embedding, storage, and retrieval
├── utils.py              # Helper functions for PDF/text extraction
├── qdrant_client.py      # Qdrant connection & vector DB logic
├── requirements.txt      # Python dependencies
└── README.md             # You're reading it!
```

---

## ⚙️ How It Works

1. **Upload** a product manual (PDF or plain text).
2. The file is split into chunks and embedded using a language model.
3. Embeddings are stored in **Qdrant**, a vector search engine.
4. When a user enters a question, relevant chunks are retrieved via semantic search.
5. Retrieved context + user query are passed to an LLM (e.g., OpenRouter or OpenAI) to generate a final response.

---

## 🧑‍💻 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **RAG Backend**: Custom Python pipeline
- **Vector Store**: [Qdrant](https://qdrant.tech/)
- **Embeddings & LLM**: OpenRouter / Hugging Face / OpenAI APIs

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/product-manual-assistant.git
cd product-manual-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file for API keys and configuration:

```bash
OPENROUTER_API_KEY=your_key_here
QDRANT_HOST=http://localhost:6333
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📸 Screenshots

*(Add screenshots of the app interface here to give users a quick preview.)*

---

## ✅ TODO

- [ ] Add user authentication
- [ ] Support batch uploads
- [ ] Add feedback mechanism for answers
- [ ] Dockerize the app

---

## 📄 License

MIT License. Feel free to use, modify, and share.

---

## 🙌 Acknowledgements

- [Qdrant](https://qdrant.tech/)
- [Streamlit](https://streamlit.io/)
- [OpenRouter](https://openrouter.ai/)
- [LangChain](https://www.langchain.com/) (if used)