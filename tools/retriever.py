def get_retriever(vectorstore, k: int = 3):
    return vectorstore.as_retriever(search_kwargs={"k": k})
