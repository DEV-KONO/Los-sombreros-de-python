import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def csv_to_hist(route: str):
    df = pd.read_csv(route)
    df['date'] = pd.to_datetime(df['date'])
    df['Positivo'] = df['Sentimiento']
    df['Negativo'] = abs(df['Sentimiento']-1)
    df.drop('Sentimiento', axis=1, inplace = True)

    df2 = df[['date', 'Positivo', 'Negativo']].groupby(['date']).sum()
    df2.reset_index(inplace = True)

    df2['date'] = pd.to_datetime(df2['date'])
    df2['month'] = df2['date'].dt.month
    df2['year'] = df2['date'].dt.year

    def f_mes(n_mes,año):
        df_año = df2[df2['year']==año]
        df_mes = df_año[df_año['month']==n_mes]
        return df_mes
    def grafico_comentarios(mes,año):
        fig, ax = plt.subplots()
        ax.bar(f_mes(mes,año).date, f_mes(mes,año).Positivo)
        ax.bar(f_mes(mes,año).date, f_mes(mes,año).Negativo*-1)

        if mes == 1:
            m = 'Enero'
        if mes == 2:
            m = 'Febrero'
        if mes == 3:
            m = 'Marzo'
        if mes == 4:
            m = 'Abril'
        if mes == 5:
            m = 'Mayo'
        if mes == 6:
            m = 'Junio'
        if mes == 7:
            m = 'Julio'
        if mes == 8:
            m = 'Agosto'
        if mes == 9:
            m = 'Septiembre'
        if mes == 10:
            m = 'Octubre'
        if mes == 11:
            m = 'Noviembre'
        if mes == 12:
            m = 'Diciembre'

        # Formatting x labels
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.tick_params(labelbottom=False)
        plt.tight_layout()
        plt.title('Comentarios Positivos vs Negativos')
        plt.xlabel(m+' '+str(año))
        #plt.ylabel('Dias')
    
        # Use absolute value for y-ticks
        ticks =  ax.get_yticks()
        ax.set_yticklabels([int(abs(tick)) for tick in ticks])

    grafico_comentarios(5, 2023)