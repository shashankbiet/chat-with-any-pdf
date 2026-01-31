from langchain_core.prompts import ChatPromptTemplate


def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant answering questions from a PDF."),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}")
    ])
