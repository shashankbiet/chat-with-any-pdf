from tools import (
    load_documents,
    split_documents,
    get_embeddings,
    build_vectorstore,
    get_retriever,
    get_llm,
    get_prompt,
)


def main():
    documents = load_documents(path = "sample.pdf")

    chunks = split_documents(documents, chunk_size=1000, chunk_overlap=150)

    embeddings = get_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = build_vectorstore(chunks, embeddings)

    retriever = get_retriever(vectorstore, k=3)

    llm = get_llm()

    prompt = get_prompt()

    while True:
        question = input("\nAsk a question (or 'exit'): ")
        if question.lower() == "exit":
            break

        docs = retriever.invoke(question)
        context = "\n\n".join(d.page_content for d in docs)

        chain = prompt | llm
        response = chain.invoke({
            "context": context,
            "question": question
        })

        print("\nAnswer:\n", response.content)


if __name__ == "__main__":
    main()
