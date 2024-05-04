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

import numpy as np
import matplotlib.pyplot as plt
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
import csv
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
        'tree_by_salary': None,
        'map_id': None,
        "tree_by_workplace_type" : None,
        "map_year" : None,
        "map_salary" : None,
        "lista_jobs" : None,
    }
    
    control['lista_jobs'] = lt.newList(datastructure='ARRAY_LIST')

    control['map_year'] =  mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)

    control['map_skills'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['map_req7_habilidades'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['map_req7_experticia'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['map_req7_ubicacion'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['map_id'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['map_city_workplace'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['map_salary'] = mp.newMap(numelements=50000, maptype='PROBING', loadfactor=0.5)
    
    control['tree_by_date'] = om.newMap(omaptype='RBT', cmpfunction=compare_dates)
    
    control['tree_by_salary'] = om.newMap(omaptype='RBT', cmpfunction=compare_salary)
    
    control['tree_by_workplace_type'] = om.newMap(omaptype='RBT', cmpfunction=compare_workplace)
    
    
    return control
    


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    catalog = data_structs
    
    catalog = add_date(catalog, data)

    
    return catalog


def add_list(catalog, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    answer = catalog["lista_jobs"]
    lt.addLast(answer, data)
    
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


def add_year(catalog, data):
    
    map_skills = catalog['map_year']
    
    key = key_day_ano(data["published_at"])
    entry = mp.get(map_skills, key)
    
    if entry is None:
        entry = new_date_entry(key)
        lt.addLast(entry['data'], data)
        mp.put(map_skills, key, entry)
    else:
        entry = entry["value"]
        lt.addLast(entry['data'], data)
    
    return catalog

def add_id_salary(catalog, data):
    
    map_skills = catalog['map_salary']
    
    key = data['id']
    
    entry = mp.get(map_skills, key)
    
    if entry is None:
        entry = new_map_salary_entry(data)
        lt.addLast(entry['data'], data)
        mp.put(map_skills, key, entry)
    else:
        entry = entry["value"]
        lt.addLast(entry['data'], data)
    
    return catalog

def add_city_workplace(catalog, data):
    
    map_city = catalog['map_city_workplace']
    
    key = data['city']+"_"+data['workplace_type']
    
    entry = mp.get(map_city, key)
    
    if entry is None:
        entry = new_city_workplace_entry(data)
        lt.addLast(entry['data'], data)
        mp.put(map_city, key, entry)
    else:
        entry = entry["value"]
        lt.addLast(entry['data'], data)
    
    return catalog


def add_id(catalog, data):
    
    map_id = catalog['map_id']
    
    key = data['id']
    
    entry = mp.get(map_id, key)
    
    if entry is None:
        entry = new_id_entry(data)
        lt.addLast(entry['data'], data)
        mp.put(map_id, key, entry)
    else:
        entry = entry["value"]
        lt.addLast(entry['data'], data)
    
    return catalog



def add_salary(catalog, data):
    
    tree_by_city = catalog['tree_by_salary']
    
    key = data['id']
    
    entry = mp.get(tree_by_city, key)
    
    if entry is None:
        entry = new_salary_entry(data)
        lt.addLast(entry['salary'], data)
        mp.put(tree_by_city, key, entry)
    else:
        entry = entry["value"]
        lt.addLast(entry['salary'], data)
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

def add_workplace(catalog, data):
    
    
    tree_workplace_type = catalog['tree_by_workplace_type']
    
    key = data["workplace_type"]
    key_value =  om.get(tree_workplace_type, key)
    if key_value is None:
        entry = new_workplace_entry(data['workplace_type'])
        lt.addLast(entry['data'], data)
        
        om.put(tree_workplace_type, key, entry)
    else:
        entry = me.getValue(key_value)
        lt.addLast(entry['data'], data)

    return catalog

def add_req7_experticia(catalog, data):
    
    
    map_req7 = catalog['map_req7_experticia']

    ano=  key_day_ano(data['published_at'])
    
    key = str(ano)+"_"+data["country_code"]+"_"+data["experience_level"]
    
    key_value =  om.get(map_req7, key)
 
    if key_value is None:
        entry = new_req7_entry(key)
        lt.addLast(entry['data'], data)
        
        om.put(map_req7, key, entry)
    else:
        entry = me.getValue(key_value)
        lt.addLast(entry['data'], data)

    return catalog

def add_req7_ubicacion(catalog, data):
    
    
    map_req7 = catalog['map_req7_ubicacion']

    ano=  key_day_ano(data['published_at'])
    key = str(ano)+"_"+data["country_code"]+"_"+data["workplace_type"]
    
    key_value =  om.get(map_req7, key)
   
    if key_value is None:
        entry = new_req7_entry(key)
        lt.addLast(entry['data'], data)
        
        om.put(map_req7, key, entry)
    else:
        entry = me.getValue(key_value)
        lt.addLast(entry['data'], data)

    return catalog

def add_req7_habilidad(catalog, data):
    
    
    map_req7 = catalog['map_req7_habilidades']

    ano=  key_day_ano(data["published_at"])
    habilidades = search_skills(catalog, data)
    for i in habilidades["skills"]:
        key = str(ano)+"_"+data["country_code"]+"_"+str(i)
        key_value =  om.get(map_req7, key)
        if key_value is None:
            entry = new_req7_entry(key)
            lt.addLast(entry['data'], data)
            
            om.put(map_req7, key, entry)
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

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def new_req7_entry(date):
    
    entry = {
        'key' : date,
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    return entry

def new_date_entry(date):
    
    entry = {
        'date' : date,
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    return entry
def new_workplace_entry(date):
    
    entry = {
        'workplace_type' : date,
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    
def new_map_salary_entry(date):
    
    entry = {
        'id' : date["id"],
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    
    return entry
def new_skills_entry(data):

    entry = {
        'id' : data['id'],
        'skills' : lt.newList(datastructure='ARRAY_LIST')
    }
    
    return entry

def new_city_workplace_entry(data):

    entry = {
        'city_workplace' : data['city']+"_"+data["workplace_type"],
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    
    return entry

def new_id_entry(data):

    entry = {
        'id' : data['id'],
        'data' : lt.newList(datastructure='ARRAY_LIST')
    }
    
    return entry
    
    
def new_salary_entry(data):

    entry = {
        'id' : data['id'],
        'salary' : lt.newList(datastructure='ARRAY_LIST')
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

def key_day_ano(date):
    """
    Función que retorna la clave de un día
    """
    
    key = date.year

    
    return key

# Funciones de consulta

def get_data(data_structs, id):
    """9
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una list
    pass

def data(catalog):
    answer = catalog["lista_jobs"]
    size_list = answer
    answer = merg.sort(answer, sort_by_date)
    answer = first_and_last_three(answer)
    lista = lt.newList(datastructure="ARRAY_LIST")
    for job in lt.iterator(answer):
        job = search_skills(catalog, job)
        lt.addLast(lista, job)
    size = lt.size(size_list)
    table = tabulate_data(lista)
    return size, table

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

def req_2(catalog, salary_min, salary_max):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    
    answer_list = lt.newList(datastructure='ARRAY_LIST')    
    
    tree_date = catalog['tree_by_salary']
    
    values = om.values(tree_date, salary_min, salary_max)
    lista = []
    for value in lt.iterator(values):
        data_value = value['salary']
        for job in lt.iterator(data_value):
            job = search_skills(catalog, job)
            job = search_salary_info(catalog, job)
            if job["salary_from"] != "" and float(job["salary_from"])>float(salary_min) and float(salary_max)>float(job["salary_to"]):
                lt.addLast(answer_list, job)

    merg.sort(answer_list, sort_by_salary)
    
    size = lt.size(answer_list)   
    if size>=10: 
        answer_list = first_and_last(answer_list)
    table = tabulate_rq2(answer_list)
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

def search_skills_req7(catalog, job):
    
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
def search_salary_info(catalog, job):
    
    id = job["id"]
    map_id = catalog["map_id"]
    info_data = mp.get(map_id, id)
    if info_data is not None:
        value_data = info_data["value"]
        list_data = value_data["data"]
        for data in lt.iterator(list_data):
            titulo=data["title"]
            calle=data["street"]
            ciudad=data["city"]
            pais=data["country_code"]
            fecha=data["published_at"]
            tamano=data["company_size"]
            nombre=data["company_name"]
            work=data["workplace_type"]
            experiencia=data["experience_level"]
           
    job["title"]=titulo
    job["street"]=calle
    job["city"]=ciudad
    job["country_code"]=pais
    job["published_at"]=fecha
    job["company_name"]=nombre
    job["company_size"]=tamano
    job["workplace_type"]=work
    job["experience_level"]=experiencia
    

    if job["currency_salary"] == "pln":
        job["salary_from"] = float(job["salary_from"])*0.25 
    elif job["currency_salary"] == "eur":
        job["salary_from"] = float(job["salary_from"])*1.07
    elif job["currency_salary"] == "gbp":
        job["salary_from"] = float(job["salary_from"])*1.25
    elif job["currency_salary"] == "chf":
        job["salary_from"] = float(job["salary_from"])*1.10
    
    return job

def search_salary_info_city(catalog, job):
    
    id = job["id"]
    map_id = catalog["map_salary"]
    info_data = mp.get(map_id, id)
    if info_data is not None:
        value_data = info_data["value"]
        list_data = value_data["data"]
        for data in lt.iterator(list_data): 
            if data["currency_salary"] == "pln":
                job["salary_from"] = float(data["salary_from"])*0.25 
            elif data["currency_salary"] == "eur":
                job["salary_from"] = float(data["salary_from"])*1.07
            elif data["currency_salary"] == "gbp":
                job["salary_from"] = float(data["salary_from"])*1.25
            elif data["currency_salary"] == "chf":
                job["salary_from"] = float(data["salary_from"])*1.10
    
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

def first_and_last_three(list):
    
    first_five = lt.subList(list, 1, 3)
    last_five = lt.subList(list, lt.size(list) - 3, 3)
    
    answer = lt.newList(datastructure="ARRAY_LIST")
    
    for element in lt.iterator(first_five):
        lt.addLast(answer, element)
    for element in lt.iterator(last_five):
        lt.addLast(answer, element)
        
    return answer


def tabulate_data(data):
    
    headers = ['Fecha', 'Titulo', 'Company_Name', "Experience_Level", "Country", "City",]
    table = []
    for job in lt.iterator(data):
        row = []
        row.append(job["published_at"])
        row.append(job["title"])
        row.append(job["company_name"])
        row.append(job["experience_level"])
        row.append(job["country_code"])
        row.append(job["city"])
        table.append(row)
        
    return tabulate(table, headers=headers, tablefmt="grid")

def tabulate_rq1(data):
    
    headers = ['Fecha', 'Titulo', 'Company_Name', "Experience_Level", "Country", "City", "Company Size", "Tipo de Ubicacion", "Skills"]
    table = []
    for job in lt.iterator(data):
        row = []
        row.append(job["published_at"])
        row.append(job["title"])
        row.append(job["company_name"])
        row.append(job["experience_level"])
        row.append(job["country_code"])
        row.append(job["city"])
        row.append(job["company_size"])
        row.append(job["workplace_type"])
        row.append(job["skills"])
        table.append(row)
        
    return tabulate(table, headers=headers, tablefmt="grid")

def tabulate_rq2(data):
    
    headers = ['Fecha', 'Titulo', 'Company_Name', 'Experience_Level', 'Country', 'City', 'Company Size', "Workplace Type", "Minimum Salary", "Skills"]
    table = []
    for job in lt.iterator(data):
        row = []
        row.append(job["published_at"])
        row.append(job["title"])
        row.append(job["company_name"])
        row.append(job["experience_level"])
        row.append(job["country_code"])
        row.append(job["city"])
        row.append(job["company_size"])
        row.append(job["workplace_type"])
        row.append(job["salary_from"])
        row.append(job["skills"])
        table.append(row)
        
    return tabulate(table, headers=headers, tablefmt="grid")

def tabulate_rq4(data):
    
    headers = ['Fecha', 'Titulo', 'Company_Name', 'Experience_Level', 'Country', 'City', 'Company Size', "Workplace Type", "Minimum Salary", "Skills"]
    table = []
    for job in lt.iterator(data):
        row = []
        print(job)
        row.append(job["published_at"])
        row.append(job["title"])
        row.append(job["company_name"])
        row.append(job["experience_level"])
        row.append(job["country_code"])
        row.append(job["city"])
        row.append(job["company_size"])
        row.append(job["workplace_type"])
        row.append(job["salary_from"])
        row.append(job["skills"])
        table.append(row)
        
    return tabulate(table, headers=headers, tablefmt="grid")




def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(catalog, tipo_trabajo, ciudad, numero_ofertas):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    answer_list = lt.newList(datastructure='ARRAY_LIST')  
    map_workplace = catalog['map_city_workplace']
    key = ciudad+"_"+tipo_trabajo
    info_jobs = mp.get(map_workplace, key)
    if info_jobs is not None:
        value_jobs = info_jobs["value"]
        list_jobs = value_jobs["data"]
        for job in lt.iterator(list_jobs):
            job = search_skills(catalog, job)
            job = search_salary_info_city(catalog, job)
            if "salary_from" in job:
                lt.addLast(answer_list, job)
    merg.sort(answer_list, sort_by_date)
    size = lt.size(answer_list)
    answer_list = lt.subList(answer_list,1, numero_ofertas)
    table = tabulate_rq4(answer_list)
    return size, table

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


def req_7(catalog, tipo_propiedad, pais, ano):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    answer_list = lt.newList(datastructure='ARRAY_LIST')  
    if tipo_propiedad == "experience_level":
        map_workplace = catalog['map_req7_experticia']
    elif tipo_propiedad == "skills":
        map_workplace = catalog['map_req7_habilidades']
    elif tipo_propiedad == "workplace_type":
        map_workplace = catalog['map_req7_ubicacion']  
    keys = mp.keySet(map_workplace)
    for i in lt.iterator(keys):
        if ano in i and pais in i:
            info_jobs = mp.get(map_workplace, i)
            if info_jobs is not None:
                value_jobs = info_jobs["value"]
                list_jobs = value_jobs["data"]
                for job in lt.iterator(list_jobs):
                    job = search_skills(catalog, job)
                    job = search_salary_info_city(catalog, job)
                    if "salary_from" in job:
                        lt.addLast(answer_list, job)
    merg.sort(answer_list, sort_by_date)
    size = lt.size(answer_list)
    if lt.size(answer_list)>=10: 
        answer_list1 = first_and_last(answer_list)
    table = tabulate_rq4(answer_list1)
    grafico = {}
    if tipo_propiedad == "experience_level":
        for m in lt.iterator(answer_list):
            if m["experience_level"] not in grafico:
                grafico[m["experience_level"]] = 1
            else:
                grafico[m["experience_level"]]+=1
    elif tipo_propiedad == "skills":
        for m in lt.iterator(answer_list):
            for i in m["skills"]:
                if i not in grafico:
                 grafico[i] = 1
            else:
                 grafico[i]+=1
    elif tipo_propiedad == "workplace_type":
        for m in lt.iterator(answer_list):
            if m["workplace_type"] not in grafico:
                grafico[m["workplace_type"]] = 1
            else:
                grafico[m["workplace_type"]]+=1
    courses = list(grafico.keys())
    values = list(grafico.values())
            
    fig = plt.figure(figsize = (10, 5))
            
            # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
                    width = 0.5)
            
    plt.xlabel(tipo_propiedad)
    plt.ylabel("Numero de ofertas")
    plt.title("Numero de ofertas por " + tipo_propiedad)
    p =catalog["map_year"]
    valores = mp.get(p, int(ano))
    size1 = lt.size(valores["value"]["data"])
    valor_minimo = []
    valor_maximo = []
    valor_minimo.append(min(grafico.keys()))
    valor_minimo.append(min(grafico.values()))
    valor_maximo.append(max(grafico.keys()))
    valor_maximo.append(max(grafico.values()))
    return size, table, size1, valor_minimo, valor_maximo
    


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

def compare_salary(data_1, data_2):
    """
    Función encargada de comparar dos fechas
    """
    
    if data_1 == data_2:
        return 0
    elif data_1 > data_2:
        return 1
    else:
        return -1
    
def compare_workplace(data_1, data_2):
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

def sort_by_salary(data_1, data_2):
    
    return data_1['salary_from'] > data_2['salary_from']

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
