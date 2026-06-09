"""
Módulo principal del proyecto de análisis histórico de La Liga (1995-2025).

Este fichero sirve como punto de entrada para ejecutar los diferentes ejercicios
de la práctica de forma incremental utilizando argumentos por línea de comandos.

Uso:
    python src/main.py -ex <numero>   Ejecuta los ejercicios del 1 al N
    python src/main.py --help         Muestra la ayuda
"""
import argparse
import sys
import os
import config
from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7  # pylint: disable=unused-import


def main():
    """
    Función principal que gestiona la línea de comandos y coordina
    la ejecución secuencial e incremental de los ejercicios de la PEC.
    """
    parser = argparse.ArgumentParser(
        description="Herramienta de análisis de datos históricos de La Liga (1995-2025).",
        epilog="Ejemplo: python src/main.py -ex 3  (ejecuta los ejercicios 1, 2 y 3)"
    )
    parser.add_argument(
        "-ex",
        type=int,
        choices=range(1, 8),
        metavar="N",
        help="Ejecutar de forma incremental los ejercicios del 1 al N (valores válidos: 1-7)."
    )

    args = parser.parse_args()

    if args.ex is None:
        parser.print_help()
        sys.exit(0)

    print(f"\nIniciando ejecución incremental hasta el Ejercicio {args.ex}...")
    print("=" * 60)

    if args.ex >= 1:
        print("\n[EX1] Ejercicio 1: Carga del dataset y análisis exploratorio")
        print("-" * 60)
        data_path = os.path.join(os.path.dirname(__file__), "data", "LaLiga_Matches.csv")
        data = ex1.load_and_eda(data_path)
        print(f"Primeras filas:\n{data.head()}\n")
        print(f"Últimas filas:\n{data.tail()}\n")
        print(f"Dimensiones: {data.shape[0]} filas x {data.shape[1]} columnas\n")
        print(f"Tipos de datos:\n{data.dtypes}\n")
        print(f"Estadísticas descriptivas:\n{data.describe()}\n")
        print(f"Valores nulos:\n{data.isnull().sum()}\n")
        img_path = ex1.plot_home_away_goals(data)
        print(f"Gráfica guardada en: {img_path}")

    if args.ex >= 2:
        print("\n[EX2] Ejercicio 2: Partidos totales jugados")
        print("-" * 60)
        matches_team_total = ex2.total_matches(data)
        print(f"Top 10 equipos con más partidos:\n{matches_team_total.head(10)}\n")
        max_val = matches_team_total["total_matches"].max()
        always_first = matches_team_total[
            matches_team_total["total_matches"] == max_val
        ]
        print(f"Equipos siempre en Primera División:\n{always_first}\n")
        img_path = ex2.plot_matches_team_total(matches_team_total)
        print(f"Gráfica guardada en: {img_path}")

    if args.ex >= 3:
        print("\n[EX3] Ejercicio 3: Distribución de goles")
        print("-" * 60)
        distr_goals_home, distr_goals_away = ex3.goals_distribution(data)
        print(f"Distribución goles local:\n{distr_goals_home}\n")
        print(f"Distribución goles visitante:\n{distr_goals_away}\n")
        img_path = ex3.plot_goals_distribution(distr_goals_home, distr_goals_away)
        print(f"Gráfica guardada en: {img_path}")

    if args.ex >= 4:
        print("\n[EX4] Ejercicio 4: Partidos ganados en casa/fuera")
        print("-" * 60)
        ftr_df = ex4.FTR(data)
        print(f"Conteo de resultados (H, A, D):\n{ftr_df}\n")
        total = ftr_df["Matches"].sum()
        home_wins = ftr_df.loc["H", "Matches"]
        print(f"Los equipos locales ganan el {(home_wins / total) * 100:.2f}% de los partidos.\n")
        img_path = ex4.plot_FTR(ftr_df)
        print(f"Gráfica guardada en: {img_path}")

    if args.ex >= 5:
        print("\n[EX5] Ejercicio 5")
        print("-" * 60)
        # resultado = ex5.nombre_funcion()
        # print(resultado)

    if args.ex >= 6:
        print("\n[EX6] Ejercicio 6")
        print("-" * 60)
        # resultado = ex6.fun_total_goals()
        # print(resultado)

    if args.ex >= 7:
        print("\n[EX7] Ejercicio 7")
        print("-" * 60)
        # resultado = ex7.nombre_funcion()
        # print(resultado)

    print("\n" + "=" * 60)
    print("Ejecución incremental finalizada con éxito.")


if __name__ == "__main__":
    main()
    