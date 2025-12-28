

# 📄 PDF Question Answering with LangChain (Local LLM)

This project demonstrates how to build a **PDF-based Question Answering (QA) system** using **LangChain**, **FAISS**, **Hugging Face embeddings**, and a **local LLM served via LM Studio**.

The application loads a PDF, splits it into chunks, stores embeddings in a vector database, retrieves relevant content for a user query, and generates answers using a locally hosted language model.

---

## 🚀 Features

- Load and process PDF documents  
- Chunk and embed text using sentence transformers  
- Store and search embeddings with FAISS  
- Retrieve relevant document context  
- Ask questions interactively via CLI  
- Use a **local LLM** (no OpenAI API required)

---

## 🧠 Architecture Overview

PDF → Text Chunks → Embeddings → FAISS Vector Store
                         ↓
                   Retriever (Top-K)
                         ↓
                  Prompt + Local LLM
                         ↓
                     Answer

--- 

## 🖥️ Local LLM Setup (LM Studio)

1. Install **LM Studio**
2. Download a supported chat model  
   *(e.g., Mistral, LLaMA, Phi)*
3. Start the local server:
   - **API Base URL:** `http://localhost:1234/v1`

> ⚠️ **Note:**  
> The application uses `ChatOpenAI` **only as a compatible client interface** for LM Studio.  
> It does **not** connect to OpenAI’s hosted API.


---

## ▶️ How to Run

Follow the steps below to set up and run the application locally.

#### Create Virtual Environment
```bash
uv venv
```

#### Activate Virtual Environment
```bash
source .venv/bin/activate
```

#### Install Dependencies
```bash
uv add -r requirements.txt
```

#### Run the Application
```bash
python main.py
```

---