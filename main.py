
from src.extraccion import extraer_datos
from src.transformacion import transformar_datos
from src.carga import cargar_parquet


def main():
    print("Iniciando pipeline ETL...")

    # 1. Extracción
    datos = extraer_datos("datos/ventas.csv")
    print(f"Datos extraídos: {len(datos)} registros")

    # 2. Transformación
    datos_limpios = transformar_datos(datos)
    print(f"Datos después de la limpieza: {len(datos_limpios)} registros")

    # 3. Carga
    cargar_parquet(datos_limpios, "output/ventas_limpias.parquet")

    print("Pipeline ETL finalizado correctamente.")


if __name__ == "__main__":
    main()
