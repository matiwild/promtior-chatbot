# Technical Documentation - Promtior Chatbot

## 1. Overview

This project implements a QA chatbot that uses the Llama 2 7B model in GGUF format along with LangChain to answer questions about Promtior's services. The solution integrates several components:

- **Data Loading:** Loads Promtior's information from a text file (`promtior_info.txt`).
- **Embeddings & Vector Store:** Generates embeddings using `HuggingFaceInstructEmbeddings` (model "hkunlp/instructor-large") and builds a vector store with FAISS.
- **Language Model:** Initializes the Llama 2 7B model using `LlamaCpp` from llama-cpp-python.
- **QA Chain:** Combines the model and vector store using a RetrievalQA chain to generate answers.


## 2. Project Structure

promtior-chatbot/
├── src/
│   ├── config.py           # Configuration parameters (paths, model parameters, etc.)
│   ├── data_loader.py      # Functions to load and process the document
│   ├── model_setup.py      # Functions to initialize the model, embeddings, vector store, and QA chain
│   └── main.py             # Main application code
├── doc/
│   ├── promtior_info.txt   # Promtior information file
│   ├── UML-Component-Diagram.png # UML component diagram
│   └── DOCUMENTATION.md    # This technical documentation
├── tests/
│   └── test_basic.py       # Basic unit tests (e.g., verifying document loading)
├── requirements.txt        # Project dependencies
└── README.md               # General instructions and project summary

## 3. Installation and Execution Instructions
1. **Clone the Repository:**
git clone https://github.com/your_username/promtior-chatbot.git
cd promtior-chatbot
2. **Create and Activate a Virtual Environment:**

**On Windows:**
python -m venv env
.\env\Scripts\activate

**On macOS/Linux:**
python3 -m venv env
source env/bin/activate

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Place the Model:**
Download the Llama 2 7B Chat GGUF model file.
Place the model file in the src/models/7B/ directory.
Ensure that the MODEL_PATH in src/config.py points to the correct file (e.g., ./src/models/7B/llama-2-model.gguf).

5. **Run the Application:**
python src/main.py
The chatbot will load Promtior's information, initialize the model and vector store, and answer sample queries:

"What services does Promtior offer?"
"When was the company founded?"
## 4. Running Tests
To run the tests, execute:

python -m unittest discover -s src/tests
## 5. Architecture Diagram
Below is a UML Component Diagram (UML-Component-Diagram.png) illustrating how each component (file) in the project interacts to form the chatbot:

![UML Component Diagram](./UML-Component-Diagram.png)

## 6. Future Improvements
Interactive Interface: Implement a web or CLI interactive interface for dynamic queries.
Optimization: Explore using a smaller or more quantized model to improve CPU inference speed.
Robustness: Enhance error handling and add more unit tests to cover additional parts of the system.

## 7. Conclusion
This project demonstrates the integration of NLP techniques using LangChain, llama-cpp-python, and FAISS to build a QA chatbot that answers specific questions about Promtior. The modular structure, clear configuration, and inclusion of unit tests highlight adherence to good software engineering practices.

