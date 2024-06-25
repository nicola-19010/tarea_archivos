import json

def leer_verduras():
    try:
        with open('verduras.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  

def escribir_verduras(verduras):
    with open('verduras.json', 'w') as archivo:
        json.dump(verduras, archivo)  

def agregar_verdura(nombre, cantidad):
    verduras = leer_verduras()
    verduras.append({'nombre': nombre, 'cantidad': cantidad})
    escribir_verduras(verduras)

def eliminar_verdura(nombre):
    verduras = leer_verduras()
    for verdura in verduras:
        if verdura['nombre'] == nombre:
            verduras.remove(verdura)
    escribir_verduras(verduras)

def modificar_verdura(nombre, nueva_cantidad):
    verduras = leer_verduras()
    for verdura in verduras:
        if verdura['nombre'] == nombre:
            verdura['cantidad'] = nueva_cantidad
    escribir_verduras(verduras)

def mostrar_verduras():
    verduras = leer_verduras()
    for verdura in verduras:
        print(f"Nombre: {verdura['nombre']}, Cantidad: {verdura['cantidad']}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar verduras")
        print("2. Agregar verdura")
        print("3. Modificar verdura")
        print("4. Eliminar verdura")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_verduras()
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la verdura: ")
            cantidad = int(input("Ingrese la cantidad: "))
            agregar_verdura(nombre, cantidad)
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la verdura a modificar: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            modificar_verdura(nombre, nueva_cantidad)
        elif opcion == '4':
            nombre = input("Ingrese el nombre de la verdura a eliminar: ")
            eliminar_verdura(nombre)
        elif opcion == '5':
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
