import os
import logging
from huggingface_hub import hf_hub_download
from config import MODEL_PATH, DOCUMENT_PATH, N_CTX, TEMPERATURE, N_THREADS, MAX_TOKENS, EMBEDDING_MODEL
from data_loader import load_document
from model_setup import initialize_vector_store, initialize_model, build_qa_chain

def download_model_from_hf(repo_id: str, filename: str, local_path: str):
    """Downloads the model from Hugging Face Hub if it does not exist locally.    """
    if not os.path.exists(local_path):
        logging.info("Model not found at %s. Downloading from %s/%s", local_path, repo_id, filename)
        local_file = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=os.path.dirname(local_path),
            local_dir_use_symlinks=False
        )
        logging.info("Model downloaded successfully to %s", local_file)
        return local_file
    return local_path

def run_query(qa_chain, query: str, max_tokens: int) -> str:
    """Execute a query and return the 'result' from the QA chain."""
    result = qa_chain.invoke(input=query, max_tokens=max_tokens)
    return result.get("result", result)

def main():
    global MODEL_PATH
    logging.basicConfig(level=logging.WARNING)
    
    repo_id = "TheBloke/Llama-2-7B-Chat-GGUF"
    filename = "llama-2-7b-chat.Q2_K.gguf"

    if not os.path.exists(MODEL_PATH):
        MODEL_PATH_local = download_model_from_hf(repo_id, filename, MODEL_PATH)
        MODEL_PATH = MODEL_PATH_local    
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
