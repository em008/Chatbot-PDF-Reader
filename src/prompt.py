"""
This code defines a function `pdfreaderprompt` that returns a `PromptTemplate` object. The `PromptTemplate` object is used to create a template for generating prompts for a language model. Here is a brief explanation of the code:
The `pdfreaderprompt` function is defined to create a `PromptTemplate` object that can be used to generate prompts for a language model.
The `PromptTemplate` object is created using a string template that specifies the format of the prompt. The string template contains two placeholders: `{context}` and `{question}`.
The `input_variables` argument of the `PromptTemplate` constructor is used to specify the names of the variables that will be used to fill in the placeholders.
"""

from langchain.prompts import PromptTemplate

def pdfreaderprompt():
    prompt_template = """PDF: {context}
    Question: {question}"""
    
    return PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
