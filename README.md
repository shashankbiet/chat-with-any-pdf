

# 📄 Chat With Any PDF

A local-first Document Question Answering (QA) system that lets users chat with the contents of any PDF using **in-memory vector search** and **local LLMs**.

This project is intentionally designed to demonstrate **RAG fundamentals without persistent or external vector databases**.

---

## 🚀 Overview

Chat With Any PDF enables users to upload a PDF, ask natural language questions, and receive answers grounded strictly in the document content.

The goal of this project is **educational**: to help engineers understand how document QA systems work end-to-end *before* introducing persistent vector databases, production infrastructure, or advanced agentic workflows.

All computation happens **locally and ephemerally**, making this setup:
- Privacy-preserving
- Offline-capable
- Lightweight and easy to reason about

---

## 🎯 Project Category

Document QA with Ephemeral Vector Search

This repository represents the foundational layer of Retrieval-Augmented Generation (RAG), using an **in-memory vector index recreated on every run**.

---

## 🧠 What This Project Demonstrates

### 📑 Document Processing
- PDF parsing and text extraction
- Handling multi-page documents

### ✂️ Chunking Strategies
- Fixed-size chunking
- Chunk overlap for context preservation
- Trade-offs between chunk size and recall

### 🔢 Embeddings
- Embedding generation for document chunks
- Ephemeral, in-memory usage
- No reuse across sessions

### 🔍 Retrieval
- Similarity search using an in-memory FAISS index
- Top-K retrieval
- Stateless retrieval per run

### 🧩 Prompt Engineering
- Context injection into prompts
- Grounded answer generation
- Basic hallucination reduction techniques

### 🤖 Local LLM Usage
- Fully local inference
- No paid APIs
- Offline-first setup

### 🔗 LangChain Fundamentals
- Document loaders
- Text splitters
- Embedding interfaces
- Retrieval chains

---


## ❌ What This Project Does NOT Do

To keep the architecture intentionally simple, this project does **not** include:

- ❌ Persistent or disk-backed vector databases
- ❌ Managed or remote vector DB services
- ❌ Long-term conversational memory
- ❌ Multi-document or multi-session retrieval
- ❌ Advanced RAG pipelines (reranking, hybrid search, agents)
- ❌ Production-grade observability or tracing
- ❌ Authentication, authorization, or user management

---

## 🏗️ Architecture Overview

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embedding Generation
 ↓
In-Memory FAISS Index (Ephemeral)
 ↓
Top-K Retriever
 ↓
Prompt + Retrieved Context
 ↓
Local LLM
 ↓
Answer
```

#### Architectural Guarantees

- Vectors live only in memory
- FAISS index is rebuilt on every run
- No data is written to disk
- No cross-session state
- Answers are grounded in retrieved chunks

--- 

## 🧰 Tech Stack

- Language: Python
- LLM Framework: LangChain
- Embeddings: LangChain Embeddings
- Vector Index: FAISS (in-memory only)
- LLM Runtimes: Ollama, LM Studio
- Environment Management: uv

--- 

## 🖥️ Setup & Installation

### Local Ollama Setup

- Install **Ollama**
- Download a supported chat model  
   *(e.g., Gemma 3, LLaMA 3, Mistral, Phi-3)*
   ```bash
   ollama pull gemma3:1b
   ```
- Start the local server:
   
   Ollama runs automatically when a model is invoked.

### Local LM Studio

- Install **LM Studio**
- Download a supported chat model  
   *(e.g., Mistral, LLaMA, Phi)*
- Start the local server:
   - **API Base URL:** `http://localhost:1234/v1`

> **Note:**
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

## 💬 Example Usage

- Upload a PDF
- Ask:
   - “What is the main conclusion of this document?”
- The system:
   - Retrieves relevant chunks
   - Injects them into the prompt
   - Generates a grounded answer using a local LLM

---

## 🔍 Observability

### Logging

- PDF successfully loaded and parsed
- Total number of pages extracted from the PDF
- Number of text chunks created after splitting
- Chunk size and overlap configuration used
- Total number of embeddings generated
- FAISS in-memory index creation status

---

## ⚠️ Limitations

- In-memory only (RAM-bound)
- FAISS index rebuilt on every run
- No persistence across sessions
- Limited by model context window
- Not suitable for large-scale or production workloads

---