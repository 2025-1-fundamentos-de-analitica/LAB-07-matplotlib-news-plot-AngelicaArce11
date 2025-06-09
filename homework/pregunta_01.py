"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # Creamos la figura
    plt.Figure()

    # Creamos la paleta de colores para cada columna
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey'
    }

    # Creamos el orden de importancia de cada columna
    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1
    }

    # Creamos el grosor de la linea de cada columna
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2
    }

    # Leemos el archivo
    df = pd.read_csv('files/input/news.csv', index_col=0)

    # LLenamos la figura con la informacion de cada columna 
    for col in df.columns:
        plt.plot(
            df[col], 
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidths[col],
            label= col
        )

    # Titulo de la grafica
    plt.title('How people get their news', fontsize=16)

    # Ocultamos las lineas que enmarcan el grafico
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    # Ocultamos el eje y
    plt.gca().axes.get_yaxis().set_visible(False)


    for col in df.columns:
        # Creamos un punto para el inicio de las lineas
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col]
        )
        # Ponemos un texto al punto del inicio
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + ' ' + str(df[col][first_year]) + '%',
            ha='right',
            va='center',
            color=colors[col]
        )
        # Creamos un punto al final de las lineas
        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col]
        )
        # Ponemos un texto que acompaña al punto del final
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + '%',
            ha='left',
            va='center',
            color=colors[col]
        )

    # Hacemos que aparezcan todos los años en el eje x
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    )

    # Creamos la carpeta de plots
    os.makedirs('files/plots', exist_ok=True)

    # Guardamos la imagen de la grafica
    plt.tight_layout()
    plt.savefig('files/plots/news.png')