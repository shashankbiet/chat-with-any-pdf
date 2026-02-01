import logging

logger = logging.getLogger(__name__)


def get_retriever(vectorstore, k: int = 3):
    logger.info(f"Initializing retriever with k={k}")
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever
