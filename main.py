from read_data import DataReader
from train_model import Model


if __name__ == '__main__':
    df = DataReader('AI paper').create_dataset()
    output = Model().create_summary(df['abstract'][0])
