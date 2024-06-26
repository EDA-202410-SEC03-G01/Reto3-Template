﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import numpy as np
import matplotlib.pyplot as plt
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(size):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(size)
    
    return control
    

def choose_size():

    print("Escoja el tamanio de los datos")
    print("1. small")
    print("2. medium")
    print("3. large")
    print("4. 10 porciento")
    print("5. 20 porciento")
    print("6. 30 porciento")
    print("7. 40 porciento")
    print("8. 50 porciento")
    print("9. 60 porciento")
    print("10. 70 porciento")
    print("11. 80 porciento")
    print("12. 90 porciento")
    
    value = int(input("Ingrese el valor: "))
    
    if value == 1:
        return "small-"
    elif value == 2:
        return "medium-"
    elif value == 3:
        return "large-"
    elif value == 4:
        return "10-por-"
    elif value == 5:
        return "20-por-"
    elif value == 6:
        return "30-por-"
    elif value == 7:
        return "40-por-"
    elif value == 8:
        return "50-por-"
    elif value == 9:
        return "60-por-"
    elif value == 10:
        return "70-por-"
    elif value == 11:
        return "80-por-"
    elif value == 12:
        return "90-por-"
    else:
        return "large-"


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, size):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    return controller.load_data(control, size)


def print_data(catalog):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    answer = controller.data(catalog)
    if answer is not None:
        size, table = answer
        print("============= Carga de Datos =============")
        print(f"La cantidad de ofertas es {size}")
        print(table)
    else:
        print("No funciono")

def print_req_1(control, date_min, date_max):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    
    answer = controller.req_1(control, date_min, date_max)
    
    if answer is not None:
        size, table = answer
        print("============= Requerimiento 1 =============")
        print("Ofertas laborales publicadas entre las fechas " + date_min + " y " + date_max)
        print(f"La cantidad de ofertas es {size}")
        print(table)
    else:
        print("No funciono")
        


def print_req_2(control, salario_min, salario_max):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    answer = controller.req_2(control, salario_min, salario_max)
    
    if answer is not None:
        size, table = answer
        print("============= Requerimiento-2  =============")
        print("Ofertas laborales publicadas entre los salarios " + salario_min + " y " + salario_max)
        print(f"La cantidad de ofertas es {size}")
        print(table)
    else:
        print("No funciono")
  


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, tipo_trabajo, pais, numero_ofertas):
    """
        Función que imprime la solución del Requerimiento 4en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    answer = controller.req_4(control, tipo_trabajo, ciudad, numero_ofertas)
    
    if answer is not None:
        size, table = answer
        print("============= Requerimiento-4  =============")
        print("Ofertas laborales publicadas ciudad y tipo de trabajo " + tipo_trabajo + " y " + ciudad)
        print(f"La cantidad de ofertas es {size}")
        print(table)
    else:
        print("No funciono")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control, tipo_propiedad, pais, ano):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    answer = controller.req_7(control, tipo_propiedad, pais, ano)
    
    if answer is not None:
        size, table, size1, valor_minimo, valor_maximo = answer
        
        print("============= Requerimiento-7 =============")
        print("Ofertas laborales publicadas para el pais, ano y propiedad " + tipo_propiedad + pais + " y " + str(ano))
        print(f"La cantidad de ofertas en el ano son {size1}")
        print(f"La cantidad de ofertas utilizadas en el grafico son {size}")
        print(f"El valor minimo utilizado en el grafico es {valor_minimo}")
        print(f"El valor maximo utilizado en el grafico es {valor_maximo}")
        print(table)
        plt.show()
    else:
        print("No funciono")


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            size = choose_size()
            control = new_controller(size)
            control = load_data(control, size)
            print_data(control)
            print("Información cargada correctamente\n")
            
        elif int(inputs) == 2:
            print("---------- Requerimiento 1 ----------\n")
            print("Conocer las ofertas laborales publicadas durante un intervalo de fechas especifico\n")
            
            date_min = input("Ingrese fecha limite inferior: ")
            date_max = input("Ingrese fecha limite superior: ")
            
            print_req_1(control, date_min, date_max)

        elif int(inputs) == 3:
            print("---------- Requerimiento 2 ----------\n")
            print("Conocer las ofertas laborales publicadas durante un intervalo de salarios especifico\n")
            
            salario_min = input("Ingrese el limite inferior del salario: ")
            salario_max = input("Ingrese el limite superior del salario: ")
            
            print_req_2(control, salario_min, salario_max)


        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print("---------- Requerimiento 4 ----------\n")
            print("Conocer las ofertas laborales publicadas dado el pais y tipo de trabajo")
            
            tipo_trabajo = input("Ingrese el tipo de trabajo: ")
            ciudad = input("Ingrese la ciudad: ")
            numero_ofertas = int(input("Ingrese el numero de ofertas: "))
            print_req_4(control, tipo_trabajo, ciudad, numero_ofertas)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            
            print_req_6(control)

        elif int(inputs) == 8:
            print("---------- Requerimiento 7 ----------\n")
            print("Conocer las ofertas laborales publicadas dado un ano, pais y propiedad de conteo")
            
            tipo_trabajo = str(input("Ingrese el tipo de propiedad (experticia, ubicacion o habilidad): "))
            if tipo_trabajo == "experticia":
                tipo_trabajo = "experience_level"
            if tipo_trabajo == "habilidad":
                tipo_trabajo = "skills"
            if tipo_trabajo == "ubicacion":
                tipo_trabajo = "workplace_type"
            pais = str(input("Ingrese el pais: "))
            ano = str(input("Ingrese el ano: "))
            print_req_7(control, tipo_trabajo, pais, ano)
        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
