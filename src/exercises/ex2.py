"""
Ejercicio 2: Partidos totales jugados por equipo.
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import config


def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el número total de partidos jugados por cada equipo
    a lo largo de todas las temporadas, sumando sus partidos
    como local (HomeTeam) y como visitante (AwayTeam).

    Args:
        data (pandas.DataFrame): Dataset de La Liga ya cargado y limpio.

    Returns:
        pandas.DataFrame: DataFrame con los equipos como índice y la columna
            'total_matches' con el número total de partidos jugados.
    """
    home_counts = data.groupby("HomeTeam").size().rename("home")
    away_counts = data.groupby("AwayTeam").size().rename("away")

    matches_team_total = (
        pd.concat([home_counts, away_counts], axis=1)
        .fillna(0)
        .astype(int)
    )
    matches_team_total["total_matches"] = (
        matches_team_total["home"] + matches_team_total["away"]
    )
    matches_team_total = matches_team_total[["total_matches"]].sort_values(
        "total_matches", ascending=False
    )
    matches_team_total.index.name = "Team"

    return matches_team_total


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> str:
    """
    Genera un gráfico de barras con el total de partidos jugados
    por cada equipo. Los equipos siempre en primera división
    se destacan en rojo.

    La figura se guarda en src/img/ con el nombre del alumno y timestamp.

    Args:
        matches_team_total (pandas.DataFrame): DataFrame devuelto por
            total_matches(), con los equipos como índice y la columna
            'total_matches'.

    Returns:
        None
    """
    max_matches = matches_team_total["total_matches"].max()
    colors = [
        "#E63946" if v == max_matches else "#4C72B0"
        for v in matches_team_total["total_matches"]
    ]

    _, ax = plt.subplots(figsize=(18, 7))
    ax.bar(
        matches_team_total.index,
        matches_team_total["total_matches"],
        color=colors,
        edgecolor="white",
        linewidth=0.5
    )
    ax.set_title(
        "Total de partidos jugados por equipo en La Liga (1995-2025)",
        fontsize=14, fontweight="bold", pad=15
    )
    ax.set_xlabel("Equipo", fontsize=11, labelpad=10)
    ax.set_ylabel("Número de partidos", fontsize=11)
    ax.tick_params(axis="x", rotation=90, labelsize=8)
    ax.tick_params(axis="y", labelsize=9)
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)

    legend_elements = [
        Patch(facecolor="#E63946", label="Siempre en Primera División"),
        Patch(facecolor="#4C72B0", label="Resto de equipos")
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper right")
    plt.tight_layout()

    output_path = f"src/img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    return output_path
    