# 📚 RAG-Langchain -- Retrieval Augmented Generation with LangChain

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange)
![LLM](https://img.shields.io/badge/LLM-Llama3.1-purple)

A Retrieval Augmented Generation (RAG) system built using **LangChain**,
**Chroma Vector Database**, and **Groq LLM**. This project allows users
to ask questions about their **custom PDF documents** and receive
AI-generated answers grounded in those documents.

------------------------------------------------------------------------

# 📌 Project Overview

Large Language Models are powerful but limited to their training data.
**RAG solves this by combining LLMs with external knowledge sources.**

Pipeline:

1.  Load PDF documents
2.  Split documents into chunks
3.  Generate embeddings
4.  Store embeddings in a vector database
5.  Retrieve relevant chunks
6.  Generate answers using an LLM

------------------------------------------------------------------------

# 🧠 RAG Architecture

User Query │ ▼ Retriever (Chroma Vector DB) │ ▼ Relevant Document Chunks
│ ▼ LLM (Llama 3.1 via Groq) │ ▼ Final Answer

------------------------------------------------------------------------

# ⚙️ Tech Stack

-   Python
-   LangChain
-   Chroma Vector Database
-   HuggingFace Embeddings
-   Groq LLM
-   NLTK

------------------------------------------------------------------------

# 📂 Project Structure

    RAG-Langchain
    │
    ├── documents/
    │   └── sample.pdf
    │
    ├── vector-db/
    │
    ├── document_ingestion.py
    │
    ├── retrieval.py
    │
    ├── constants.py
    │
    ├── .env
    │
    ├── requirements.txt
    │
    └── README.md

------------------------------------------------------------------------

# 🚀 Installation

## 1 Clone Repository

    git clone https://github.com/CoderVindra/RAG-Langchain.git
    cd RAG-Langchain

## 2 Create Virtual Environment

    python -m venv venv

Activate:

Windows

    venv\Scripts\activate

Linux / Mac

    source venv/bin/activate

## 3 Install Dependencies

    pip install -r requirements.txt
------------------------------------------------------------------------

# 🔑 Environment Variables

Create `.env` file:

    GROQ_API_KEY=your_groq_api_key

------------------------------------------------------------------------

# ▶️ Running the Project

## Step 1 Add Documents

Place PDF files inside:

    documents/

## Step 2 Create Vector Database

    python document_ingestion.py

This generates embeddings and stores them in `vector-db/`.

## Step 3 Query the System

    python retrieval.py

Example query:

    What does documents say about origin of life?

------------------------------------------------------------------------

# ✨ Features

-   Document based Q&A
-   Fast vector search using Chroma
-   HuggingFace embeddings
-   Groq powered LLM
-   Easy to extend with more documents

------------------------------------------------------------------------

# 👨‍💻 Author

**Ravindra Pawar**

Backend & AI Developer\
Python \| LangChain \| RAG \| LLM Applications
