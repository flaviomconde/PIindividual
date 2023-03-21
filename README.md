# <h1 align="center"> **PROYECTO INDIVIDUAL MLOps de Plataformas de streaming**


### <h2 align="center"> *¡Bienvenidos a mi primer proyecto!* 
Partiendo del contesto del ciclo de vida de un proyecto de Machine Learning debemos contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.
En primer lugar, realice transformaciones específicas en los datos (ETL) para disponibilizarlos a través de endpoints accesibles mediante la API que fue desplegada en Render.
En segundo lugar, realice un proceso de EDA a los datos para armar un sistema de recomendacion de peliculas con machine learning.


# <h2 align="center"> **Etapas de proyecto**

## <h2 align="center"> Transformaciones
En el archivo ETL_EDA realizamos todos los puntos sugeridos por el cliente

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

Los valores nulos del campo rating deberán reemplazarse por el string “G” corresponde al maturity rating: “general for all audiences”

De haber fechas, deberán tener el formato AAAA-mm-dd

Los campos de texto deberán estar en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

## <h2 align="center"> Desarrollo API

**Funcion get_max_duration** : Busca la película con mayor duración con filtros de año, plataforma y tipo de duración. 

Para utilizarla deben indicar: 

*year*: solo acepta numeros enteros.

*duration_type*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)

*platform*: Dos opciones se escriben en minúscula (min, Season)


**Función get_score_count**: Busca y cuenta la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

Para utilizarla deben indicar: 

*year*: Solo acepta numeros enteros.

*score*: Acepta numeros enteros y con coma.

*platform*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)

**Función get_count_platform**: Busca y cuenta la cantidad de películas por plataforma. 

Para utilizarla deben indicar: 

*Platform*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)


**Función get_actor**: Busca al actor que más se repite según plataforma y año. 

Para utilizarla deben indicar: 

*Platform*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)

*Anio*: Solo acepta numeros enteros.

## <h2 align="center"> Deployment

El diployment fue realizado en Render [link](https://piindividual.onrender.com/docs)

## <h2 align="center"> Análisis exploratorio de los datos
El EDA nos permite familiarizarnos aún más con los datos, podemos conocer si hay errores, duplicados, valores faltantes, relaciones, entre otros. Uno de los problemas que me enfrenté al usar un dataset tan grande (1.5GB) es que mi computadora no tenia la suficiente capacidad, por lo que tuve que recurrir a tomar solo una muestra y así explorar las librerias especiales para el EDA, como son pandas profiling.
## <h2 align="center"> Sistema de recomendación
Para realizar una recomendación de una película, utilice un filtro colaborativo basado en SVD (Descomposción en Valores singulares), que sirve para reducir la dimensionalidad que para el caso de tanto volumen de datos, acorta los tiempos de procesamiento y la librerría Surprise que ayuda a aplicar los algoritmos de recomendadion.

Este enfoque colaborativo se basa en la idea de que los usuarios con gustos similares calificarán de manera similar las mismas películas.
sistema de recomnedacion con gradeo [link](http://127.0.0.1:7860/)
## <h2 align="center"> Video 
[link]()

## <h2 align="center"> Contacto
correo: flavio.conde92@gmail.com