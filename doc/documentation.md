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
│ ├── config.py # Configuration parameters (paths, model parameters, etc.)
│ ├── data_loader.py # Functions to load and process the document
│ ├── model_setup.py # Functions to initialize the model, embeddings, vector store, and QA chain
│ ├── models/7B/ # Contains the Llama 2 7B Chat GGUF model (included in Docker image)
│ └── main.py # Main application code
├── doc/
│ ├── promtior_info.txt # Promtior information file
│ ├── UML-Component-Diagram.png # UML component diagram
│ └── DOCUMENTATION.md # This technical documentation
├── tests/
│ └── test_basic.py # Basic unit tests (e.g., verifying document loading)
│ ├── test_model_setup.py # Unit tests for model initialization and query execution
├── requirements.txt # Project dependencies
├── Dockerfile # Docker configuration (includes model in container)
├── Procfile # Defines the command to run in Railway deployment
└── runtime.txt # Specifies Python runtime version

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

4. **Model Handling (Handled in Dockerfile)**

The Llama 2 7B Chat GGUF model is already included in the Docker image.
The Dockerfile ensures that the model is available inside the container.
No manual download is required.

5. **Run the Application:**

**Local Execution (Virtual Environment):**
python src/main.py

**Run with Docker:**
docker build -t promtior-chatbot .
docker run --rm -it promtior-chatbot

**Deploy in Railway:**
(See Railway-specific documentation below.)

## 4. Running Tests

To run the tests, execute:

python -m unittest discover -s src/tests

This includes:

test_basic.py: Verifies document loading.
test_model_setup.py: Ensures model initialization and QA chain execution work as expected.

## 5. Deployment in Railway

This project is designed to run on Railway using a Docker container.
The Dockerfile ensures that all dependencies and the model are included.

The Procfile defines the entry point:
web: python src/main.py

Deployment Steps:
Push the latest changes to GitHub (git push origin feature/deploy).
Railway will automatically detect changes and redeploy the container.
Check logs in Railway to ensure the service starts correctly.

Current Issue on Railway:
At the moment, the deployment on Railway is not working as expected. The service crashes after deployment, likely due to model handling or resource limitations. This issue is under investigation, and updates will be provided in future iterations of the documentation.

## 6. Architecture Diagram

Below is a UML Component Diagram (UML-Component-Diagram.png) illustrating how each component (file) in the project interacts to form the chatbot:

![UML Component Diagram](./UML-Component-Diagram.png)

## 7. Future Improvements

Interactive Interface: Implement a web or CLI interactive interface for dynamic queries.
Optimization: Explore using a smaller or more quantized model to improve CPU inference speed.
Robustness: Enhance error handling and add more unit tests to cover additional parts of the system.

## 8. Conclusion

This project demonstrates the integration of NLP techniques using LangChain, llama-cpp-python, and FAISS to build a QA chatbot that answers specific questions about Promtior. The modular structure, clear configuration, and inclusion of unit tests highlight adherence to good software engineering practices.
