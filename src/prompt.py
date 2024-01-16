from langchain.prompts import PromptTemplate

def pdfreaderprompt():
    prompt_template = """PDF: {context}
    Question: {question}"""
    
    return PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
