import csv

def leer_datos():
    lista_personas = []
    try:
        with open('detalles.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                persona = {'nombre': fila[0], 'edad': fila[1], 'ciudad': fila[2]}
                lista_personas.append(persona)
            return lista_personas
    except FileNotFoundError:
        return []

def escribir_datos(personas):
    with open('detalles.csv', 'w') as archivo:
        escritor = csv.writer(archivo)
        for persona in personas:
            escritor.writerow([persona['nombre'], persona['edad'], persona['ciudad']])

def agregar_usuario(nombre, edad, ciudad):
    personas = leer_datos()
    nuevo_usuario = {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}
    personas.append(nuevo_usuario)
    escribir_datos(personas)

def eliminar_usuario(nombre):
    personas = leer_datos()
    for persona in personas:
        if persona['nombre'] == nombre:
            personas.remove(persona)
    escribir_datos(personas)

def modificar_usuario(nombre, edad_nueva, ciudad_nueva):
    personas = leer_datos()
    for persona in personas:
        if persona['nombre'] == nombre:
            persona['edad'] = edad_nueva
            persona['ciudad'] = ciudad_nueva
    escribir_datos(personas)

def mostrar_personas():
    personas = leer_datos()
    for persona in personas:
        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}")

###### Menú (NO MODIFICAR)######
def menu():
    print("")
    print("Menú:")
    print("1. Mostrar personas")
    print("2. Agregar usuario")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

while True:
    menu()
    opcion = input("Ingrese una opción: ")
        
    if opcion == "1":
        mostrar_personas()
    elif opcion == "2":
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        ciudad = input("Ingrese la ciudad: ")
        agregar_usuario(nombre, edad, ciudad)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del usuario a modificar: ")
        edad_nueva = int(input("Ingrese la nueva edad: "))
        ciudad_nueva = input("Ingrese la nueva ciudad: ")
        modificar_usuario(nombre, edad_nueva, ciudad_nueva)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del usuario a eliminar: ")
        eliminar_usuario(nombre)
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")


