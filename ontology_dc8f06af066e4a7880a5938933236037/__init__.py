from transformers import pipeline
import os, contextlib
os.environ['TRANSFORMERS_CACHE'] = f'{os.getcwd()}/cache'

nlp = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

folder_path = 'config/contexts'
context = ""

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        print(f"Reading file: {file_path} and adding to context")
        with open(file_path, 'r', encoding='utf-8') as f:
            with contextlib.suppress(UnicodeDecodeError):
                context += f"{f.read()} "