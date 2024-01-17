"""
This code creates a chatbot that can answer questions based on a given PDF file.
The first few lines of the code import the necessary libraries and modules.
The `CreateChatbot()` function creates a chatbot that can answer questions based on a given PDF file. The function prompts the user to enter the file path of the PDF file, loads the PDF file, and creates a `RetrievalQA` object that can be used to answer questions based on the PDF file.
The `while` loop at the end of the code runs the chatbot. It prompts the user to enter a question, and then uses the `RetrievalQA` object to generate a response to the question.
This code requires the user to have a Hugging Face API token, which is used to access the Hugging Face model. The user is prompted to enter the API token when the code is run.
"""

from langchain_community.llms import HuggingFaceHub
from src.pdfloader import load_pdf
from src.prompt import pdfreaderprompt
from langchain.chains import RetrievalQA
from getpass import getpass
import os

huggingface_api_token = input("Enter Hugging Face API Token: ")
HUGGINGFACEHUB_API_TOKEN = getpass()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_token

repo_id = "google/flan-t5-xxl"  

def CreateChatbot():
    file_path = input("Enter file path: ")
    vectorDB = load_pdf(file_path)

    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )

    prompt = pdfreaderprompt()

    chain_type_kwargs = {
        "prompt": prompt
    }

    chain = RetrievalQA.from_chain_type(
        llm=llm, retriever=vectorDB.as_retriever(), chain_type_kwargs=chain_type_kwargs
    )

    return chain

if __name__ == '__main__':
    chatbot = CreateChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.invoke(user_input)
        print("Chatbot: ", response)
