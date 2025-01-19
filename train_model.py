from transformers import pipeline
from config import config
import torch

class Model:
    def __init__(self):
        self.model = config['model']
        self.device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
        print(self.device)

    def get_model(self):
        self.summarizer = pipeline("summarization", model=config['model'], device=self.device)

    def create_summary(self, text):
        self.get_model()
        return self.summarizer(text)
