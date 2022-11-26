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
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos
def loadNodes(analyzer, file ):
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=",")
    for line in input_file:
        ruta = line['Code'] + '-' + line['Bus_Stop'].split('-')[1].strip()
        transbordo = line['Transbordo'] == 'S'
        model.add_stop(analyzer, ruta, transbordo, line)
    return analyzer

def loadEdges(analyzer, file):
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=",")
    for line in input_file:
        bus_stop = line['Bus_Stop'].split('-')[1].strip()
        initial = line['Code'] + '-' + bus_stop 
        final = line['Code_Destiny'] + '-' + bus_stop         
        model.add_connection(analyzer, initial, final)
    model.trasbordos(analyzer)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def get_size_bus_routes(analyzer):
    return model.get_size_bus_routes(analyzer)

def get_size_share_stops(analyzer):
    return model.get_size_share_stops(analyzer)

def get_size_unique_stops(analyzer):
    return model.get_size_unique_stops(analyzer)

def get_num_connections(analyzer):
    return model.get_num_connections(analyzer)

def req_1(analyzer, initial, final):
    return model.req_1(analyzer, initial, final)

def req_2(analyzer, initial, final):
    return model.req_2(analyzer, initial, final)