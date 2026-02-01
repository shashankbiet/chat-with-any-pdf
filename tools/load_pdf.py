import logging
from langchain_community.document_loaders import PyPDFLoader

logger = logging.getLogger(__name__)


def load_documents(path: str):
    logger.info(f"Loading PDF from: {path}")
    loader = PyPDFLoader(path)
    documents = loader.load()
    logger.info(f"PDF successfully loaded and parsed - Pages: {len(documents)}")
    return documents
