# Chatbot-PDF-Reader

For this projects a chatbot that can read PDF's and answer questions about its contents is built using the LangChain framework in Python and the large language model FLAN by Google. 
The Hugging Face Hub is used to load the large language model and get the API token. When running the chatbot it asks the user to enter their API token. The chatbot also asks the user to enter the PDF file path.
Once the PDF is loaded the data can be transformed to be more suitable for this application. To embed the data Hugging Face embeddings is used. These embeddings convert data into a numerical format which enables operations to be peformed. After converting the unstructured data into embeddings it can be stored in a local database called a vector store. This is used as context inside the large language model. Chaining is necessary for the large language model because enables the combination of multiple components to create a single coherent application. An object is created to generate a response to user questions and is used in a chain.

To run the app locally open a terminal or CLI and navigate to the directory where the `requirements.txt` file is located. Next, run the following command to install the packages listed in `requirements.txt`: `pip install -r requirements.txt`. Then, navigate to the directory where the `chatbot.py` file is located and run the command: `python chatbot.py`. The app will run on the terminal or CLI and will ask for the Hugging Face API token and a PDF file path. 

Tech Stack
- Python, LangChain Framework, Google FLAN
