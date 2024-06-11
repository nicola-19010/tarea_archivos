import csv

#def leer_datos():
    
#def escribir_datos(personas):
    
#def agregar_usuario(nombre, edad, ciudad):
    
#def eliminar_usuario(nombre):

#def modificar_usuario(nombre, edad_nueva, ciudad_nueva):

#def mostrar_personas():

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


