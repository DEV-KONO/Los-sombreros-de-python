import pandas as pd

def y_range(ruta):
    df = pd.read_csv(ruta)
    df['date'] = pd.to_datetime(df['date'])
    return range(df['date'].min().year, df['date'].max().year)
