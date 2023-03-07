import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datawarehouse"
)

cursor = mydb.cursor()


# #estados
# estados = ["Jalisco", "Michoacán", "Nuevo León", "Veracruz", "Yucatán"]

# # Valores seleccionados
# valores_seleccionados = []

# for i in range(5):
#     # Seleccionar un valor aleatorio que no se haya seleccionado antes
#     random_row2 = random.choice([e for e in estados if e not in valores_seleccionados])
#     valores_seleccionados.append(random_row2)
    
#     # Construir la consulta SQL
#     sql = "INSERT INTO estados (idestados, nombre) VALUES (%s, %s)"
#     val = (i, random_row2)
#     cursor.execute(sql, val)
#     mydb.commit()

#     print(cursor.rowcount, "fila insertada.")

# #ciudades
# ciudades = ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla",
#             "Tijuana", "León", "Cancún", "Mérida", "Cuernavaca", "Veracruz",
#             "Oaxaca", "Chihuahua", "Morelia", "Acapulco", "San Luis Potosí"]

# idestados = -1

# # Valores seleccionados
# valores_seleccionados = []

# for i in range(15):

#     # Lista de poblaciones
#     poblaciones = random.randint(100000, 2000000)
    
#     idestados = idestados+1
#     if(idestados == 4):
#         idestados=0
#     # Seleccionar un valor aleatorio que no se haya seleccionado antes
#     random_row2 = random.choice([e for e in ciudades if e not in valores_seleccionados])
#     valores_seleccionados.append(random_row2)
    
#     # Construir la consulta SQL
#     sql = "INSERT INTO ciudades (idciudades, nombre, poblacion, estados_idestados) VALUES (%s, %s,%s, %s)"
#     val = (i, random_row2, poblaciones, idestados)
#     #print (val)
#     cursor.execute(sql, val)
#     mydb.commit()

#     print(cursor.rowcount, "fila insertada.")

# #hospitales
# nombres_hospitales = ["Hospital General de México", "Hospital Juárez de México", "Instituto Nacional de Cardiología", 
#                       "Hospital Español de México", "Hospital Infantil de México Federico Gómez", "Hospital Ángeles del Pedregal", 
#                       "Hospital ABC", "Hospital Santa Fe", "Hospital San Ángel Inn", "Hospital Angeles Mocel", 
#                       "Hospital Angeles Lomas", "Hospital Central Militar", "Hospital Naval de Alta Especialidad", 
#                       "Hospital Regional de Alta Especialidad de Ixtapaluca", "Hospital Psiquiátrico Infantil Juan N. Navarro", 
#                       "Instituto Nacional de Neurología y Neurocirugía", "Instituto Nacional de Enfermedades Respiratorias", 
#                       "Instituto Nacional de Cancerología", "Hospital de Especialidades del Centro Médico Nacional de Occidente", 
#                       "Hospital Central Sur de Alta Especialidad", "Hospital General de Zona #14 del IMSS", "Hospital General de Tijuana", 
#                       "Hospital Materno Infantil de Tijuana", "Hospital del Niño y la Mujer", "Hospital Central Ignacio Morones Prieto", 
#                       "Hospital Universitario de Monterrey", "Hospital Regional de Alta Especialidad de Ciudad Victoria", 
#                       "Hospital Regional de Alta Especialidad de Oaxaca", "Hospital Civil de Guadalajara","Hospital General Dr. Ernesto Meana San Roman"]
                      
# tipos_hospitales = ["Público", "Público", "Público", "Privado", "Público", "Privado", "Privado", "Privado", "Privado", "Privado", 
#                     "Privado", "Público", "Público", "Público", "Público", "Público", "Público", "Público", "Público", "Público", 
#                     "Público", "Público", "Público", "Público", "Público", "Público", "Público", "Público", "Público", "Público"]

# idestados = -1
# # Valores seleccionados
# valores_seleccionados = []

# for i in range(30):

#     idestados = idestados+1
#     if(idestados == 15):
#         idestados=0

#     # Seleccionar un valor aleatorio que no se haya seleccionado antes
#     random_row2 = random.choice([e for e in nombres_hospitales if e not in valores_seleccionados])
#     valores_seleccionados.append(random_row2)
#     random_row = random.choice(tipos_hospitales)
    
#     # Construir la consulta SQL
#     sql = "INSERT INTO hospitales (idhospitales, nombre, tipo, ciudades_idciudades) VALUES (%s, %s,%s, %s)"
#     val = (i, random_row2, random_row, idestados)
#     # print (val)
#     # print(len(nombres_hospitales))
#     cursor.execute(sql, val)
#     mydb.commit()

#     print(cursor.rowcount, "fila insertada.")

#hospitales
nombres = ['María', 'José', 'Juan', 'Ana', 'Pedro', 'Luis', 'Carlos', 'Jorge', 'Laura', 'Fernando', 'Mónica', 'David', 'Miguel', 'Lucía', 'Ricardo', 'Patricia', 'Diana', 'Sofía', 'Gabriel', 'Raúl', 'Elena', 'Alejandro', 'Verónica', 'Silvia', 'Lorena', 'Diego', 'Carmen', 'Bruno', 'Gloria', 'Natalia', 'Andrea', 'Renata', 'Victoria', 'Isabel', 'Valentina', 'Roberto', 'Esther', 'Manuel', 'Adriana', 'Alicia', 'Rodrigo', 'Víctor', 'Dulce', 'Jesús', 'Fabiola', 'Miriam', 'Ángela', 'Francisco', 'Santiago', 'Sara', 'Daniel', 'Ignacio', 'Eduardo', 'Julieta', 'Gisela', 'Mauricio', 'Marina', 'Gustavo', 'Rosa', 'Oscar', 'Julio', 'René', 'Lucas', 'Aurora', 'Cristina', 'César', 'Emilio', 'Lidia', 'Daniela', 'Camila', 'Susana', 'Tomás', 'Claudia', 'Federico', 'Marcos', 'Gabriela', 'Guillermo', 'Luz', 'Hugo', 'Álvaro', 'Olivia', 'Elena', 'Marcela', 'Amanda', 'Leonardo', 'Isidro', 'Ernesto', 'Liliana', 'Pablo', 'Vicente', 'Vanessa']

especialidades = ["Cardiología", "Oncología", "Pediatría", "Ginecología", "Neurología", "Psiquiatría", "Dermatología", "Urología", "Traumatología", "Oftalmología", 
                  "Radiología", "Infectología", "Reumatología", "Endocrinología", "Hematología", "Nutrición", "Odontología", "Geriatría", "Cirugía Plástica", "Cirugía General"]


idestados = -1
# Valores seleccionados
valores_seleccionados = []

for i in range(90):

    idestados = idestados+1
    if(idestados == 30):
        idestados=0
    sueldo = random.randint(1000, 50000)
    # Seleccionar un valor aleatorio que no se haya seleccionado antes
    random_row2 = random.choice([e for e in nombres if e not in valores_seleccionados])
    valores_seleccionados.append(random_row2)
    random_row = random.choice(especialidades)
    
    # Construir la consulta SQL
    sql = "INSERT INTO doctores (iddoctores, nombre, sueldo, especialidad, hospitales_idhospitales) VALUES (%s, %s,%s, %s, %s)"
    val = (i, random_row2,sueldo, random_row, idestados)
    # print (val)
    # print(len(nombres_hospitales))
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "fila insertada.")

