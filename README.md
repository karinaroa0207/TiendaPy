# TiendaPy

## Descripción

TiendaPy es un sistema de gestión para una tienda de Don Aurelio.Este gestina las compras, alertas del inventario,reportes diarios de las ventas y registrar, modificar,buscar y eliminar productos.Todo esto mediante por consola.

## Funcionalidades

- Mostrar y registrar productos.
- Buscar productos por código y categoría.
- Modificar y eliminar productos.
- Registrar ventas con varios productos.
- Calcular descuentos y cambio.
- Generar alertas de inventario bajo.
- Generar reportes diarios de ventas.
- Guardar el inventario y el historial de ventas en archivos de texto.

## Requisitos

- Python 3.12 o mas.
- Librería `tabulate`.

## Instalación

1. Clonar o descargar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Crear el entorno virtual:

   `py -m venv venv`

4. Activar el entorno virtual:

   `venv\Scripts\activate`

5. Instalar las dependencias:

   `pip install -r requirements.txt`

## Ejecución

Desde la carpeta principal del proyecto, ejecutar:

`python src/main.py`

## Estructura del proyecto

- `src/main.py`: menú principal del sistema.
- `src/inventario.py`: administración de productos.
- `src/ventas.py`: registro de ventas.
- `src/reportes.py`: alertas y reportes.
- `src/persistencia.py`: lectura y escritura de archivos.
- `src/validaciones.py`: validación de datos.
- `data/inventario.txt`: almacenamiento de productos.
- `data/ventas.txt`: historial de ventas.

## Almacenamiento de datos

El sistema utiliza archivos de texto para guardar el inventario y el historial de ventas. Los datos se conservan al cerrar y volver a ejecutar el programa.
