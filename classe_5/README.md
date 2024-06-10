# (En cuanto al archivo main.py) Análisis de Notas de Alumnos

Este script de Python realiza un análisis de las notas de los alumnos, ajusta las notas, convierte las notas numéricas en calificaciones textuales y genera un informe en formato CSV.

## Descripción

El script realiza los siguientes pasos:
1. Ajusta las notas de los alumnos sumando 1 a cada nota, asegurándose de que no excedan 10.
2. Combina los nombres y apellidos de los alumnos para obtener los nombres completos.
3. Convierte las notas numéricas en calificaciones textuales según ciertos criterios.
4. Construye un informe con los nombres completos, las notas ajustadas y las calificaciones textuales.
5. Guarda el informe en formato CSV para su posterior análisis.

## Dependencias

El script utiliza la librería `pandas` para manejar los datos como un DataFrame de manera eficiente.

Se puede instalar la librería utilizando pip:

```sh
pip install pandas
```

# (En cuanto al archivo main2.py) Análisis de Datos de Canal de YouTube

Este script de Python realiza un análisis de datos de un canal de YouTube a partir de un archivo Excel, calcula estadísticas y guarda los resultados en un nuevo archivo Excel.

## Descripción

El script realiza los siguientes pasos:

1. Lee un archivo Excel que contiene datos del canal de YouTube.
2. Calcula el promedio de espectadores, comentarios y likes del canal.
3. Calcula las desviaciones absolutas y porcentuales de espectadores, comentarios y likes con respecto a los promedios.
4. Elimina columnas innecesarias del DataFrame.
5. Guarda el DataFrame modificado en un nuevo archivo Excel.

## Dependencias

El script utiliza la librería `pandas` para manipular los datos como DataFrames.

Puedes instalar la librería utilizando pip:

```sh
pip install pandas
