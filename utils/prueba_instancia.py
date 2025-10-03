from instancia import Instance

# direcciones = [{'nombre': 'Juana Manso 740, CABA', 'lng': -58.3628543, 'lat': -34.606188}, {'nombre': 'Edificio ICBC, CABA', 'lng': -58.3646533, 'lat': -34.598542}, {'nombre': 'Edificio Pampa Energy, CABA', 'lng': -58.3760536, 'lat': -34.6079336}, {'nombre': 'Facultad de Derecho UBA, CABA', 'lng': -58.39197959999999, 'lat': -34.5826299}, {'nombre': 'Teatro Colon, CABA', 'lng': -58.3833278, 'lat': -34.601152}, {'nombre': 'Escuela Superior de Comercio Carlos Pellegrini, CABA', 'lng': -58.3940649, 'lat': -34.597085}, {'nombre': 'Universidad Torcuato Di Tella CABA', 'lng': -58.44694390000001, 'lat': -34.5480059}, {'nombre': 'Cafe Tabac Av Libertador CABA', 'lng': -58.4046528, 'lat': -34.5809763}]
# matriz =  [[0, 0.87, 1.22, 3.74, 1.96, 3.03, 10.06, 4.74], [0.87, 0, 1.48, 3.06, 1.73, 2.7, 9.4, 4.15], [1.22, 1.48, 0, 3.17, 1.01, 2.04, 9.3, 3.98], [3.74, 3.06, 3.17, 0, 2.21, 1.62, 6.34, 1.17], [1.96, 1.73, 1.01, 2.21, 0, 1.08, 8.3, 2.97], [3.03, 2.7, 2.04, 1.62, 1.08, 0, 7.3, 2.04], [10.06, 9.4, 9.3, 6.34, 8.3, 7.3, 0, 5.33], [4.74, 4.15, 3.98, 1.17, 2.97, 2.04, 5.33, 0]]
# cargas =  [0, 1, 1, 1, 1, 1, 1, 1]
# q_vehiculos =  1
# capacidad_vehiculos = 2
# ventanas =   [(0, 1440.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0)]
# velocidad =  10
# materiales =  ['', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento']



# direcciones = [{'nombre': 'Juana Manso 740, CABA', 'lng': -58.3628543, 'lat': -34.606188}, {'nombre': 'Edificio ICBC, CABA', 'lng': -58.3646533, 'lat': -34.598542}, {'nombre': 'Edificio Pampa Energy, CABA', 'lng': -58.3760536, 'lat': -34.6079336}, {'nombre': 'Facultad de Derecho UBA, CABA', 'lng': -58.39197959999999, 'lat': -34.5826299}, {'nombre': 'Teatro Colon, CABA', 'lng': -58.3833278, 'lat': -34.601152}]
# matriz =  [[0, 0.87, 1.22, 3.74, 1.96], [0.87, 0, 1.48, 3.06, 1.73], [1.22, 1.48, 0, 3.17, 1.01], [3.74, 3.06, 3.17, 0, 2.21], [1.96, 1.73, 1.01, 2.21, 0]]
# cargas =  [0, 1, 1, 1, 1]
# q_vehiculos =  1
# capacidad_vehiculos =  10
# ventanas =  [(0, 1440.0), (480.0, 1020.0), (660.0, 780.0), (900.0, 1080.0), (480.0, 1020.0)]
# velocidad =  10
# materiales =  ['', 'Cemento', '', '', '']


# direcciones = [{'nombre': 'Juana Manso 740, CABA', 'lng': -58.3628543, 'lat': -34.606188}, {'nombre': 'Av. Rivadavia 5408, CABA', 'lng': -58.441367, 'lat': -34.620971}, {'nombre': 'Av. Rivadavia 5712, CABA', 'lng': -58.44595639999999, 'lat': -34.6226549}, {'nombre': 'Av. José María Moreno 100, CABA', 'lng': -58.4358034, 'lat': -34.6191713}, {'nombre': 'Av. Pedro Goyena 100, CABA', 'lng': -58.4284882, 'lat': -34.6254067}, {'nombre': 'Av. Gaona 100, CABA', 'lng': -58.4699339, 'lat': -34.6182317}, {'nombre': 'Av. Avellaneda 1548, CABA', 'lng': -58.4530537, 'lat': -34.6203802}, {'nombre': 'Av. Díaz Vélez 5152, CABA', 'lng': -58.4394074, 'lat': -34.6090641}, {'nombre': 'Pujol 644, CABA', 'lng': -58.44843760000001, 'lat': -34.6151026}, {'nombre': 'Rojas 100, CABA', 'lng': -58.44199249999999, 'lat': -34.6194256}, {'nombre': 'Yerbal 100, CABA', 'lng': -58.43221399999999, 'lat': -34.6151244}, {'nombre': 'Del Barco Centenera 141, CABA', 'lng': -58.441112, 'lat': -34.6212889}, {'nombre': 'Honorio Pueyrredón 100, CABA', 'lng': -58.44129220000001, 'lat': -34.6191999}]
# matriz =  [[0, 7.37, 7.82, 6.83, 6.38, 9.89, 8.4, 7.01, 7.89, 7.39, 6.42, 7.36, 7.32], [7.37, 0, 0.46, 0.55, 1.28, 2.63, 1.07, 1.34, 0.92, 0.18, 1.06, 0.04, 0.2], [7.82, 0.46, 0, 1.01, 1.63, 2.25, 0.7, 1.63, 0.87, 0.51, 1.51, 0.47, 0.57], [6.83, 0.55, 1.01, 0, 0.96, 3.12, 1.58, 1.17, 1.24, 0.57, 0.56, 0.54, 0.5], [6.38, 1.28, 1.63, 0.96, 0, 3.88, 2.32, 2.07, 2.16, 1.4, 1.19, 1.24, 1.36], [9.89, 2.63, 2.25, 3.12, 3.88, 0, 1.56, 2.97, 2.0, 2.56, 3.47, 2.66, 2.62], [8.4, 1.07, 0.7, 1.58, 2.32, 1.56, 0, 1.77, 0.72, 1.02, 1.99, 1.1, 1.08], [7.01, 1.34, 1.63, 1.17, 2.07, 2.97, 1.77, 0, 1.06, 1.18, 0.94, 1.37, 1.14], [7.89, 0.92, 0.87, 1.24, 2.16, 2.0, 0.72, 1.06, 0, 0.76, 1.48, 0.96, 0.8], [7.39, 0.18, 0.51, 0.57, 1.4, 2.56, 1.02, 1.18, 0.76, 0, 1.01, 0.22, 0.07], [6.42, 1.06, 1.51, 0.56, 1.19, 3.47, 1.99, 0.94, 1.48, 1.01, 0, 1.06, 0.95], [7.36, 0.04, 0.47, 0.54, 1.24, 2.66, 1.1, 1.37, 0.96, 0.22, 1.06, 0, 0.23], [7.32, 0.2, 0.57, 0.5, 1.36, 2.62, 1.08, 1.14, 0.8, 0.07, 0.95, 0.23, 0]]
# cargas =  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# q_vehiculos =  2
# capacidad_vehiculos =  5
# ventanas =  [(300.0, 1380.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0), (480.0, 1020.0)]
# velocidad =  10
# materiales =  ['', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Cemento', 'Asfalto', 'Asfalto', 'Asfalto']



direcciones = [{'nombre': 'Juana Manso 740, CABA', 'lng': -58.3628543, 'lat': -34.606188}, {'nombre': 'Edificio ICBC, CABA', 'lng': -58.3646533, 'lat': -34.598542}, {'nombre': 'Universidad de Palermo, CABA', 'lng': -58.4158971, 'lat': -34.5973151}, {'nombre': 'Universidad de Belgrano, CABA', 'lng': -58.4438222, 'lat': -34.5638646}, {'nombre': 'Universidad Catolica Argentina UCA, CABA', 'lng': -58.3657906, 'lat': -34.6136442}, {'nombre': 'UADE, CABA', 'lng': -58.3819186, 'lat': -34.617048}, {'nombre': 'Universidad Di Tella, CABA', 'lng': -58.44694390000001, 'lat': -34.5480059}, {'nombre': 'Facultad de Derecho UBA, CABA', 'lng': -58.39197959999999, 'lat': -34.5826299}, {'nombre': 'Facultad de Psicologia UBA, CABA', 'lng': -58.4124022, 'lat': -34.6123364}, {'nombre': 'Ciudad Universitaria, UBA, CABA', 'lng': -58.44462399999999, 'lat': -34.5423313}, {'nombre': 'ITBA parque patricios, CABA', 'lng': -58.4063908, 'lat': -34.6417149}]
matriz =  [[0, 0.87, 4.95, 8.78, 0.87, 2.12, 10.06, 3.74, 4.59, 10.32, 5.61], [0.87, 0, 4.69, 8.21, 1.68, 2.59, 9.4, 3.06, 4.63, 9.63, 6.13], [4.95, 4.69, 0, 4.51, 4.93, 3.81, 6.18, 2.73, 1.7, 6.66, 5.01], [8.78, 8.21, 4.51, 0, 9.04, 8.19, 1.79, 5.19, 6.11, 2.4, 9.31], [0.87, 1.68, 4.93, 9.04, 0, 1.52, 10.41, 4.2, 4.27, 10.72, 4.85], [2.12, 2.59, 3.81, 8.19, 1.52, 0, 9.71, 3.94, 2.84, 10.1, 3.54], [10.06, 9.4, 6.18, 1.79, 10.41, 9.71, 0, 6.34, 7.82, 0.67, 11.06], [3.74, 3.06, 2.73, 5.19, 4.2, 3.94, 6.34, 0, 3.8, 6.58, 6.7], [4.59, 4.63, 1.7, 6.11, 4.27, 2.84, 7.82, 3.8, 0, 8.32, 3.31], [10.32, 9.63, 6.66, 2.4, 10.72, 10.1, 0.67, 6.58, 8.32, 0, 11.59], [5.61, 6.13, 5.01, 9.31, 4.85, 3.54, 11.06, 6.7, 3.31, 11.59, 0]]
cargas =  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
q_vehiculos =  2
capacidad_vehiculos =  4
ventanas =  [(0, 1440.0), (480.0,600), (480.0, 600), (480.0, 600), (480.0, 600), (480.0, 600), (480.0, 600), (480.0, 600), (480.0, 600), (480.0, 600), (480.0,600)]
velocidad =  13


instance = Instance(
            matriz=matriz,
            carga=cargas,
            q_vehiculos=q_vehiculos,
            capacidad_vehiculos=capacidad_vehiculos,
            ventana_de_tiempo=ventanas,
            velocidad=velocidad,
)
        

solucion = instance.solucion_factible()

camiones, horarios = instance.definir_horarios_camiones(solucion)

print("##############")
print("SOLUCION: ", solucion)

print("CAMIONES: ", camiones)
print("HORARIOS: ", horarios)
print("LEN(CAMIONES): ", len(camiones))


print("SOLUCION FACTIBLE?", instance.caminos_validos(solucion))


print("FORMATEADO", instance.formatear_horarios(solucion))