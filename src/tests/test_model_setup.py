import unittest
from src.config import MODEL_PATH, DOCUMENT_PATH, N_CTX, TEMPERATURE, N_THREADS, MAX_TOKENS, EMBEDDING_MODEL
from src.data_loader import load_document
from src.model_setup import initialize_vector_store, initialize_model, build_qa_chain
from langchain_community.llms import LlamaCpp

class TestModelSetup(unittest.TestCase):
    def setUp(self):
        self.document_text = load_document(DOCUMENT_PATH)
    
    def test_initialize_vector_store(self):
        vs = initialize_vector_store(self.document_text, EMBEDDING_MODEL)
        self.assertIsNotNone(vs, "The vector store should not be None.")
    
    def test_initialize_model(self):
        llm = initialize_model(MODEL_PATH, N_CTX, TEMPERATURE, N_THREADS, verbose=False)
        self.assertIsInstance(llm, LlamaCpp, "The model should be an instance of LlamaCpp.")
    
    def test_build_qa_chain(self):
        vs = initialize_vector_store(self.document_text, EMBEDDING_MODEL)
        llm = initialize_model(MODEL_PATH, N_CTX, TEMPERATURE, N_THREADS, verbose=False)
        qa_chain = build_qa_chain(llm, vs)
        self.assertIsNotNone(qa_chain, "The QA chain should not be None.")
    
    def test_run_query(self):
        vs = initialize_vector_store(self.document_text, EMBEDDING_MODEL)
        llm = initialize_model(MODEL_PATH, N_CTX, TEMPERATURE, N_THREADS, verbose=False)
        qa_chain = build_qa_chain(llm, vs)
        result = qa_chain.invoke(input="Test query", max_tokens=32)
        self.assertIsInstance(result, dict, "The result should be a dictionary.")
        self.assertIn("result", result, "The result dictionary should contain a 'result' key.")
        self.assertTrue(len(result["result"]) > 0, "The 'result' value should not be empty.")

if __name__ == '__main__':
    unittest.main()
