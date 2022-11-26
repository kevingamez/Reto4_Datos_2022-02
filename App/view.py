"""
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Buscar un camino posible entre dos estaciones (G)")
    print("2- Buscar el camino con menos paradas entre dos estaciones (G)")
    print("3- Reconocer los componentes conectados de la Red de rutas de bus (I)")
    print("4- Planear el camino con distancia mínima entre dos puntos geográficos (I)")
    print("5- Informar las estaciones “alcanzables” desde un origen a un número máximo de conexiones")
    print("6- Buscar el camino con mínima distancia entre una estación de origen y un vecindario de destino (G)")
    print("7- Encontrar un posible camino circular desde una estación de origen (G)")
    print("8- Graficar resultados para cada uno de los requerimientos (B)")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()

    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        file_nodes = cf.data_dir + 'Barcelona/bus_stops_bcn-utf8-large.csv'
        file_edges = cf.data_dir + 'Barcelona/bus_edges_bcn-utf8-large.csv'
        catalog = controller.init()
        controller.loadNodes(catalog, file_nodes)
        controller.loadEdges(catalog, file_edges)
        print('Número de rutas de autobús cargadas: ' + str(controller.get_size_bus_routes(catalog)))
        print('Número de paradas de autobús excusivas cargadas: ' + str(controller.get_size_unique_stops(catalog)))
        print('Número de paradas de autobús compartidas cargadas: ' + str(controller.get_size_share_stops(catalog)))
        print('Número de arcos usados: ' + str(controller.get_num_connections(catalog)))
        
    elif int(inputs[0]) == 1:
        pass
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 8:
        pass
    else:
        sys.exit(0)
sys.exit(0)
