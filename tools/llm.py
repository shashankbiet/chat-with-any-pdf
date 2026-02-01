import logging
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)


def get_llm():
    logger.info("Initializing LLM")
    # LM Studio
    llm = ChatOpenAI(
        openai_api_base="http://localhost:1234/v1",
        openai_api_key="lm-studio",
        model_name="local-model",
        temperature=0.2
    )
    logger.info("LLM successfully initialized")

    # Ollama
    # llm = ChatOllama(
    #     model="gemma3:1b",
    #     temperature=0.2
    # )
    return llm
