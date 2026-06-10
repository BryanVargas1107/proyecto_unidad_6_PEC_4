# Análisis Histórico de La Liga Española (1995-2025)
### Proyecto Unidad 6 — PEC 4

**Autor:** Bryan Vargas  
**Asignatura:** Programación en Python  

---

## Descripción

Proyecto de análisis de datos históricos de la Liga Española de fútbol desde
la temporada 1995-96 hasta la 2025-26, desarrollado en Python con archivos `.py`
planos organizados en módulos. Incluye análisis exploratorio, distribución de
goles, clasificaciones históricas y visualizaciones gráficas.

---

## Estructura del proyecto

```
proyecto_unidad_6_PEC_4/
├── src/
│   ├── main.py               # Punto de entrada principal
│   ├── config.py             # Variables globales (autor, timestamp)
│   ├── data/
│   │   └── LaLiga_Matches.csv
│   ├── exercises/
│   │   ├── __init__.py
│   │   ├── ex1.py            # Carga del dataset y análisis exploratorio
│   │   ├── ex2.py            # Partidos totales jugados por equipo
│   │   ├── ex3.py            # Distribución de goles
│   │   ├── ex4.py            # Partidos ganados en casa/fuera/empate
│   │   ├── ex5.py            # Clasificación global 1995-2025
│   │   ├── ex6.py            # Dataframe summary y podium histórico
│   │   └── ex7.py            # Grafo de conexiones top 5 equipos
│   └── img/                  # Gráficas generadas
├── tests/
│   └── tests_ex6.py          # Tests unitarios de fun_total_goals
├── doc/                      # Documentación generada con pydoc
├── screenshots/              # Capturas de pantalla de autoría
├── .pylintrc                 # Configuración de Pylint
├── requirements.txt          # Dependencias del proyecto
├── LICENSE                   # Licencia MIT
└── README.md
```

---

## Instalación en un entorno virtual limpio

```bash
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activar el entorno
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3. Instalar las dependencias
pip install -r requirements.txt
```

---

## Ejecución del proyecto

Siempre desde la raíz del proyecto:

```bash
# Mostrar ayuda
python src/main.py --help

# Ejecutar un ejercicio específico (ejecuta todos los anteriores también)
python src/main.py -ex 1
python src/main.py -ex 3
python src/main.py -ex 7
```

El argumento `-ex N` ejecuta de forma incremental los ejercicios del 1 al N.

---

## Comprobación del análisis estático (Linting)

Se utiliza **Pylint** para el análisis estático del código.

```bash
# Analizar todo el proyecto
pylint src/

# Analizar un módulo específico
pylint src/exercises/ex1.py

# Analizar los tests
pylint tests/tests_ex6.py
```

La configuración personalizada se encuentra en `.pylintrc`.

---

## Generación de la documentación

Se utiliza **pydoc** para generar la documentación en HTML a partir de los docstrings.

```bash
# Situarse en la carpeta src/
cd src

# Generar los archivos HTML
python -m pydoc -w main config exercises.ex1 exercises.ex2 exercises.ex3 exercises.ex4 exercises.ex5 exercises.ex6 exercises.ex7

# Mover la documentación a la carpeta doc/
move *.html ..\doc\

# Volver a la raíz
cd ..
```

La documentación generada se encuentra en la carpeta `doc/`.

---

## Ejecución de los tests

Se utiliza el módulo **unittest** de la librería estándar de Python.

```bash
# Ejecutar los tests con detalle
python -m unittest tests/tests_ex6.py -v
```

Los tests comprueban el correcto funcionamiento de la función `fun_total_goals`
definida en el ejercicio 6.

---

## Subir el proyecto a GitHub

```bash
# Inicializar el repositorio (solo la primera vez)
git init
git remote add origin https://github.com/BryanVargas1107/proyecto_unidad_6_PEC_4.git

# Añadir cambios y hacer commit
git add .
git commit -m "descripción del cambio"

# Subir al repositorio remoto
git push -u origin main
```

---

## Notas

- Las gráficas se guardan automáticamente en `src/img/` al ejecutar el proyecto.
- El nombre del alumno y el timestamp se configuran en `src/config.py`.