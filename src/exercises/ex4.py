"""
Ejercicio 4: Partidos ganados en casa, fuera o empatados.
"""
# pylint: disable=invalid-name
import matplotlib.pyplot as plt
import pandas as pd
import config


def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el número de partidos ganados por el equipo local (H),
    visitante (A) o que terminaron en empate (D).

    Args:
        data (pandas.DataFrame): Dataset de La Liga.

    Returns:
        pandas.DataFrame: DataFrame con el conteo de resultados, ordenado
            por H, A y D.
    """
    ftr_df = (
        data["FTR"]
        .value_counts()
        .reindex(["H", "A", "D"])
        .rename_axis("Result")
        .to_frame(name="Matches")
    )
    return ftr_df


def plot_FTR(ftr: pd.DataFrame) -> str:
    """
    Genera un gráfico de barras con la distribución de los resultados
    de los partidos (H, A, D).

    La figura se guarda en src/img/ con el nombre del alumno y timestamp.

    Args:
        ftr (pandas.DataFrame): DataFrame devuelto por FTR().

    Returns:
        None
    """
    _, ax = plt.subplots(figsize=(8, 6))

    colors = ["#4C72B0", "#DD8452", "#55A868"]

    ax.bar(
        ftr.index,
        ftr["Matches"],
        color=colors,
        edgecolor="white",
        linewidth=0.5
    )

    ax.set_title("Resultados Históricos de La Liga (1995-2025)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Resultado (H: Local, A: Visitante, D: Empate)", fontsize=11, labelpad=10)
    ax.set_ylabel("Número de partidos", fontsize=11)
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)

    plt.tight_layout()

    output_path = f"src/img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    return output_path
