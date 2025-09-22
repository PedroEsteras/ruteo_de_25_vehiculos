import os
from dotenv import load_dotenv
import json
from haversine import haversine, Unit
import googlemaps



load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=API_KEY)




with open("utils/direcciones.json", encoding="utf-8") as f:
    direcciones = json.load(f)

def coordenadas_direccion(direccion):
    for d in direcciones:
        if d["nombre"] == direccion:
            return {"lat": d["lat"], "lng": d["lng"], "nombre": d["nombre"]}
    return None  # Si no lo encontró

def obtener_coordenadas_lista(lista_nombres):
    resultado = []
    for nombre in lista_nombres:
        for d in direcciones:
            if d["nombre"] == nombre:
                resultado.append({"lat": d["lat"], "lng": d["lng"], "nombre": d["nombre"]})
                break  # Sale del for cuando encontró la dirección
        else:
            # Si no encontró la dirección en la lista global, puede agregar None o ignorar
            resultado.append(None)
    return resultado



def obtener_coordenadas_google_maps(lista_nombres):
    resultado = []
    for direccion in lista_nombres:
        geocode_result = gmaps.geocode(direccion)

        if geocode_result:
            location = geocode_result[0]["geometry"]["location"]
            nuevo_punto = {"nombre": direccion, "lng" : location['lng'], "lat" : location["lat"]}
            resultado.append(nuevo_punto)

        else:
            print(f"No se encontraron resultados para la dirección {direccion}")
    
    return resultado


def matriz_distancias(puntos):
    """Calcula la matriz de distancias entre puntos geográficos.
    Args:
        puntos (list): Lista de diccionarios con las coordenadas de los puntos.
                       Cada diccionario debe tener las claves 'lat' y 'lng'.
    Returns:
        list: Matriz de distancias entre los puntos, donde la distancia entre el punto i y el j está en la posición [i][j].
    """
    n = len(puntos)
    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(0)  # La distancia a sí mismo es 0
            else:
                # Obtener las coordenadas de los puntos
                punto1 = (puntos[i]['lat'], puntos[i]['lng'])
                punto2 = (puntos[j]['lat'], puntos[j]['lng'])
                
                # Calcular la distancia entre los dos puntos
                distancia = haversine(punto1, punto2, unit=Unit.KILOMETERS)
                fila.append(round(distancia, 2))
        matriz.append(fila)
    
    return matriz