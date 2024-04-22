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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from tabulate import tabulate
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_catalog(size):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    
    control = {
        'tree_by_date' : None,
        'map_skills' : None,
    }
    
    
    control['map_skills'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['tree_by_date'] = om.newMap(omaptype='RBT', cmpfunction=compare_dates)
    
    return control
    


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    catalog = data_structs
    
    catalog = add_date(catalog, data)

    
    return catalog

def add_skill(catalog, data):
    
    map_skills = catalog['map_skills']
    
    key = data['id']
    
    entry = mp.get(map_skills, key)
    
    if entry is None:
        entry = new_skills_entry(data)
        lt.addLast(entry['skills'], data)
        mp.put(map_skills, key, entry)
    else:
        entry = entry["value"]
        lt.addLast(entry['skills'], data)
    
    return catalog

    
def add_date(catalog, data):
    
    
    tree_date = catalog['tree_by_date']
    
    key = key_day(data['published_at'])
    
    key_value =  om.get(tree_date, key)
    
    if key_value is None:
        entry = new_date_entry(data['published_at'])
        lt.addLast(entry['data'], data)
        
        om.put(tree_date, key, entry)
    else:
        entry = me.getValue(key_value)
        lt.addLast(entry['data'], data)

    return catalog

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def new_date_entry(date):
    
    entry = {
        'date' : date,
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    
    return entry
def new_skills_entry(data):

    entry = {
        'id' : data['id'],
        'skills' : lt.newList(datastructure='ARRAY_LIST')
    }
    
    return entry
    


def key_day(date):
    """
    Función que retorna la clave de un día
    """
    
    day = date.day
    month = date.month
    year = date.year
    
    key = datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    
    return key

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(catalog, date_min, date_max):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    answer_list = lt.newList(datastructure='ARRAY_LIST')    
    
    date_min = datetime.strptime(date_min, '%Y-%m-%d')
    date_max = datetime.strptime(date_max, '%Y-%m-%d')
    
    tree_date = catalog['tree_by_date']
    
    values = om.values(tree_date, date_min, date_max)
    
    for value in lt.iterator(values):
        data_value = value['data']
        
        for job in lt.iterator(data_value):
            job = search_skills(catalog, job)
            lt.addLast(answer_list, job)

    merg.sort(answer_list, sort_by_date)
    
    size = lt.size(answer_list)    
    answer_list = first_and_last(answer_list)
    table = tabulate_rq1(answer_list)
    return size, table

def search_skills(catalog, job):
    
    id = job["id"]
    map_skills = catalog["map_skills"]
    my_skills = []
    info_skills = mp.get(map_skills, id)
    
    if info_skills is not None:
        value_skills = info_skills["value"]
        list_skills = value_skills["skills"]
        for skill in lt.iterator(list_skills):
            my_skills.append(skill["name"])
    
    job["skills"] = my_skills
    
    return job

def first_and_last(list):
    
    first_five = lt.subList(list, 1, 5)
    last_five = lt.subList(list, lt.size(list) - 5, 5)
    
    answer = lt.newList(datastructure="ARRAY_LIST")
    
    for element in lt.iterator(first_five):
        lt.addLast(answer, element)
    for element in lt.iterator(last_five):
        lt.addLast(answer, element)
        
    return answer

def tabulate_rq1(data):
    
    headers = ['Fecha', 'Titulo', 'Company_Name',  "Skills"]
    table = []
    for job in lt.iterator(data):
        row = []
        row.append(job["published_at"])
        row.append(job["title"])
        row.append(job["company_name"])
        row.append(job["skills"])
        table.append(row)
        
    return tabulate(table, headers=headers, tablefmt="grid")


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def compare_dates(data_1, data_2):
    """
    Función encargada de comparar dos fechas
    """
    
    if data_1 == data_2:
        return 0
    elif data_1 > data_2:
        return 1
    else:
        return -1


# Funciones de ordenamiento
def sort_by_date(data_1, data_2):
    
    return data_1['published_at'] > data_2['published_at']


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
