

# 📄 Chat With Any PDF

A lightweight Document Question Answering (QA) project that allows users to chat with the contents of any PDF using local LLMs.

This project is intentionally designed without a persistent vector database to demonstrate how document QA systems work at a foundational level before introducing heavier infrastructure.

---

## 🚀 Overview

Chat With Any PDF enables users to:
- Upload a PDF
- Parse and chunk its contents
- Generate embeddings in memory
- Ask natural language questions
- Receive answers grounded in the document

All processing happens locally and ephemerally, making this project ideal for learning, experimentation, and low-overhead deployments.

---

## 🎯 Project Category

Document QA (Pre-Vector DB Architecture)

This repository focuses on core building blocks of document-based AI systems before introducing vector databases, long-term memory, or RAG pipelines.

---

## 🧠 What This Project Demonstrates
📑 Document Processing
- PDF parsing and text extraction
- Handling multi-page and structured documents

✂️ Chunking Strategies
- Fixed-size chunking
- Overlap management
- Context preservation techniques

🔢 Embeddings
- In-memory embedding generation
- Similarity search without persistence
- Trade-offs of ephemeral embeddings

🧩 Prompt Engineering
- Context injection into prompts
- Answer grounding using retrieved chunks
- Reducing hallucinations without a vector DB

🧠 Local LLMs
- Works with:
  - Ollama
  - LM Studio
- No dependency on paid APIs
- Fully offline-capable setup

🔗 LangChain Fundamentals
- Document loaders
- Text splitters
- Chains
- LLM wrappers


---

## ❌ What This Project Explicitly Does NOT Do
To keep the architecture intentionally simple, this project does not include:
- ❌ Persistent vector databases (FAISS, Chroma, Pinecone, etc.)
- ❌ Long-term conversational memory
- ❌ Multi-document or multi-session retrieval
- ❌ Advanced RAG pipelines
- ❌ Production-grade observability or tracing

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