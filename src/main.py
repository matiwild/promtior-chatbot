import logging
from config import MODEL_PATH, DOCUMENT_PATH, N_CTX, TEMPERATURE, N_THREADS, MAX_TOKENS, EMBEDDING_MODEL
from data_loader import load_document
from model_setup import initialize_vector_store, initialize_model, build_qa_chain


def run_query(qa_chain, query: str, max_tokens: int) -> str:
    """Execute a query and return the 'result' from the QA chain."""
    result = qa_chain.invoke(input=query, max_tokens=max_tokens)
    return result.get("result", result)

def main():
    logging.basicConfig(level=logging.WARNING)
    
    document_text = load_document(DOCUMENT_PATH)
    
    vector_store = initialize_vector_store(document_text, EMBEDDING_MODEL)
    
    llm = initialize_model(MODEL_PATH, N_CTX, TEMPERATURE, N_THREADS, verbose=False)
    
    qa_chain = build_qa_chain(llm, vector_store)
    
    query1 = "What services does Promtior offer?"
    query2 = "When was the company founded?"
    
    print("Question:", query1)
    print("Answer:", run_query(qa_chain, query1, MAX_TOKENS))
    print("\nQuestion:", query2)
    print("Answer:", run_query(qa_chain, query2, MAX_TOKENS))

if __name__ == "__main__":
    main()
