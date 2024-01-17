"""
This code defines a function `load_pdf` that loads an unstructured PDF file and creates a vector store that can be used to retrieve information from the PDF file.
The `load_pdf` function is defined to load an unstructured PDF file and create a vector store that can be used to retrieve information from the PDF file.
The `UnstructuredPDFLoader` class from the `langchain_community.document_loaders` module is used to load the PDF file.
The `CharacterTextSplitter` class from the `langchain.text_splitter` module is used to split the PDF file into smaller chunks of text.
The `HuggingFaceEmbeddings` class from the `langchain_community.embeddings` module is used to generate embeddings for the text chunks.
The `Chroma` class from the `langchain_community.vectorstores` module is used to create a vector store that can be used to retrieve information from the PDF file.
The `load_pdf` function takes a file path as input and returns a `Chroma` object that can be used to retrieve information from the PDF file.
"""

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

def load_pdf(filepath):
    loader = UnstructuredPDFLoader(filepath)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_documents(texts, embeddings, collection_name=filepath.split("/")[-1].split(".")[0])
    return vectorstore
