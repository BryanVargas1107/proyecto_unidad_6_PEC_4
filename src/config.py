"""
Configuración global del proyecto.

Variables globales utilizadas en todos los módulos para identificar
al autor y registrar el momento de generación de los ficheros.
"""
from datetime import datetime

nom_alumne: str = "Bryan Vargas"
date_time: str = datetime.now().strftime('%Y%m%d_%H%M%S')
