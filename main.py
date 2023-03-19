from fastapi import FastAPI  
import pandas as pd
import numpy as np
from collections import Counter
#traemos el dataset a utilizar
data = pd.read_csv(r'Dataset/total_plataformas.csv')

#creamos app
app = FastAPI()

#http://127.0.0.1:8000 puerto de la fastapi

#creamos la ruta
@app.get('/')
#creamos funcion
def get_bienvenida():
    return 'hola, Soy Flavio y este es mi PI individual de consultas de plataformas'

# Pelicul;as con mayor duracion con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. 
@app.get('/max_duration')
def get_max_duration1(year:int,duration_type:str, platform:str):
    df_new = data[(data['release_year'] == year) &  (data['duration_type'] == duration_type) & (data['platform'] == platform)]
    df_new = df_new.loc[df_new['duration_int'] == df_new['duration_int'].max()]
    name = df_new['title']
    return name

@app.get('/cantidad_pelicula')
def get_score_count (platform:str,score:float,year:int):
    df_new = data[(data['platform'] == platform) &  (data['score'] > score) & (data['release_year'] == year)]
    cantidad = df_new.shape[0]
    return cantidad


@app.get('/cantidad_plataforma/{plataform}')
def get_count_platform(platform:str):
    df_new = data[(data['platform'] == platform)]
    cantidad = df_new.shape[0]
    return cantidad

@app.get('/actor_mas_repite')
def get_actor(platform:str, anio:int):
    result = data[(data['platform']==platform) & (data['release_year']==anio)]
    
    lista=[]
    result = result['cast'].dropna()
    for i in result:
        if i != 'sin dato':
             l= [elemento.strip() for elemento in i.split(',')]
             lista+=l

    mas_frecuentes = Counter(lista).most_common()
    return mas_frecuentes[0][0]




