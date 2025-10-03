from flask import Flask, render_template, request
from utils.instancia import Instance  # Asegurate de tener tu clase Instancia lista
from utils.obtener_coordenadas import obtener_coordenadas_lista, matriz_distancias, obtener_coordenadas_google_maps
import folium
import traceback

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
        
    try:
        # Obtener datos del formulario
        deposito_dir = request.form.get("deposito_direccion", "")
        deposito_inicio = request.form.get("deposito_inicio", "0")
        deposito_fin = request.form.get("deposito_fin", "24")

        direcciones = request.form.getlist("direccion[]")
        inicios = request.form.getlist("inicio[]")
        fines = request.form.getlist("fin[]")
        cargas_input = request.form.getlist("carga[]")
        

        q_vehiculos = int(request.form.get("q_vehiculos", "1"))
        capacidad_vehiculos = int(request.form.get("capacidad", "10"))
        velocidad = int(request.form.get("velocidad", "60"))

        # --- Insertar depósito como primer nodo ---
        direcciones = [deposito_dir] + direcciones

        # Cargas (depósito = 0)
        cargas = [0]
        for c in cargas_input:
            try:
                valor = int(c)
                cargas.append(valor if valor >= 0 else 1)
            except:
                cargas.append(1)

        # Ventanas de tiempo
        ventanas = []
        # Depósito
        try:
            ini = max(0, min(float(deposito_inicio), 24)) * 60
            fin = max(ini/60, min(float(deposito_fin), 24)) * 60
            ventanas.append((ini, fin))
        except:
            ventanas.append((0, 24 * 60))

        # Resto de direcciones
        for i in range(len(direcciones) - 1):  # resto (ya insertamos depósito)
            try:
                ini = float(inicios[i]) if i < len(inicios) else 0
                fin = float(fines[i]) if i < len(fines) else 24
                ini = max(0, min(ini, 24)) * 60
                fin = max(ini/60, min(fin, 24)) * 60
                ventanas.append((ini, fin))
            except:
                ventanas.append((0, 24 * 60))


        puntos = obtener_coordenadas_google_maps(direcciones)
        print(f"Puntos obtenidos: {puntos}")
        matriz = matriz_distancias(puntos)
        


        

        print("matriz = ", matriz)
        print("cargas = ", cargas)
        print("q_vehiculos = ", q_vehiculos)
        print("capacidad_vehiculos = ", capacidad_vehiculos)
        print("ventanas = ", ventanas)
        print("velocidad = ", velocidad)
    

        instance = Instance(
            matriz=matriz,
            carga=cargas,
            q_vehiculos=q_vehiculos,
            capacidad_vehiculos=capacidad_vehiculos,
            ventana_de_tiempo=ventanas,
            velocidad=velocidad,
        )
        

        rutas = instance.solucion_factible()
        formateo_sol = instance.formatear_horarios(rutas)        
        
        
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
        return render_template("resultado.html", mapa=mapa_html, resultados=formateo_sol, puntos=puntos)

    
    except Exception as e:
        tb = traceback.format_exc()
        # Devolverlo como respuesta
        return f"Error al procesar:\n{tb}", 500
    





if __name__ == "__main__":
    app.run(debug=True)
