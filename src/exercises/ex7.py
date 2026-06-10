"""
Ejercicio 7: Grafo de conexiones entre los 5 equipos mejor clasificados.

Funciones:
    - graf: Genera un grafo de conexiones entre los 5 equipos con más
      puntos acumulados en La Liga (1995-2025).
"""
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import config


def graf(data: pd.DataFrame, selected_teams: list) -> str:
    """
    Genera un grafo de conexiones entre los equipos de la lista
    selected_teams, mostrando el número total de partidos disputados
    entre cada par de equipos como etiqueta de cada arista.

    Solo se consideran los partidos en que tanto el equipo local como
    el visitante pertenecen a selected_teams.

    Args:
        data (pd.DataFrame): Dataset de La Liga ya cargado y limpio.
        selected_teams (list): Lista con los nombres de los equipos
            a incluir en el grafo (se espera los 5 con más puntos).

    Returns:
        str: Ruta relativa donde se ha guardado la figura.
    """
    filtered = data[
        data["HomeTeam"].isin(selected_teams) &
        data["AwayTeam"].isin(selected_teams)
    ]

    graph = nx.Graph()
    graph.add_nodes_from(selected_teams)

    for i, team1 in enumerate(selected_teams):
        for team2 in selected_teams[i + 1:]:
            matches = len(filtered[
                ((filtered["HomeTeam"] == team1) & (filtered["AwayTeam"] == team2)) |
                ((filtered["HomeTeam"] == team2) & (filtered["AwayTeam"] == team1))
            ])
            if matches > 0:
                graph.add_edge(team1, team2, weight=matches)

    pos = nx.circular_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    node_colors = ["#FFD700", "#C0C0C0", "#CD7F32", "#4C72B0", "#DD8452"]

    _, ax = plt.subplots(figsize=(10, 8))

    nx.draw_networkx_nodes(
        graph, pos, ax=ax,
        node_color=node_colors,
        node_size=3000,
        alpha=0.95
    )
    nx.draw_networkx_labels(
        graph, pos, ax=ax,
        font_size=10,
        font_weight="bold"
    )
    nx.draw_networkx_edges(
        graph, pos, ax=ax,
        edge_color="#555555",
        width=1.8,
        alpha=0.7
    )
    nx.draw_networkx_edge_labels(
        graph, pos, ax=ax,
        edge_labels=edge_labels,
        font_size=9,
        font_color="#222222",
        bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "alpha": 0.7}
    )

    ax.set_title(
        "Grafo de conexiones: Top 5 equipos históricos (1995-2025)",
        fontsize=14, fontweight="bold", pad=20
    )
    ax.axis("off")
    plt.tight_layout()

    output_path = f"src/img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    return output_path
