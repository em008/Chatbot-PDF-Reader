"""
This code creates a chatbot that can answer questions based on a given PDF file.
This code requires the user to have a Hugging Face API token, which is used to access the Hugging Face model. The user is prompted to enter the API token when the code is run.
"""

from langchain_community.llms import HuggingFaceHub
from huggingface_hub import InferenceClient
from src.pdfloader import load_pdf
from src.prompt import pdfreaderprompt
from langchain.chains import RetrievalQA
import os


def get_huggingface_api_token():
    # Prompt user for Hugging Face API token
    return input("Enter Hugging Face API Token: ")


def initialize_language_model():
    # Initialize language model
    repo_id = "google/flan-t5-xxl"
    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    return llm


def load_pdf_file():
    # Load PDF file
    file_path = input("Enter file path: ")
    return load_pdf(file_path)


def create_chatbot(llm, vectorDB):
    # Set up chatbot prompt
    prompt = pdfreaderprompt()

    # Create RetrievalQA chain
    chain_type_kwargs = {"prompt": prompt}
    chatbot = RetrievalQA.from_chain_type(
        llm=llm, retriever=vectorDB.as_retriever(), chain_type_kwargs=chain_type_kwargs
    )

    return chatbot


if __name__ == '__main__':
    huggingface_api_token = get_huggingface_api_token()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_token

    language_model = initialize_language_model()
    pdf_file = load_pdf_file()
    chatbot_input = create_chatbot(language_model, pdf_file)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_input.invoke(user_input)
        print("Chatbot:", response)
