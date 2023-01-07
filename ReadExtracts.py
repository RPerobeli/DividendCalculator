import pandas as pd
import os

def LerExtratosCSV_Clear():
    path = os.getcwd()
    path += "\DividendCalculator\Extratos"
    os.chdir(path )

    frames = []
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".csv"):
            file_path = f"{path}\{file}"
    
            # call read text file function
            df = pd.read_csv(file_path, sep = ';')
            frames.append(df)
            df_total = pd.concat(frames)
    return(df_total)