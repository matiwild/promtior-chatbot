FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p src/models/7B

RUN python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='TheBloke/Llama-2-7B-Chat-GGUF', filename='llama-2-7b-chat.Q2_K.gguf', local_dir='src/models/7B', local_dir_use_symlinks=False)"

COPY . .

CMD ["python", "src/main.py"]
