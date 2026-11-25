
import pandas as pd
import re


def transformar_datos(datos):
    """
    Limpia y transforma los datos:
    - Normaliza nombres de columnas.
    - Elimina filas vacías.
    - Elimina duplicados.
    - Gestiona valores nulos.
    """

    datos = datos.copy()

    # 1. Normalizar nombres de columnas
    datos.columns = [
        re.sub(
            r"_+",
            "_",
            re.sub(r"[^a-zA-Z0-9]+", "_", str(col).strip().lower())
        ).strip("_")
        for col in datos.columns
    ]

    # 2. Eliminar filas completamente vacías
    datos = datos.dropna(how="all")

    # 3. Eliminar registros duplicados
    datos = datos.drop_duplicates()

    # 4. Gestionar valores nulos numéricos
    columnas_numericas = datos.select_dtypes(
        include="number"
    ).columns

    for columna in columnas_numericas:
        if datos[columna].isnull().any():
            mediana = datos[columna].median()

            if pd.notna(mediana):
                datos[columna] = (
                    datos[columna].astype("Float64").fillna(mediana)
                )

    # 5. Gestionar valores nulos de texto
    columnas_texto = datos.select_dtypes(
        include=["object", "string"]
    ).columns

    for columna in columnas_texto:
        datos[columna] = datos[columna].fillna("sin_dato")

    print("Transformación realizada correctamente.")
    print(f"Registros finales: {len(datos)}")
    print(f"Valores nulos restantes: {datos.isnull().sum().sum()}")

    return datos

