from datasets import load_dataset

class DataReader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

    def load(self):
        return load_dataset(self.dataset_name)