import logging
from langchain_community.vectorstores import FAISS

logger = logging.getLogger(__name__)


def build_vectorstore(documents, embeddings):
    logger.info(f"Building FAISS in-memory index with {len(documents)} documents")
    vectorstore = FAISS.from_documents(documents, embeddings)
    logger.info("FAISS in-memory index creation status: SUCCESS")
    return vectorstore
