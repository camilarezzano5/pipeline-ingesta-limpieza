
import os


def cargar_parquet(datos, ruta_salida):
    """
    Guarda los datos transformados en formato Parquet.
    Crea la carpeta de salida si no existe.
    """

    try:
        # Crear carpeta de salida
        carpeta = os.path.dirname(ruta_salida)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        # Exportar a formato Parquet
        datos.to_parquet(
            ruta_salida,
            engine="pyarrow",
            index=False
        )

        print("Carga realizada correctamente.")
        print(f"Archivo generado: {ruta_salida}")
        print(f"Tamaño del archivo: {os.path.getsize(ruta_salida)} bytes")

    except Exception as error:
        print(f"Error durante la carga: {error}")
        raise
