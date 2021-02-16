# Initialize connection with rest of lib
from utils import *
from DL_ClassifierModel import *

# Own imports
from pathlib import Path

data_path = Path("data/celegans/data.txt")
assert data_path.exists(), "Download the necessary data from the following link: " \
                           "https://raw.githubusercontent.com/masashitsubaki/CPI_prediction/master/dataset/celegans/original/data.txt"

data_class = DataClass_normal(dataPath=data_path)

print(data_class)
