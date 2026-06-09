"""
Ejercicio 5: Clasificación global de La Liga (1995-2025).
"""
import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Añade al dataset las columnas 'points_home' y 'points_away',
    asignando 3, 1 o 0 puntos en función del resultado del partido (FTR).

    Args:
        data (pandas.DataFrame): Dataset de La Liga.

    Returns:
        pandas.DataFrame: Nuevo DataFrame con las dos columnas añadidas.
    """
    df = data.copy()

    df["points_home"] = df["FTR"].map({"H": 3, "D": 1, "A": 0})
    df["points_away"] = df["FTR"].map({"H": 0, "D": 1, "A": 3})

    return df


def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """
    Calcula el total de puntos conseguidos y acumulados desde 1995
    por cada equipo.

    Args:
        data (pandas.DataFrame): Dataset que ya contiene las columnas de puntos.

    Returns:
        tuple: (pd.Series, pd.DataFrame) con la misma información de los
            puntos totales ordenados de mayor a menor.
    """
    home_pts = data.groupby("HomeTeam")["points_home"].sum()
    away_pts = data.groupby("AwayTeam")["points_away"].sum()

    # Sumamos los puntos como local y visitante
    series_total_points = (
        home_pts.add(away_pts, fill_value=0)
        .astype(int)
        .sort_values(ascending=False)
        .rename_axis("Team")
        .rename("Total_Points")
    )

    # Convertir la Series en DataFrame
    df_total_points = series_total_points.to_frame()

    return series_total_points, df_total_points


def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """
    Devuelve el equipo que ha acumulado más puntos históricamente.

    Args:
        df_total_points (pandas.DataFrame): Clasificación histórica.

    Returns:
        str: Nombre del equipo ganador.
    """
    return df_total_points.index[0]
