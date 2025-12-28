

# 📄 Chat with Your PDFs Using Local RAG

This project demonstrates how to build a Retrieval-Augmented Generation (RAG)–powered PDF Question Answering system using LangChain, FAISS, Hugging Face embeddings, and a locally hosted LLM served via Ollama/LM Studio.

The application ingests PDF documents, splits them into semantically meaningful chunks, converts them into vector embeddings, and stores them in a FAISS vector database. When a user asks a question, the system retrieves the most relevant content and generates grounded answers using a local language model—without relying on any external APIs.

---

## 🚀 Features

- Load and process PDF documents  
- Split text into optimized, overlapping chunks
- Generate embeddings using Hugging Face sentence transformers
- Store and search vectors efficiently with FAISS
- Retrieve relevant document context  
- Interactive question answering via CLI 
- Fully local execution using a local LLM (no OpenAI API required)

---

## 🧠 Architecture Overview

PDF → Text Chunks → Embeddings → FAISS Vector Store
                         ↓
                   Retriever (Top-K)
                         ↓
                  Prompt + Local LLM
                         ↓
                     Answer

#### This architecture ensures:

- Reduced hallucinations
- Answers grounded in source documents
- Scalability to large PDFs
- Offline and privacy-preserving operation

--- 

## 🖥️ Local LLM Setup 

### Ollama

1. Install **Ollama**
2. Download a supported chat model  
   *(e.g., Gemma 3, LLaMA 3, Mistral, Phi-3)*
   ```bash
   ollama pull gemma3:1b
   ```

3. Start the local server:
   
   Ollama runs automatically when a model is invoked.

### LM Studio

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