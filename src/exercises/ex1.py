"""
Ejercicio 1: Carga del dataset y análisis exploratorio de los datos.
"""
import os
import config
import pandas as pd
import matplotlib.pyplot as plt


def load_and_eda(file: str) -> pd.DataFrame:
    """
    Carga el dataset de La Liga desde un fichero CSV y elimina las columnas
    de medio tiempo ('HTHG', 'HTAG', 'HTR').

    Args:
        file (str): Ruta al fichero CSV con los datos históricos de La Liga.

    Returns:
        pandas.DataFrame: Dataset limpio listo para su análisis exploratorio.
    """
    data = pd.read_csv(file)
    cols_to_drop = ["HTHG", "HTAG", "HTR"]
    data = data.drop(columns=cols_to_drop)
    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """
    Genera una figura con dos boxplots que muestran la distribución de goles
    marcados por los equipos locales (FTHG) y visitantes (FTAG).

    La figura se guarda en src/img/ con el nombre del alumno y timestamp.

    Args:
        data (pandas.DataFrame): Dataset de La Liga ya cargado y limpio.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))

    axes[0].boxplot(data["FTHG"].dropna(), patch_artist=True,
                    boxprops=dict(facecolor="#4C72B0", color="#2c3e50"),
                    medianprops=dict(color="white", linewidth=2),
                    whiskerprops=dict(color="#2c3e50"),
                    capprops=dict(color="#2c3e50"),
                    flierprops=dict(marker="o", color="#4C72B0", alpha=0.4))
    axes[0].set_title("Goles equipo local (FTHG)", fontsize=13)
    axes[0].set_ylabel("Número de goles")
    axes[0].set_xticks([])

    axes[1].boxplot(data["FTAG"].dropna(), patch_artist=True,
                    boxprops=dict(facecolor="#DD8452", color="#2c3e50"),
                    medianprops=dict(color="white", linewidth=2),
                    whiskerprops=dict(color="#2c3e50"),
                    capprops=dict(color="#2c3e50"),
                    flierprops=dict(marker="o", color="#DD8452", alpha=0.4))
    axes[1].set_title("Goles equipo visitante (FTAG)", fontsize=13)
    axes[1].set_ylabel("Número de goles")
    axes[1].set_xticks([])

    fig.suptitle("Distribución de goles: local vs visitante (La Liga 1995-2025)",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()

    src_dir = os.path.dirname(os.path.dirname(__file__))
    img_dir = os.path.join(src_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    filename = f"grafica_ex1_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(img_dir, filename), dpi=150, bbox_inches="tight")
    plt.close()
