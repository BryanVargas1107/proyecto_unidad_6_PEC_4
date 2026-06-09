"""
Ejercicio 3: Distribución de goles marcados por equipos locales y visitantes.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import config


def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calcula la distribución de goles a tiempo completo para los equipos
    locales (FTHG) y visitantes (FTAG).

    Cada DataFrame resultante tiene como índice el número de goles marcados
    y como columna 'matches' el número de partidos en que se han marcado
    exactamente ese número de goles.

    Args:
        data (pandas.DataFrame): Dataset de La Liga ya cargado y limpio.

    Returns:
        tuple: Par de DataFrames (distr_goals_home, distr_goals_away):
            - distr_goals_home: distribución de goles del equipo local.
            - distr_goals_away: distribución de goles del equipo visitante.
    """
    distr_goals_home = (
        data["FTHG"]
        .value_counts()
        .sort_index()
        .rename_axis("goals")
        .to_frame(name="matches")
    )

    distr_goals_away = (
        data["FTAG"]
        .value_counts()
        .sort_index()
        .rename_axis("goals")
        .to_frame(name="matches")
    )

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(
    distr_goals_home: pd.DataFrame,
    distr_goals_away: pd.DataFrame
) -> None:
    """
    Genera una figura con dos subplots de barras que representan la
    distribución de goles marcados por los equipos locales y visitantes.

    La figura se guarda en src/img/ con el nombre del alumno y timestamp.

    Args:
        distr_goals_home (pandas.DataFrame): Distribución de goles locales.
        distr_goals_away (pandas.DataFrame): Distribución de goles visitantes.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].bar(
        distr_goals_home.index,
        distr_goals_home["matches"],
        color="#4C72B0",
        edgecolor="white",
        linewidth=0.5
    )
    axes[0].set_title("Goles equipo local (FTHG)", fontsize=13)
    axes[0].set_xlabel("Número de goles")
    axes[0].set_ylabel("Número de partidos")
    axes[0].set_xticks(distr_goals_home.index)
    axes[0].yaxis.grid(True, linestyle="--", alpha=0.5)
    axes[0].set_axisbelow(True)

    axes[1].bar(
        distr_goals_away.index,
        distr_goals_away["matches"],
        color="#DD8452",
        edgecolor="white",
        linewidth=0.5
    )
    axes[1].set_title("Goles equipo visitante (FTAG)", fontsize=13)
    axes[1].set_xlabel("Número de goles")
    axes[1].set_ylabel("Número de partidos")
    axes[1].set_xticks(distr_goals_away.index)
    axes[1].yaxis.grid(True, linestyle="--", alpha=0.5)
    axes[1].set_axisbelow(True)

    fig.suptitle(
        "Distribución de goles: local vs visitante (La Liga 1995-2025)",
        fontsize=14,
        fontweight="bold"
    )
    plt.tight_layout()

    src_dir = os.path.dirname(os.path.dirname(__file__))
    img_dir = os.path.join(src_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    filename = f"grafica_ex3_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(img_dir, filename), dpi=150, bbox_inches="tight")
    plt.close()
