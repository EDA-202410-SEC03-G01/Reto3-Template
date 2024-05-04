"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
from datetime import datetime
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(size):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
    control = model.new_catalog(size)
    
    return control
    
    


# Funciones para la carga de datos

def load_data(control, size):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    load_jobs(control, size)
    load_skills(control, size)
    load_salary(control, size)
    load_jobs_id(control, size)
    

    return control

def load_jobs(control, size):
    """
    Carga los datos de los trabajos
    """
    
    jobs_file = cf.data_dir + size +"jobs.csv" # Selecciona el archivo con el porcentaje de datos a cargar S
    
    input_file = csv.DictReader(open(jobs_file, encoding='utf-8'),delimiter=";") # Obejto Iterador que permite leer el archivo
    
    for job in input_file:
        # 2022-04-14T17:24:00.000Z
        job['published_at'] = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        model.add_data(control, job)
        model.add_year(control, job)
        model.add_list(control, job)
    
def load_jobs_id(control, size):
    """
    Carga los datos de los trabajos
    """
    
    jobs_file = cf.data_dir + size +"jobs.csv" # Selecciona el archivo con el porcentaje de datos a cargar S
    
    input_file = csv.DictReader(open(jobs_file, encoding='utf-8'),delimiter=";") # Obejto Iterador que permite leer el archivo
    
    for job in input_file:
        job['published_at'] = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        model.add_id(control, job)
        model.add_req7_experticia(control, job)
        model.add_req7_habilidad(control, job)
        model.add_req7_ubicacion(control, job)
        model.add_city_workplace(control, job)
        
def load_skills(control, size):
    
    skills_file = cf.data_dir + size +"skills.csv" # Selecciona el archivo con el porcentaje de datos a cargar 
    input_file = csv.DictReader(open(skills_file, encoding='utf-8'),delimiter=";") # Obejto Iterador que permite leer el archivo
    
    for skill in input_file:
        model.add_skill(control, skill)
        
def load_salary(control, size):
    
    salary_file = cf.data_dir + size +"employments_types.csv" # Selecciona el archivo con el porcentaje de datos a cargar 
    input_file = csv.DictReader(open(salary_file, encoding='utf-8'),delimiter=";") # Obejto Iterador que permite leer el archivo
    for salary in input_file:
        model.add_salary(control, salary)
        model.add_id_salary(control, salary)

        

# Funciones de ordenamiento

def data(catalog):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    return model.data(catalog)

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, date_min, date_max):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    
    return model.req_1(control, date_min, date_max)


def req_2(control, salary_min, salary_max):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    return model.req_2(control, salary_min, salary_max)


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control, tipo_trabajo, ciudad, numero_ofertas):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    return model.req_4(control, tipo_trabajo, ciudad, numero_ofertas)


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control, tipo_propiedad, pais, ano):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    return model.req_7(control, tipo_propiedad, pais, ano)


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
