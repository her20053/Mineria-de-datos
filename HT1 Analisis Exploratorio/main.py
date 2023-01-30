import pandas as pd

def exploracion_rapida():
    df = pd.read_csv("movies.csv", encoding= 'unicode_escape')
    print(df.describe())
    print(df.info())
    print(df.head())
    
if __name__ == "__main__":
    exploracion_rapida()