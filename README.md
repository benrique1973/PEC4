# Análisis de Datos de TMDB
Este proyecto analiza datos de series de televisión de The Movie Database (TMDB) para ayudar a Open Broadcast Corporation en la toma de decisiones sobre adquisiciones de licencias de emisión.

## Descripción

El proyecto consta de varios módulos que permiten descomprimir archivos, leer y procesar datos de series de televisión, filtrar estos datos según varios criterios y visualizar los resultados a través de gráficos. El análisis se centra en identificar tendencias y patrones que puedan ser útiles para la toma de decisiones en el ámbito de los medios de comunicación.

## Requisitos

Para ejecutar este proyecto, necesitarás Python instalado en tu sistema. Este proyecto ha sido probado en Python 3.8. Además, se requieren las siguientes bibliotecas:

pandas
matplotlib

## Instalación

# Guía de instalacion

Ubicarse en la carpeta del proyecto ('PEC4')

## Crear un Entorno Virtual

Abrir la Terminal o CMD: Primero, abre tu terminal (en Linux) o CMD/powershell (en Windows).

Navegar al Directorio del Proyecto: Usa el comando cd para ir al directorio donde está o estará tu proyecto.

#### En windows

```bash

cd ruta/a/tu/PEC4

python -m venv venv

```

#### En Linux

```bash

cd ruta/a/tu/PEC4

python -m venv venv

```

## Activar el Entorno Virtual

Una vez que has creado tu entorno virtual, debes activarlo:

### En Windows en ventana CMD:

```bash

.\venv\Scripts\activate

```

### En Linux:

```bash
source venv/bin/activate
```

Cuando el entorno virtual esté activo, verá el nombre del entorno virtual (en este caso, venv) al principio de la línea de comandos.

### Instalacion de requerimientos

#### En Windows

```bash

pip install -r requirements.txt

```

#### En Linux

```bash

pip install -r requirements.txt

```

## Ejecutar el script

Para ejecutar tu script de Python, usa el comando python seguido del nombre del archivo. 

```bash

python main.py

```
Una vez corrido, seleccionar la opción que desee utilizar
Puede correrlo linelamente o por cada opción, en este último caso
el programa ejecutara los pasos previos (por lo que puede tardar mas)

# Ejecución de Tests

Este proyecto incluye una suite de tests para asegurar que los módulos funcionan correctamente. Para ejecutar los tests, sigue estos pasos:

1. Asegúrate de estar en el directorio raíz del proyecto.
2. Ejecuta el siguiente comando en tu terminal:

```bash

python -m unittest discover -s tests

```

Este comando buscará y ejecutará todos los tests definidos en el directorio `tests`. Asegúrate de que todos los tests se ejecuten correctamente para validar la funcionalidad del código.

## Ejecución del Programa

Para ejecutar el programa principal, navega a la carpeta del proyecto y ejecuta:

```bash

python main.py

```

##  Uso

Para ejecutar el programa principal, navega a la carpeta del proyecto y ejecuta:

```bash

python main.py

```
Puede ejecutar toda la tarea solicitada desde ese menú, seleccionando la opción deseada y proporcionando los insumos mínimos

En caso de no desarrollarse de forma secuencial (que es lo ideal), las funciones y procedimientos se ha hecho usando los insumos minimos colocados en la carpeta 'Data' dentro del proyecto

En la carpeta 'Datos', se guarda el resultado de todos los procedimientos con un nombre que facilita su identificacion

Si lo desea puede correr de forma independiente cada módulo, segun se describe en cada sección

Sigue las instrucciones en pantalla para navegar por las diferentes opciones del menú.

## Estructura del Proyecto

El proyecto está organizado en varios módulos, cada uno con funciones específicas relacionadas con la gestión, procesamiento, filtrado y visualización de datos. Además, main.py es el script principal que ejecuta la aplicación.

data_management.py: Funciones para descomprimir archivos y leer datos.
data_processing.py: Funciones para procesar y manipular datos.
data_filtering.py: Funciones para filtrar datos según varios criterios.
data_visualization.py: Funciones para visualizar datos a través de gráficos.
main.py: Script principal que ejecuta la aplicación.

### Módulo data_management.py

#### Descripción

El módulo data_management.py contiene funciones esenciales para la gestión de datos en el proyecto TMDB Data Analysis. Este módulo se encarga de la descompresión de archivos, la lectura y combinación de datos CSV, y la comparación de tiempos de procesamiento entre diferentes métodos de lectura de datos.

#### Funcionalidades

El módulo incluye las siguientes funciones principales:

ejercicio_1_1(filepath): Descomprime archivos .zip o .tar.gz en una carpeta específica.
ejercicio_1_2(): Lee y combina archivos CSV en un único DataFrame utilizando Pandas.
ejercicio_1_3(): Realiza una tarea similar a ejercicio_1_2, pero utilizando la librería CSV de Python.
ejercicio_1_4(tiempo_pandas, tiempo_csv): Compara los tiempos de procesamiento entre Pandas y CSV.

#### Uso

Para utilizar las funciones de este módulo, primero importa el módulo en tu script de Python:

from tmdb.data_management import ejercicio_1_1, ejercicio_1_2, ejercicio_1_3, ejercicio_1_4

A continuación, puedes llamar a las funciones según sea necesario. Por ejemplo:

###### Descomprimir un archivo

resultado_descompresion = ejercicio_1_1('path/al/archivo.zip')

###### Combinar archivos CSV usando Pandas

df_combinado, tiempo_procesamiento = ejercicio_1_2()

###### Combinar archivos CSV usando la librería CSV

df_combinado_csv, tiempo_procesamiento_csv = ejercicio_1_3()

###### Comparar tiempos de procesamiento

analisis_tiempo = ejercicio_1_4(tiempo_procesamiento, tiempo_procesamiento_csv)

### Módulo de Procesamiento de Datos (data_processing.py)

Este módulo contiene funciones para procesar y analizar datos de series de televisión. Las funciones principales incluyen la adición de una nueva columna al DataFrame y la manipulación de fechas.

#### Funciones Principales

ejercicio_2_1_pandas(df=None):

Descripción: Añade una columna air_days al DataFrame, que representa el número de días que una serie ha estado en emisión. Si el DataFrame proporcionado está vacío o es None, carga los datos desde un archivo CSV predeterminado.

#### Uso

```bash

import pandas as pd
from data_processing import ejercicio_2_1_pandas

# Cargar DataFrame existente o usar None para cargar desde archivo

df = pd.DataFrame()  # o df = None

resultado = ejercicio_2_1_pandas(df)

```

#### Ejemplo de uso

```bash

import pandas as pd
from data_processing import ejercicio_2_1_pandas, ejercicio_2_1_csv

# Ejemplo de uso de ejercicio_2_1_pandas

df_pandas = pd.DataFrame()  # Suponiendo que df_pandas es tu DataFrame
resultado_pandas = ejercicio_2_1_pandas(df_pandas)

# Ejemplo de uso de ejercicio_2_1_csv

df_csv = None  # Suponiendo que no tienes un DataFrame y quieres cargar desde un archivo
resultado_csv = ejercicio_2_1_csv(df_csv)

```

### Módulo de Filtrado de Datos (data_filtering.py)

Este módulo data_filtering.py forma parte del proyecto de análisis de datos de TMDB (The Movie Database). Proporciona funcionalidades para filtrar datos de series de televisión según varios criterios específicos.

#### Funciones

El módulo incluye las siguientes funciones:

ejercicio_3_1(df): Filtra y muestra los nombres de las series en inglés que contienen las palabras 'mystery' o 'crime' en su resumen.

ejercicio_3_2(df): Filtra y muestra los nombres de las series que comenzaron en 2023 y fueron canceladas.

ejercicio_3_3(df): Filtra y muestra las series cuyo idioma incluye el japonés.

Cada función acepta un DataFrame de Pandas como argumento y devuelve un DataFrame filtrado.

#### Uso

Para utilizar estas funciones, primero importe el módulo y luego pase un DataFrame de Pandas como argumento. A continuación, se muestra un ejemplo de cómo utilizar la función ejercicio_3_1:

```bash

from tmdb.data_filtering import ejercicio_3_1

# Suponiendo que df es un DataFrame de Pandas con los datos de las series

df_filtrado = ejercicio_3_1(df)

```

### Data Visualization Module

Este módulo data_visualization.py forma parte del proyecto de análisis de datos de TMDB (The Movie Database). Proporciona funcionalidades para visualizar diferentes aspectos de los datos de series de televisión, como la distribución de series por año, por tipo y por género.

#### Uso

El módulo data_visualization.py contiene las siguientes funciones principales:


grafico_series_por_año(df): Muestra un gráfico de barras del número de series por año de inicio.
grafico_series_por_tipo_y_decada(df): Muestra un gráfico de líneas del número de series por categoría de 'type' desde 1940.
grafico_series_por_genero(df): Muestra un gráfico circular del número de series por género.

#### Ejemplos

Aquí hay algunos ejemplos de cómo utilizar estas funciones:

```bash

import pandas as pd
from data_visualization import grafico_series_por_año, grafico_series_por_tipo_y_decada, grafico_series_por_genero

# Suponiendo que df es un DataFrame de Pandas con los datos de las series

df = pd.DataFrame() # Reemplazar con la carga de su DataFrame

# Visualizar el número de series por año

grafico_series_por_año(df)

# Visualizar el número de series por tipo y década

grafico_series_por_tipo_y_decada(df)

# Visualizar el número de series por género

grafico_series_por_genero(df)

```

## Tests

Para ejecutar los tests, usa el siguiente comando:

```bash

python -m unittest

```

## Ejecución de Tests

Este proyecto incluye una suite de tests para asegurar que los módulos funcionan correctamente. Para ejecutar los tests, sigue estos pasos:

1. Asegúrate de estar en el directorio raíz del proyecto.
2. Ejecuta el siguiente comando en tu terminal:

```bash

python -m unittest discover -s tests

```

Este comando buscará y ejecutará todos los tests definidos en el directorio `tests`. Asegúrate de que todos los tests se ejecuten correctamente para validar la funcionalidad del código.

### Pruebas para el Módulo de Gestión de Datos

El archivo test_data_management.py contiene pruebas unitarias para asegurar el correcto funcionamiento de las funciones en data_management.py.

#### Ejecutar Pruebas

Para ejecutar las pruebas, necesitarás tener Python y unittest instalados. Puedes ejecutar las pruebas con el siguiente comando:

```bash

python -m unittest test_data_management.py

```
Este comando ejecutará todas las pruebas definidas en test_data_management.py y mostrará los resultados en la consola.


### Pruebas para el Módulo de Procesamiento de Datos

El archivo test_data_processing.py contiene pruebas unitarias para asegurar el correcto funcionamiento de las funciones en data_processing.py.

#### Ejecutar Pruebas

Para ejecutar las pruebas, necesitarás tener Python y unittest instalados. Puedes ejecutar las pruebas con el siguiente comando:

```bash

python -m unittest test_data_processing.py

```
Este comando ejecutará todas las pruebas definidas en test_data_processing.py y mostrará los resultados en la consola.

#### Pruebas Incluidas

test_ejercicio_2_1_pandas_con_df_vacio: Verifica que ejercicio_2_1_pandas funcione correctamente con un DataFrame vacío.
test_ejercicio_2_1_pandas_con_df_none: Verifica que ejercicio_2_1_pandas funcione correctamente con None como argumento.
test_ejercicio_2_1_csv_con_df_vacio: Verifica que ejercicio_2_1_csv funcione correctamente con un DataFrame vacío.
test_ejercicio_2_1_csv_con_df_none: Verifica que ejercicio_2_1_csv funcione correctamente con None como argumento.


### Pruebas para Módulo de Filtrado de Datos (test_data_filtering.py)

Este archivo contiene pruebas unitarias para las funciones definidas en data_filtering.py. Se utilizan para asegurar que las funciones de filtrado funcionen como se espera.

#### Ejecución de Pruebas

Para ejecutar estas pruebas, use el siguiente comando:

```bash

python -m unittest test_data_filtering.py

```
### Test Suite para Data Visualization Module

Este archivo test_data_visualization.py contiene las pruebas unitarias para el módulo data_visualization.py del proyecto de análisis de datos de TMDB.

#### Ejecución de Tests

Para ejecutar estos tests, necesitarás tener instalado Python y las dependencias especificadas en requirements.txt. Puedes ejecutar los tests utilizando el siguiente comando en tu terminal:

```bash

python -m unittest test_data_visualization.py

```
#### Descripción de Tests

test_ejercicio_4_1: Verifica la correcta funcionalidad de la función que genera el gráfico de barras del número de series por año de inicio.
test_ejercicio_4_2: Comprueba la generación del gráfico de líneas del número de series por categoría de 'type' desde 1940.
test_ejercicio_4_3: Asegura que el gráfico circular del número de series por género se genere correctamente.

## Licencia

Este proyecto se distribuye bajo lMIT License. Consulta el archivo LICENSE para más detalles.

# Autores 

Autor : Balmore Enrique López Ramírez
Desarrollo asistido por ChatGPT de OpenAI
