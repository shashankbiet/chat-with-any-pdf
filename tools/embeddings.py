import logging
from langchain_community.embeddings import HuggingFaceEmbeddings

logger = logging.getLogger(__name__)


def get_embeddings(model_name: str):
    logger.info(f"Initializing embeddings model: {model_name}")
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    logger.info(f"Embeddings model initialized successfully")
    return embeddings
