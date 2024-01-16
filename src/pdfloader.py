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
