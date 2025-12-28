from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama


# 1. Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# 2. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)
chunks = text_splitter.split_documents(documents)

# 3. Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Store in vector DB
vectorstore = FAISS.from_documents(chunks, embeddings)

# 5. Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 6. Load Local LLM 

# LM Studio
# llm = ChatOpenAI(
#     openai_api_base="http://localhost:1234/v1",
#     openai_api_key="lm-studio",
#     model_name="local-model",
#     temperature=0.2
# )

# Ollama
llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.2
)

# 7. Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answering questions from a PDF."),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# 8. Ask questions
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
