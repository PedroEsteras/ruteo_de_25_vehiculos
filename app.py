from flask import Flask, render_template, request
from utils.instancia import Instance  # Asegurate de tener tu clase Instancia lista
from utils.obtener_coordenadas import obtener_coordenadas_lista, matriz_distancias, obtener_coordenadas_google_maps
import folium


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    try:
        # Obtener datos del formulario
        direcciones = request.form.getlist("direccion[]")
        inicios = request.form.getlist("inicio[]")
        fines = request.form.getlist("fin[]")
        cargas_input = request.form.getlist("carga[]")
        q_vehiculos = int(request.form.get("q_vehiculos", "1"))
        capacidad_vehiculos = int(request.form.get("capacidad", "10"))
        velocidad = int(request.form.get("velocidad", "60"))



        # Cargas a enteros
        cargas = []

        for c in cargas_input:
            try:
                valor = int(c)
                cargas.append(valor if valor >= 0 else 1)
            except:
                cargas.append(1)


        # Procesar ventanas de tiempo
        ventanas = []
        for i in range(len(direcciones)):
            try:
                ini = float(inicios[i]) if i < len(inicios) else 0
                fin = float(fines[i]) if i < len(fines) else 24
                ini = max(0, min(ini, 24)) * 60
                fin = max(ini, min(fin, 24)) * 60
                ventanas.append((ini, fin))
            except:
                ventanas.append((0, 24 * 60))


        puntos = obtener_coordenadas_google_maps(direcciones)
        print(f"Puntos obtenidos: {puntos}")
        matriz = matriz_distancias(puntos)
        # puntos = [{'nombre': 'Juana Manso 740, CABA', 'lng': -58.3628543, 'lat': -34.606188}, {'nombre': 'Avenida Corrientes 587, CABA', 'lng': -58.3749274, 'lat': -34.6031593}, {'nombre': '2359 Venezuela, CABA', 'lng': -58.4004394, 'lat': -34.6150739}, {'nombre': 'Avenida Coronel Diaz 1584, CABA', 'lng': -58.4132794, 'lat': -34.5924232}, {'nombre': 'Barragan 222, CABA', 'lng': -58.5228943, 'lat': -34.6376952}, {'nombre': 'Avenida Santafe 1000', 'lng': -58.38132619999999, 'lat': -34.5955176}, {'nombre': 'Pizzeria Guerrin, CABA', 'lng': -58.385982, 'lat': -34.6041209}, {'nombre': 'Universidad Torcuato Di Tella, CABA', 'lng': -58.44694390000001, 'lat': -34.5480059}, {'nombre': 'Ciudad Universitaria, Buenos Aires', 'lng': -58.44462399999999, 'lat': -34.5423313}, {'nombre': 'paysandu 1624, Buenos Aires', 'lng': -58.45779229999999, 'lat': -34.6056494}]
        # print(len(puntos), "CANTIDAD DE PUNTOS")
        # matriz = matriz_distancias(puntos)
        
        instance = Instance(
            matriz=matriz,
            carga=cargas,
            q_vehiculos=q_vehiculos,
            capacidad_vehiculos=capacidad_vehiculos,
            ventana_de_tiempo=ventanas,
            velocidad=velocidad
        )

        rutas = instance.solucion_factible() 


        colores = ["black", "blue", "green", "orange", "brown", 
                   "darkcyan", "darkmagenta", "darkviolet", "deepskyblue", "firebrick"] 

        # Crear mapa centrado en Buenos Aires
        mapa = folium.Map(location=[-34.6037, -58.3816], zoom_start=12)

        # Agregar marcadores
        for i, punto in enumerate(puntos):
            folium.CircleMarker(
                location=[punto["lat"], punto["lng"]],
                radius=4,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.7,
                popup=f"{punto['nombre']}"
            ).add_to(mapa)

        # Dibujar rutas con colores
        for col, camino in enumerate(rutas):
            color = colores[col % len(colores)]
            for i in range(len(camino) - 1):
                j = camino[i]
                jj = camino[i + 1]
                folium.PolyLine(
                    locations=[(puntos[j]["lat"], puntos[j]["lng"]), (puntos[jj]["lat"], puntos[jj]["lng"])],
                    color=color,
                    weight=4,
                    opacity=0.8
                ).add_to(mapa)

            # Cerrar la ruta volviendo al inicio
            folium.PolyLine(
                locations=[(puntos[camino[-1]]["lat"], puntos[camino[-1]]["lng"]), (puntos[camino[0]]["lat"], puntos[camino[0]]["lng"])],
                color=color,
                weight=4,
                opacity=0.8
            ).add_to(mapa)

        # Generar HTML embebido del mapa
        mapa_html = mapa._repr_html_()

        # Pasar el HTML del mapa y las rutas al template
        return render_template("resultado.html", mapa=mapa_html, rutas=rutas, puntos=puntos)
    

    
    except Exception as e:
        return f"Error al procesar: {e}", 500
    





if __name__ == "__main__":
    app.run(debug=True)
