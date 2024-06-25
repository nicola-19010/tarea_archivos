import json

class Hotel:
    def __init__(self, habitaciones):
        self.habitaciones = habitaciones
    
    def agregar_habitacion(self, numero, tipo, estado):
        nueva_habitacion = Habitacion(numero, tipo, estado)
        self.habitaciones.append(nueva_habitacion)

    def consultar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return vars(habitacion)
        return {}
    
    

class Habitacion:
    def __init__(self, numero, tipo, estado):
        self.numero = numero
        self.tipo = tipo
        self.estado = estado

class GestorArchivos():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def guardar_datos(self, lista_de_objetos):
        with open(self.nombre_archivo, 'w') as archivo:
            json.dump(self.convertir_a_list_diccionarios(lista_de_objetos), archivo)
    
    def cargar_datos(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                return self.convertir_a_list_objetos(json.load(archivo))
        except FileNotFoundError:
            return []
    
    def convertir_a_list_diccionarios(self, lista_de_objetos):
        lista = []
        for objeto in lista_de_objetos:
            lista.append(vars(objeto))
        return lista
    
    def convertir_a_list_objetos(self, lista_de_diccionarios):
        lista = []
        for diccionario in lista_de_diccionarios:
            lista.append(Habitacion(**diccionario))
        return lista
    

def menu():
    gestor_archivos = GestorArchivos('habitaciones.json')
    habitaciones = gestor_archivos.cargar_datos()
    hotel = Hotel(habitaciones)

    while True:
        print("");
        print("Menú:")
        print("1. Agregar habitación")
        print("2. Consultar habitación")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            numero = input("Ingrese el número de la habitación: ")
            tipo = input("Ingrese el tipo de la habitación: ")
            estado = input("Ingrese el estado de la habitación: ")
            hotel.agregar_habitacion(numero, tipo, estado)
            gestor_archivos.guardar_datos(hotel.habitaciones)
        elif opcion == "2":
            numero = input("Ingrese el número de la habitación: ")
            print(hotel.consultar_habitacion(numero))
        elif opcion == "3":
            break
menu()



        
    




