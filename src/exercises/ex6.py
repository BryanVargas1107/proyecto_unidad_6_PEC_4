"""
Ejercicio 6: Dataframe summary_1995_2025 y podium histórico de La Liga.

Funciones:
    - fun_total_goals: Calcula el total de goles locales, visitantes y globales.
    - fun_total_goals_by_team: Calcula los goles por equipo (local, visitante y total).
    - fun_summary_1996_2025: Construye el dataframe resumen con puntos y goles.
    - podium: Genera la gráfica de podium con los tres primeros clasificados.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import config


def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """
    Calcula el total de goles marcados por los equipos locales,
    visitantes y el global del dataset completo.

    Args:
        data (pandas.DataFrame): Dataset de La Liga ya cargado y limpio.

    Returns:
        tuple[int, int, int]: Tupla con (home_goals, away_goals, total_goals).
    """
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals
    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(
    data: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Calcula los goles marcados por cada equipo como local, como visitante
    y el total acumulado, ordenados de mayor a menor.

    Args:
        data (pandas.DataFrame): Dataset de La Liga ya cargado y limpio.

    Returns:
        tuple: Tres DataFrames (home_goals_by_team, away_goals_by_team,
            total_goals_by_team), cada uno con el equipo como índice.
    """
    home_goals_by_team = (
        data.groupby("HomeTeam")["FTHG"]
        .sum()
        .sort_values(ascending=False)
        .rename_axis("Team")
        .to_frame(name="home_goals")
    )
    away_goals_by_team = (
        data.groupby("AwayTeam")["FTAG"]
        .sum()
        .sort_values(ascending=False)
        .rename_axis("Team")
        .to_frame(name="away_goals")
    )
    total_goals_by_team = (
        home_goals_by_team["home_goals"]
        .add(away_goals_by_team["away_goals"], fill_value=0)
        .astype(int)
        .sort_values(ascending=False)
        .rename_axis("Team")
        .to_frame(name="total_goals")
    )
    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(
    total_points_by_team: pd.DataFrame,
    home_goals_by_team: pd.DataFrame,
    away_goals_by_team: pd.DataFrame,
    total_goals_by_team: pd.DataFrame
) -> pd.DataFrame:
    """
    Construye el dataframe resumen con puntos y goles de todos los equipos,
    ordenado por puntos totales de mayor a menor.

    Args:
        total_points_by_team (pd.DataFrame): Puntos totales por equipo.
        home_goals_by_team (pd.DataFrame): Goles como local por equipo.
        away_goals_by_team (pd.DataFrame): Goles como visitante por equipo.
        total_goals_by_team (pd.DataFrame): Goles totales por equipo.

    Returns:
        pd.DataFrame: DataFrame resumen con columnas Total_Points,
            home_goals, away_goals y total_goals.
    """
    summary = pd.concat(
        [total_points_by_team, home_goals_by_team,
         away_goals_by_team, total_goals_by_team],
        axis=1
    ).sort_values("Total_Points", ascending=False)
    return summary


def podium(summary_1996_2025: pd.DataFrame) -> str:
    """
    Genera una gráfica de podium con los tres primeros equipos de la
    clasificación histórica. El primer clasificado aparece en el centro,
    el segundo a la izquierda y el tercero a la derecha.

    La figura se guarda en src/img/ con el nombre del alumno y timestamp.

    Args:
        summary_1996_2025 (pd.DataFrame): DataFrame resumen devuelto por
            fun_summary_1996_2025(), ordenado por Total_Points.

    Returns:
        str: Ruta relativa donde se ha guardado la figura.
    """
    top3 = summary_1996_2025.head(3)
    teams = top3.index.tolist()
    points = top3["Total_Points"].tolist()

    # Orden visual: 2º izquierda, 1º centro, 3º derecha
    podium_teams = [teams[1], teams[0], teams[2]]
    podium_points = [points[1], points[0], points[2]]
    podium_colors = ["#C0C0C0", "#FFD700", "#CD7F32"]
    podium_labels = ["2º Puesto", "1º Puesto", "3º Puesto"]

    _, ax = plt.subplots(figsize=(9, 6))

    rects = ax.bar(
        [0, 1, 2],
        podium_points,
        color=podium_colors,
        edgecolor="white",
        linewidth=1.5,
        width=0.6
    )

    for rect, team, pts, label in zip(rects, podium_teams, podium_points, podium_labels):
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            rect.get_height() + 10,
            team,
            ha="center", va="bottom",
            fontsize=12, fontweight="bold"
        )
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            rect.get_height() / 2,
            f"{pts} pts\n{label}",
            ha="center", va="center",
            fontsize=10, color="white", fontweight="bold"
        )

    ax.set_title(
        "Podium Histórico de La Liga (1995-2025)",
        fontsize=14, fontweight="bold", pad=20
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    ax.legend(
        handles=[
            mpatches.Patch(color="#FFD700", label=f"1º {teams[0]}"),
            mpatches.Patch(color="#C0C0C0", label=f"2º {teams[1]}"),
            mpatches.Patch(color="#CD7F32", label=f"3º {teams[2]}")
        ],
        loc="upper right",
        fontsize=10
    )

    plt.tight_layout()

    output_path = f"src/img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    return output_path
