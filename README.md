# Sistema de Gestión de Hotel

## Video propio con lo necesario para entender el código
https://youtu.be/Hzg-vTeyEN4

## Descripción
Este repositorio contiene la solución a la tarea de gestión de hotel realizada para el taller de programación. El sistema desarrollado es orientado a objetos y permite la administración de habitaciones de un hotel, facilitando la adición de nuevas habitaciones y la consulta de su estado. Además, cuenta con una clase `GestorArchivos` que maneja la persistencia de los datos mediante operaciones de lectura y escritura en archivos JSON.

## Funcionalidades
- **Agregar habitaciones**: Permite ingresar nuevas habitaciones especificando su número, tipo y estado actual.
- **Consultar habitación**: Permite consultar el estado de una habitación existente mediante su número.
- **Guardar y cargar datos**: Las habitaciones agregadas se guardan en un archivo JSON y se cargan al iniciar el programa para mantener persistencia de los datos.

## Estructura de Clases
- `Hotel`: Gestiona las operaciones relacionadas con las habitaciones.
- `Habitacion`: Define las propiedades de las habitaciones.
- `GestorArchivos`: Se encarga de la persistencia de datos, guardando y cargando las habitaciones desde un archivo JSON.
