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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Utils import error as error
from DISClib.ADT import graph as gr
from haversine import haversine, Unit


assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    try:
        analyzer = {
            'search' : None,
            'graph' : None,
            'paths' : None,
            'transbordos' : None, 
            'stops' : None,
            'bus_routes' : None,
            'cordenadas_min' : (1000000.0,1000000.0),
            'cordenadas_max' : (1000000.0,1000000.0),
        }

        analyzer['graph'] = gr.newGraph(datastructure='ADJ_LIST', directed=True, size=1000, comparefunction=None)
        analyzer['transbordos'] = mp.newMap(numelements=100, maptype='CHAINING', loadfactor=0.5, comparefunction=None)
        analyzer['stops'] = mp.newMap(numelements=1000, maptype='PROBING', loadfactor=0.5, comparefunction=None)
        analyzer['bus_routes'] = mp.newMap(numelements=1000, maptype='PROBING', loadfactor=0.5, comparefunction=None)

        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')

# Funciones para agregar informacion al catalogo
def add_stop(analyzer, stop, transbordo, info):
    """
    Adiciona una estación como un vértice del grafo
    """
    try:

        if transbordo:
            # Si la estación permite transbordos se verifica si ya existe en el mapa, si no existe se agrega como vertice
            if not mp.contains(analyzer['transbordos'], stop.split('-')[0]):
                buses = lt.newList(datastructure='ARRAY_LIST')
                lt.addLast(buses, stop.split('-')[1])
                mp.put(analyzer['transbordos'], stop.split('-')[0], buses)
                
            else:
                buses = mp.get(analyzer['transbordos'], stop.split('-')[0])['value']
                lt.addLast(buses, stop.split('-')[1])
        mp.put(analyzer['stops'], stop, info)
        bus = stop.split('-')[1]
        if not mp.contains(analyzer['bus_routes'], bus):
            mp.put(analyzer['bus_routes'], bus, stop.split('-')[1])

        if not gr.containsVertex(analyzer['graph'], stop):
            gr.insertVertex(analyzer['graph'], stop)
    except Exception as exp:
        error.reraise(exp, 'model:add_stop')

def add_connection(analyzer, initial, final):
    """
    Adiciona un arco entre dos estaciones
    """
    try:
        lat = float(mp.get(analyzer['stops'], initial)['value']['Latitude'])
        lon = float(mp.get(analyzer['stops'], initial)['value']['Longitude'])
        cor_initial = (lat, lon)
        lat = float(mp.get(analyzer['stops'], final)['value']['Latitude'])
        lon = float(mp.get(analyzer['stops'], final)['value']['Longitude'])
        cor_final = (lat, lon)
        distance = haversine(cor_initial, cor_final)
        
        if analyzer['stops']:
            distance = 0
        gr.addEdge(analyzer['graph'], initial, final, distance)
        gr.addEdge(analyzer['graph'], final, initial, distance)

    except Exception as exp:
        
        error.reraise(exp, 'model:add_connection')

def trasbordos(analyzer):
    vertices = mp.keySet(analyzer['transbordos'])
    for vertex in lt.iterator(vertices):
        parada = 'T-' + vertex
        if not gr.containsVertex(analyzer['graph'], parada):
            gr.insertVertex(analyzer['graph'], parada)
        neighbours = mp.get(analyzer['transbordos'], vertex)['value']
        for neighbor in lt.iterator(neighbours):
            final = vertex+'-'+neighbor
            gr.addEdge(analyzer['graph'], parada, final, 0)
            gr.addEdge(analyzer['graph'], final, parada, 0)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareStopIds(stop1, stop2):
    if stop1 == stop2:
        return 0
    elif stop1 > stop2:
        return 1
    else:
        return -1

def get_size_bus_routes(analyzer):
    return mp.size(analyzer['bus_routes'])

def get_size_share_stops(analyzer):
    return mp.size(analyzer['transbordos'])

def get_size_unique_stops(analyzer):
    return (mp.size(analyzer['stops'])-mp.size(analyzer['transbordos']))

def get_num_connections(analyzer):
    return gr.numEdges(analyzer['graph'])