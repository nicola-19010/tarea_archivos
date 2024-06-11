import json

#Implementar funciones

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


