import os
from dotenv import load_dotenv
from constants import VECTOR_DB_PATH, COLLECTION_NAME
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA


# load env variables
load_dotenv()

# Initialize llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
)

# Load embedding model
embedding = HuggingFaceEmbeddings()

# load vector store
vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embedding
)

# create retriever from vector store
retriever = vector_store.as_retriever()

# create retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Send user query and display result
query = "What does documents say about origin of life?"
response = qa_chain.invoke({"query": query})
print(response.get("result"))
