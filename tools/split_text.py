import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)


def split_documents(documents, chunk_size: int = 1000, chunk_overlap: int = 150):
    logger.info(f"Chunk config - size: {chunk_size}, overlap: {chunk_overlap}")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(documents)
    logger.info(f"Number of text chunks created after splitting: {len(chunks)}")
    return chunks
