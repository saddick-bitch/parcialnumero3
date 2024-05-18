#Ejercicio 1
# Definir una lista para almacenar las calificaciones
calificaciones = []

# Solicitar al usuario el número de asignaturas
numero_asignaturas = int(input("Ingrese el número de asignaturas: "))

# Ciclo para ingresar las calificaciones de cada asignatura
for i in range(numero_asignaturas):
  calificacion = float(input(f"Ingrese la calificación de la asignatura {i + 1}: "))
  calificaciones.append(calificacion)

# Calcular la suma de las calificaciones
suma_calificaciones = 0
for calificacion in calificaciones:
  suma_calificaciones += calificacion

# Calcular el promedio de las calificaciones
promedio = suma_calificaciones / numero_asignaturas

# Mostrar el promedio de las calificaciones
print(f"El promedio de las calificaciones es: {promedio:.2f}")

#Ejercicio 2

# Definir una lista para almacenar los contactos
contactos = []

# Función para agregar un nuevo contacto
def agregar_contacto():
  nombre = input("Ingrese el nombre del contacto: ")
  telefono = input("Ingrese el número de teléfono: ")
  correo_electronico = input("Ingrese el correo electrónico: ")

  # Crear un diccionario para almacenar los datos del contacto
  contacto = {
    "nombre": nombre,
    "telefono": telefono,
    "correo_electronico": correo_electronico
  }

  # Agregar el contacto a la lista
  contactos.append(contacto)
  print(f"Contacto agregado correctamente.")

# Función para buscar un contacto por nombre
def buscar_contacto():
  nombre_buscado = input("Ingrese el nombre del contacto a buscar: ")

  # Recorrer la lista de contactos
  for contacto in contactos:
    if contacto["nombre"].lower() == nombre_buscado.lower():
      print(f"Nombre: {contacto['nombre']}")
      print(f"Teléfono: {contacto['telefono']}")
      print(f"Correo electrónico: {contacto['correo_electronico']}")
      return

  # Si no se encuentra el contacto, mostrar un mensaje
  print(f"Contacto no encontrado.")

# Función para eliminar un contacto
def eliminar_contacto():
  nombre_buscado = input("Ingrese el nombre del contacto a eliminar: ")

  # Recorrer la lista de contactos
  for indice, contacto in enumerate(contactos):
    if contacto["nombre"].lower() == nombre_buscado.lower():
      # Eliminar el contacto de la lista
      del contactos[indice]
      print(f"Contacto eliminado correctamente.")
      return

  # Si no se encuentra el contacto, mostrar un mensaje
  print(f"Contacto no encontrado.")

# Función para mostrar todos los contactos
def mostrar_contactos():
  if len(contactos) == 0:
    print("No hay contactos almacenados.")
  else:
    print("Lista de contactos:")
    for contacto in contactos:
      print(f"Nombre: {contacto['nombre']}")
      print(f"Teléfono: {contacto['telefono']}")
      print(f"Correo electrónico: {contacto['correo_electronico']}")
      print("----------")

# Menú principal
while True:
  print("\nMenú de opciones:")
  print("1. Agregar contacto")
  print("2. Buscar contacto")
  print("3. Eliminar contacto")
  print("4. Mostrar contactos")
  print("5. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    agregar_contacto()
  elif opcion == "2":
    buscar_contacto()
  elif opcion == "3":
    eliminar_contacto()
  elif opcion == "4":
    mostrar_contactos()
  elif opcion == "5":
    print("Saliendo del programa...")
    break
  else:
    print("Opción no válida.")

