from langchain_community.document_loaders import (
    DirectoryLoader,
    UnstructuredFileLoader
)
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import nltk
nltk.download("punkt_tab")


# Paths of directories
DOC_DIR_PATH = "C:/Users/ravin/Ravindra/RAG - Langchain/RAG-Langchain/documents"
VECTOR_DB_PATH = "C:/Users/ravin/Ravindra/RAG - Langchain/RAG-Langchain/vector-db"
COLLECTION_NAME = "document_collection"


# Initialize directory loader
loader = DirectoryLoader(
    path=DOC_DIR_PATH,
    glob="./*.pdf",
    loader_cls=UnstructuredFileLoader
)

# Load the documents
documents = loader.load()

# initialize text splitter
text_splitter = CharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500,
)

# Split the document into smaller chunks
text_chunks = text_splitter.split_documents(
    documents=documents
)

# Load embedding model for embedding vector
embedding = HuggingFaceEmbeddings()

# create vector store
vector_store = Chroma.from_documents(
    documents=text_chunks,
    embedding=embedding,
    persist_directory=VECTOR_DB_PATH,
    collection_name=COLLECTION_NAME
)

print("***********Created vector store******************")
