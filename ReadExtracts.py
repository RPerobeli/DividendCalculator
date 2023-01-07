import pandas as pd
import os

path = os.getcwd()
print(path)
os.chdir(path)

for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".csv"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        df = pd.read_csv(file_path, sep = ';')

