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
        print("\n[EX1] Ejercicio 1")
        print("-" * 60)
        # resultado = ex1.nombre_funcion()
        # print(resultado)

    if args.ex >= 2:
        print("\n[EX2] Ejercicio 2")
        print("-" * 60)
        # resultado = ex2.nombre_funcion()
        # print(resultado)

    if args.ex >= 3:
        print("\n[EX3] Ejercicio 3")
        print("-" * 60)
        # resultado = ex3.nombre_funcion()
        # print(resultado)

    if args.ex >= 4:
        print("\n[EX4] Ejercicio 4")
        print("-" * 60)
        # resultado = ex4.nombre_funcion()
        # print(resultado)

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
    