import logging
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA

def initialize_vector_store(document_text: str, embedding_model: str) -> FAISS:
    """Create documents and a vector store from the provided text."""
    docs = [Document(page_content=document_text)]
    embeddings = HuggingFaceInstructEmbeddings(model_name=embedding_model)
    return FAISS.from_documents(docs, embeddings)

def initialize_model(model_path: str, n_ctx: int, temperature: int, n_threads: int, verbose: bool = False) -> LlamaCpp:
    """Initialize the LlamaCpp model."""
    try:
        llm = LlamaCpp(
            model_path=model_path,
            n_ctx=n_ctx,
            temperature=temperature,
            n_threads=n_threads,
            verbose=verbose
        )
        return llm
    except Exception as e:
        logging.error("Error initializing model: %s", e)
        raise

def build_qa_chain(llm: LlamaCpp, vector_store: FAISS) -> RetrievalQA:
    """ Build the QA chain from the model and vector store."""
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
