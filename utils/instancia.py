from copy import deepcopy

CANTIDAD_DE_CAMINOS_POR_CAMION_MAXIMO = 10

class Instance:
    def __init__(self, matriz: list[list[int]], carga: list[int], q_vehiculos: int, capacidad_vehiculos: int, 
                 ventana_de_tiempo: list[tuple[int, int]], velocidad:int):
        
        self.n = len(matriz[0])
        self.deposito = 0
        self.clientes = [x for x in range(1, self.n)]
        self.carga = carga
        self.q = q_vehiculos
        self.capacidad_de_vehiculos = capacidad_vehiculos
        self.matriz = matriz
        self.ventanas = ventana_de_tiempo
        self.velocidad = velocidad


    def distancia(self, n1, n2):
        return self.matriz[n1][n2]
    
    def tiempo(self, n1, n2):
        return round((self.matriz[n1][n2] / self.velocidad) * 60, 2)
    
    

    def caminos_validos(self, caminos):
        # Chequeo de capacidad
        for i in range(len(caminos)):
            capacidad = self.capacidad_de_vehiculos
            clientes = caminos[i]
            for cl in clientes:
                capacidad -= self.carga[cl]
            if capacidad < 0:
                #print(f"Fallo por capacidad en camión {i}: capacidad restante={capacidad}, camino={clientes}, caminos={caminos} ")
                return False

        # Chequeo de ventanas de tiempo
        for i, camino in enumerate(caminos):
            if camino == [0]:
                continue
            primer_cliente = camino[1]
            tiempo_actual = self.ventanas[primer_cliente][0]
            for j in range(2, len(camino)):
                cl = camino[j]
                anterior = camino[j - 1]
                viaje = self.tiempo(anterior, cl)
                tiempo_actual = max(viaje + tiempo_actual, self.ventanas[cl][0])
                if tiempo_actual > self.ventanas[cl][1]:
                    #print(f"Fallo por ventana de tiempo en camión {i}: cliente {cl}, tiempo_actual={tiempo_actual}, ventana={self.ventanas[cl]}, camino={camino}")
                    return False

        camiones, horarios = self.definir_horarios_camiones(caminos)
        if len(camiones) > self.q:
            #print(f"Fallo: se necesitan {len(camiones)} camiones, máximo permitido {self.q}")
            return False
        return True

    
    def bt_solucion_factible(self, caminos, sin_visitar: list[int]):
        if sin_visitar == []:
            return caminos, True
        
        else:
            
            copia_sin_visitar = deepcopy(sin_visitar)
            c = copia_sin_visitar[0]
            copia_sin_visitar.remove(c)

            
            for i in range(len(caminos)):
                for j in range(1, len(caminos[i])):

                    copia_caminos = deepcopy(caminos)
                    copia_caminos[i].insert(j, c)
                    
                    if self.caminos_validos(copia_caminos):
                        caminos_sol, termino =  self.bt_solucion_factible(copia_caminos, copia_sin_visitar)
                        if termino:
                            return caminos_sol, termino
                  
            return [], False
                
    def solucion_factible(self):
        solucion = self.bt_solucion_factible([[0,0] for _ in range(self.q*CANTIDAD_DE_CAMINOS_POR_CAMION_MAXIMO)], sin_visitar=self.clientes)[0]

        print("SOLUCION ACTUAL FACTIBLE?", self.caminos_validos(solucion))

     

        self.borrar_vacios(solucion)
        solucion = self.vnd(solucion)
        self.borrar_vacios(solucion)
        return solucion
        

    def costo(self, caminos):
        costo = 0
        for camino in caminos:
            for i in range(len(camino) - 1):
                costo += self.distancia(camino[i], camino[i+1])

        return costo

    def operador_relocate(self, caminos, cam_origen, pos_origen, cam_destino, pos_destino):
        copia_caminos = deepcopy(caminos)
        cliente = copia_caminos[cam_origen].pop(pos_origen)  # Eliminar el cliente del camino origen
        copia_caminos[cam_destino].insert(pos_destino, cliente)  # Insertarlo en el camino destino
        return copia_caminos

    def relocate(self, caminos):
        for c1 in range(len(caminos)):  # Camino de origen
            for c2 in range(len(caminos)):  # Camino de destino
                for p1 in range(1, len(caminos[c1]) - 1):  # Posición del cliente en el camino origen
                    for p2 in range(1, len(caminos[c2]) - 1):  # Posición de inserción en el camino destino
                        if c1 == c2 and p1 == p2:
                            continue  # Evitar mover el cliente a la misma posición
                        nuevos_caminos = self.operador_relocate(caminos, c1, p1, c2, p2)
                        if self.costo(nuevos_caminos) < self.costo(caminos) and self.caminos_validos(nuevos_caminos):
                            return nuevos_caminos
        return caminos
    
    def operador_relocate_2(self, caminos, cam_origen, pos_origen, cam_destino, pos_destino):
        copia_caminos = deepcopy(caminos)

        segmento = copia_caminos[cam_origen][pos_origen:pos_origen + 2]
        del copia_caminos[cam_origen][pos_origen:pos_origen + 2]
        for i, cliente in enumerate(segmento):
            copia_caminos[cam_destino].insert(pos_destino + i, cliente)
        
        return copia_caminos

    def relocate_2(self, caminos):
        for c1 in range(len(caminos)):  
            for c2 in range(len(caminos)):  
                for p1 in range(1, len(caminos[c1]) - 2): 
                    for p2 in range(1, len(caminos[c2]) - 2):  
                        if c1 == c2 and p1 == p2:
                            continue  
                        nuevos_caminos = self.operador_relocate_2(caminos, c1, p1, c2, p2)
                        if self.costo(nuevos_caminos) < self.costo(caminos) and self.caminos_validos(nuevos_caminos):
                            return nuevos_caminos
        return caminos
    
    def operador_swap(self, caminos, cam1, pos1, cam2, pos2):
        copia_caminos = deepcopy(caminos)
        copia_caminos[cam1][pos1], copia_caminos[cam2][pos2] = copia_caminos[cam2][pos2], copia_caminos[cam1][pos1]
        
        return copia_caminos

    def swap(self, caminos):
        for c1 in range(len(caminos)):
            for c2 in range(len(caminos)):
                for p1 in range(1, len(caminos[c1]) - 1):
                    for p2 in range(1, len(caminos[c2]) - 1):
                        nuevos_caminos = self.operador_swap(caminos, c1, p1, c2, p2)
                        if self.costo(nuevos_caminos) < self.costo(caminos) and self.caminos_validos(nuevos_caminos):
                            return nuevos_caminos
        return caminos
    

    def operador_2opt(self, camino, i, k):
        nuevo_camino = deepcopy(camino)
        nuevo_camino[i:k+1] = reversed(nuevo_camino[i:k+1])
        return nuevo_camino

    def two_opt(self, caminos):
        for c in range(len(caminos)):
            for i in range(1, len(caminos[c]) - 2):
                for k in range(i + 1, len(caminos[c]) - 1):
                    nuevo_camino = self.operador_2opt(caminos[c], i, k)
                    nuevos_caminos = deepcopy(caminos)
                    nuevos_caminos[c] = nuevo_camino
                    if self.costo(nuevos_caminos) < self.costo(caminos) and self.caminos_validos(nuevos_caminos):
                        return nuevos_caminos
        return caminos
    

    
    def vnd(self, caminos):
        k = 0
    
       
        while k < 4:
    
            if k == 1:
                nuevos_caminos = self.relocate(caminos)
            elif k == 0:
                nuevos_caminos = self.swap(caminos)
            elif k == 2:
                nuevos_caminos = self.two_opt(caminos)
            elif k == 3:
                nuevos_caminos = self.relocate_2(caminos)
         
            if self.costo(nuevos_caminos) < self.costo(caminos):
               
                caminos = nuevos_caminos
                k = 0  
            else:
                k += 1  

        return caminos

    def hora_salida(self, camino):
        if len(camino) == 1:
            return 0
        return self.ventanas[camino[1]][0] - self.tiempo(0, camino[1])

    def hora_llegada(self, camino):
        if camino == [0]:
            return 0
        else:
            primer_cliente = camino[1]
            tiempo_actual = self.ventanas[primer_cliente][0]
            
            for i in range(2, len(camino)):
                cl = camino[i]
                anterior = camino[i - 1]
                viaje = self.tiempo(anterior, cl) 
                tiempo_actual = max(viaje + tiempo_actual, self.ventanas[cl][0])

        return tiempo_actual
    
    def camiones_al_mismo_tiempo(self, caminos):
        tiempos = [(self.hora_salida(camino), self.hora_llegada(camino)) for camino in caminos]

        max_camiones = 0
        for i in range(len(tiempos)):
            
            mismo_tiempo = 1
            for j in range(len(tiempos)):
                if i != j:
                    if tiempos[i][0] > tiempos[j][0] and tiempos[i][0] < tiempos[j][1] or tiempos[i][1] > tiempos[j][0] and tiempos[i][1] < tiempos[j][1]:
                            mismo_tiempo += 1
            
            max_camiones = max(max_camiones, mismo_tiempo)

        return max_camiones

    def borrar_vacios(self, solucion):
        while [0, 0] in solucion:
            solucion.remove([0, 0])



    def intervalos_camino(self, camino):
        
        # Salida minima

        primer_cliente = camino[1]
        ventana_primer_cliente = self.ventanas[primer_cliente][0]
        viaje_deposito_primer_cliente = self.tiempo(0, primer_cliente)
        salida_minima = ventana_primer_cliente - viaje_deposito_primer_cliente

        # Salida maxima

        ultimo_momento = self.ventanas[camino[-2]][1]
        tiempo_actual = ultimo_momento
        for i in range(len(camino) - 2, 0, -1):
            t_viaje = self.tiempo(camino[i], camino[i-1])
            tiempo_actual = min(tiempo_actual - t_viaje, self.ventanas[camino[i]][1] - t_viaje)
            
       
        salida_maxima = tiempo_actual

        # Llegada minima 

        tiempo_actual = self.ventanas[0][0]
        for j in range(1, len(camino)):
            cl = camino[j]
            anterior = camino[j - 1]
            viaje = self.tiempo(anterior, cl)
            tiempo_actual = max(viaje + tiempo_actual, self.ventanas[cl][0])
       
        llegada_minimo = tiempo_actual

        # Llegada maxima 

        ultimo_cliente = camino[-2]
        ventana_ultimo_cliente = self.ventanas[ultimo_cliente][1]
        llegada_maxima = ventana_ultimo_cliente + self.tiempo(ultimo_cliente, 0)
    


        return {"camino": camino, "L_min": llegada_minimo, "S_max": salida_maxima, "S_min": salida_minima, "L_max": llegada_maxima}


    def definir_horarios_camiones(self, caminos):
        # Calcular intervalos para todos los caminos
        
        intervalos_caminos = [self.intervalos_camino(c) for c in caminos if c != [0]]


        # Ordenar por llegada mínima
        intervalos_caminos.sort(key=lambda x: x["L_min"])

        camiones = []
        horarios = {}

        for c in intervalos_caminos:
            asignado = False
            for camion in camiones:
                ultimo = camion[-1]
                # Condición de encadenamiento:
                # llegada mínima del nuevo camino debe ser después de la salida mínima
                # y no superar la salida máxima del último
                if c["L_min"] >= ultimo["S_min"] and c["L_min"] <= ultimo["S_max"]:
                    camion.append(c)
                    # asignar horario: empieza lo más tarde posible pero sin pasarse
                    inicio = max(c["S_min"], ultimo["L_min"])
                    horarios[tuple(c["camino"])] = (inicio, c["L_min"])
                    asignado = True
                    break

            if not asignado:
                # abrir camión nuevo
                camiones.append([c])
                horarios[tuple(c["camino"])] = (c["S_min"], c["L_min"])

        #for nro, camion in enumerate(camiones, start=1):
            #print(f"Camión {nro}: {[c['camino'] for c in camion]}")

        return camiones, horarios


    def si_salgo_a_las_x_llego(self, camino, x):
        tiempo_actual = x

        for j in range(1, len(camino)):
            cl = camino[j]
            anterior = camino[j - 1]
            viaje = self.tiempo(anterior, cl)
            tiempo_actual = max(viaje + tiempo_actual, self.ventanas[cl][0])

        return minutos_a_horas(tiempo_actual)
        

    def llego_o_no(self, camino, x):
        tiempo_actual = x
        for j in range(1, len(camino)):
            cl = camino[j]
            anterior = camino[j - 1]
            viaje = self.tiempo(anterior, cl)
            tiempo_actual = max(viaje + tiempo_actual, self.ventanas[cl][0])
            if tiempo_actual > self.ventanas[cl][1]:
                #print(f" cliente {cl}, tiempo_actual={tiempo_actual}, ventana={self.ventanas[cl]}, camino={camino}")
                return False
        return True

    def formatear_horarios(self, solucion):

        camiones, horarios = self.definir_horarios_camiones(solucion)
        resultado = []
        
        for idx_camion, recorridos in enumerate(camiones, start=1):
            camion_info = {
                "camion": f"Camión {idx_camion}",
                "recorridos": []
            }
            
            for r in recorridos:
                camino = tuple(r['camino'])
                salida, llegada = horarios.get(camino, (None, None))
                
                camion_info["recorridos"].append({
                    "camino": r['camino'],
                    "salida": minutos_a_horas(salida) if salida is not None else "-",
                    "llegada": minutos_a_horas(llegada) if llegada is not None else "-"
                })
            
            resultado.append(camion_info)
        
        return resultado

def minutos_a_horas(minutos):
    horas = minutos // 60        # Parte entera (horas completas)
    minutos_restantes = minutos % 60  # Minutos sobrantes
    return f"{int(horas)}:{int(minutos_restantes):02d}"