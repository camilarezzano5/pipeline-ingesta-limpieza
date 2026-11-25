
import pandas as pd


def extraer_datos(ruta):
    """
    Lee un archivo CSV y devuelve un DataFrame.
    Optimiza los tipos de datos para reducir memoria.
    """

    try:
        datos = pd.read_csv(
            ruta,
            low_memory=False
        )

        # Optimización de tipos de datos
        datos = datos.convert_dtypes()

        print("Extracción realizada correctamente.")
        print(f"Cantidad de registros: {len(datos)}")
        print(f"Cantidad de columnas: {len(datos.columns)}")

        return datos

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {ruta}")
        raise

    except Exception as error:
        print(f"Error durante la extracción: {error}")
        raise
