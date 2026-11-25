
# Pipeline de Ingesta y Limpieza de Datos

## Descripción del proyecto

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) utilizando Python y Pandas para automatizar la extracción, transformación y carga de datos.

El objetivo es optimizar el procesamiento de datos mediante una estructura modular y generar archivos en formato Parquet.

## Tecnologías utilizadas

- Python
- Pandas
- PyArrow
- OpenPyXL

## Estructura del proyecto

```text
pipeline-ingesta-limpieza/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── __init__.py
    ├── extraccion.py
    ├── transformacion.py
    └── carga.py
```

## Etapas del pipeline

### 1. Extracción

Se utiliza Pandas para leer los archivos CSV y cargar los datos en un DataFrame.

### 2. Transformación

Se realizan las siguientes tareas:

- Normalización de nombres de columnas.
- Eliminación de filas completamente vacías.
- Eliminación de registros duplicados.
- Tratamiento de valores nulos numéricos mediante la mediana.
- Tratamiento de valores nulos de texto mediante la categoría "sin_dato".

### 3. Carga

Los datos procesados se exportan a formato Parquet mediante PyArrow.

Este formato permite una lectura eficiente, compresión y almacenamiento columnar, facilitando su utilización en proyectos de Machine Learning.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/camilarezzano5/pipeline-ingesta-limpieza.git
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar el siguiente comando desde la carpeta principal:

```bash
python main.py
```

## Resultado esperado

El pipeline genera un archivo Parquet con los datos procesados en la carpeta output.

## Autora

Camila Rezzano
