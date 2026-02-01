import logging
from langchain_core.prompts import ChatPromptTemplate

logger = logging.getLogger(__name__)


def get_prompt():
    logger.info("Loading prompt template")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant answering questions from a PDF."),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}")
    ])
    logger.info("Prompt template loaded successfully")
    return prompt
