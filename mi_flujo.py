"""Flujo de ETL : Permito extraer, cargar y transformar archivos.
Integrantes: Darwin Padilla
Fuente: Datos Sintéticos
SI FALLA: ___ (que pasa si la fuente no llega o cambia, y A QUIEN habria que avisar)"""
import logging, sys
from datetime import date
import pandas as pd

# ---------- 1 · PARAMETROS (todo lo que puede cambiar, junto y arriba) ----------
RUTA_ENTRADA    = "datos/exportaciones.csv"
SALIDA          = f"salida/mi_flujo_{date.today().isoformat()}.csv"
FILAS_ESPERADAS = 6
TOTAL_ESPERADO     = 8679.13
# agregue aqui otro parametro de comprobacion, por ejemplo un total esperado

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.FileHandler("flujo.log"), logging.StreamHandler()])
log = logging.getLogger("mi_flujo")

# ---------- 2 · LAS TRES FUNCIONES (cada una con su docstring) ----------
def extraer():
    """Permite importar la información en el desde el csv"""
    tabla = pd.read_csv(RUTA_ENTRADA)
    log.info("extraidas %d filas", len(tabla))
    return tabla

def transformar(tabla):
    """Crea una columna llamada filas esperadas mediante cálculos"""
    if len(tabla) != FILAS_ESPERADAS:
        raise ValueError(f"esperaba {FILAS_ESPERADAS} filas y llegaron {len(tabla)}")
    # AQUI: su transformacion y SU comprobacion que detiene (otro raise).
    return tabla

def cargar(tabla):
    """Coloca los datos calculados en una tabla """
    import os; os.makedirs("salida", exist_ok=True)
    tabla.to_csv(SALIDA, index=False)
    log.info("guardado %s (%d filas)", SALIDA, len(tabla))

# ---------- 3 · LA LOGICA, EN ORDEN ----------
if __name__ == "__main__":
    try:
        cargar(transformar(extraer())); log.info("FIN OK")
    except Exception as error:
        log.error("EL FLUJO FALLO: %s", error); sys.exit(1)
