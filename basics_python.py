import json

# Función que no tiene retorno
def saludar():
    print("Hola Mundo")


# Función que tiene retorno
def sumar(a, b):
    return a + b

# Guardar el resultado de la función
resultado = sumar(2, 3)
print("Resultado de la suma:", resultado)

# For each (Python)
lista = ["a", "b", "c"]
for elemento in lista:
    print(elemento)

# Operaciones CRUD en listas
lista = []
# Create
lista.append("a")
# Read
print("Lista después de agregar:", lista)
# Update
lista[0] = "b"
print("Lista después de actualizar:", lista)
# Delete
lista.pop(0)
lista.remove("b")
print("Lista después de eliminar:", lista)

# POO
# Definir una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)
    
    def sumar(self, a, b):
        return a + b

# Crear un objeto
persona = Persona("Juan", 30)

# Acceder a una propiedad
print("Nombre de la persona:", persona.nombre)

# Llamar a un método
persona.saludar()

# ¿Qué es un JSON?
# {clave: valor}
json_example = {
    "nombre": "Juan",
    "edad": 30
}


# ¿Qué es un diccionario?
# {clave: valor}
diccionario = {
    "nombre": "Juan",
    "edad": 30
}

#Lista de json o diccionarios
[{},{},{}]

# ¿Cómo convertir un objeto a JSON?
# vars(objeto) -> diccionario
# json.dumps(diccionario) -> json
json_str = json.dumps(vars(persona))
print("Objeto convertido a JSON:", json_str)

# ¿Cómo convertir un JSON a objeto?
# json.loads(json) -> diccionario
# Clase(**diccionario) -> objeto
diccionario = json.loads(json_str)
nueva_persona = Persona(**diccionario)
print("Nombre de la nueva persona:", nueva_persona.nombre)

# Escribir en un archivo
nombre_archivo = "datos_persona.json"
try:
    with open(nombre_archivo, 'w') as archivo:
        json.dump(vars(persona), archivo)
    print(f"Datos guardados correctamente en {nombre_archivo}.")
except IOError as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

# Leer de un archivo
try:
    with open(nombre_archivo, 'r') as archivo:
        datos_leidos = json.load(archivo)
        persona_leida = Persona(**datos_leidos)
        print(f"Datos leídos del archivo: {persona_leida.nombre}, {persona_leida.edad}")
except FileNotFoundError:
    print("El archivo no existe.")
except json.JSONDecodeError:
    print("Error en el formato del JSON.")
except Exception as e:
    print(f"Se produjo un error al leer el archivo: {e}")
