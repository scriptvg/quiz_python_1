# Lista de datos que contiene información sobre productos
datos = [
    {
        "nombre": "Zapatillas Nike Air Max",  # Nombre del producto
        "precio": 89999,  # Precio del producto
        "cantidad": 10,  # Cantidad disponible
        "marca": "Nike",  # Marca del producto
        "modelo": "Air Max",  # Modelo del producto
        "talla": [38, 39, 40, 41, 42, 43],  # Tallas disponibles
        "colores": ["Negro", "Blanco", "Rojo"],  # Colores disponibles
        "disponibilidad": True,  # Disponibilidad del producto
        "descuento": 10,  # Porcentaje de descuento
        "codigo_producto": "NKAM12345",  # Código único del producto
    },
    {
        "nombre": "Zapatillas Adidas Ultraboost",
        "precio": 79999,
        "cantidad": 15,
        "marca": "Adidas",
        "modelo": "Ultraboost",
        "talla": [38, 39, 40, 41, 42, 43, 44],
        "colores": ["Negro", "Gris", "Azul"],
        "disponibilidad": True,
        "descuento": 15,
        "codigo_producto": "ADUB67890",
    },
    {
        "nombre": "Zapatillas Puma RS-X",
        "precio": 69999,
        "cantidad": 8,
        "marca": "Puma",
        "modelo": "RS-X",
        "talla": [39, 40, 41, 42, 43],
        "colores": ["Blanco", "Verde", "Naranja"],
        "disponibilidad": True,
        "descuento": 5,
        "codigo_producto": "PMRS54321",
    },
]

import json
import os

# Función para guardar el diccionario en un archivo JSON
def guardar_diccionario(datos, archivo="productos.json"):
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)  # Guardar los datos en formato JSON con indentación
    print(f"Datos guardados exitosamente en '{archivo}'")

# Función para cargar el diccionario desde un archivo JSON
def cargar_diccionario(archivo="productos.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)  # Cargar los datos desde el archivo JSON
    except FileNotFoundError:
        # Si el archivo no existe, mostrar un mensaje y devolver None
        print(f"Archivo '{archivo}' no encontrado. Se usarán los datos predeterminados.")
        return None
    except json.JSONDecodeError:
        # Si hay un error al leer el archivo JSON, mostrar un mensaje y devolver None
        print(f"Error al decodificar '{archivo}'. Se usarán los datos predeterminados.")
        return None

# Función para modificar el diccionario de productos
def modificar_diccionario(datos):
    while True:
        # Mostrar los productos disponibles
        print("\nProductos disponibles:")
        for i, producto in enumerate(datos, 1):
            print(f"{i}. {producto['nombre']} ")  # Mostrar el índice y el nombre del producto

        # Seleccionar un producto
        try:
            indice = int(input("Seleccione el número del producto que desea modificar o eliminar (0 para salir): ")) - 1
            if indice == -1:
                print("Saliendo del programa.")  # Salir del programa si el usuario ingresa 0
                break
            if indice < 0 or indice >= len(datos):
                print("Número de producto inválido.")  # Validar que el índice sea válido
                continue
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")  # Manejar entradas no numéricas
            continue

        producto = datos[indice]  # Obtener el producto seleccionado

        # Mostrar menú de opciones
        print("\n¿Qué desea hacer con este producto?")
        print("1. Modificar una clave")  # Modificar un atributo del producto
        print("2. Eliminar una clave")  # Eliminar un atributo del producto
        print("3. Volver al menú principal")  # Volver al menú principal
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Mostrar las claves disponibles
            print("\nClaves disponibles en el producto seleccionado:")
            for clave in producto.keys():
                print(f"- {clave}")  # Mostrar todas las claves del producto

            # Solicitar clave a modificar
            clave = input("\nIngrese la clave que desea modificar: ")
            if clave in producto:
                if isinstance(producto[clave], list):  # Si el valor es una lista
                    print(f"El valor actual de '{clave}' es: {producto[clave]}")
                    print("1. Agregar un valor a la lista")
                    print("2. Modificar un valor existente en la lista")
                    print("3. Eliminar un valor de la lista")
                    sub_opcion = input("Seleccione una opción: ")

                    if sub_opcion == "1":
                        # Agregar un nuevo valor a la lista
                        nuevo_elemento = input("Ingrese el nuevo valor para agregar a la lista: ")
                        try:
                            # Convertir a entero si corresponde
                            nuevo_elemento = int(nuevo_elemento)
                            producto[clave].append(nuevo_elemento)
                            print(f"Valor '{nuevo_elemento}' agregado a la lista '{clave}'.")
                        except ValueError:
                            print("El valor ingresado no es válido. Debe ser un número entero.")

                    elif sub_opcion == "2":
                        # Modificar un valor existente en la lista
                        print(f"Valores actuales en la lista '{clave}':")
                        for i, valor in enumerate(producto[clave], 1):
                            print(f"{i}. {valor}")
                        try:
                            indice = int(input("Seleccione el número del valor que desea modificar: ")) - 1
                            if 0 <= indice < len(producto[clave]):
                                nuevo_valor = input("Ingrese el nuevo valor: ")
                                try:
                                    # Convertir a entero si corresponde
                                    nuevo_valor = int(nuevo_valor)
                                    producto[clave][indice] = nuevo_valor
                                    print(f"Valor actualizado en la lista '{clave}'.")
                                except ValueError:
                                    print("El valor ingresado no es válido. Debe ser un número entero.")
                            else:
                                print("Índice fuera de rango.")
                        except ValueError:
                            print("Entrada inválida. Debe ingresar un número.")

                    elif sub_opcion == "3":
                        # Eliminar un valor de la lista
                        print(f"Valores actuales en la lista '{clave}':")
                        for i, valor in enumerate(producto[clave], 1):
                            print(f"{i}. {valor}")
                        try:
                            indice = int(input("Seleccione el número del valor que desea eliminar: ")) - 1
                            if 0 <= indice < len(producto[clave]):
                                eliminado = producto[clave].pop(indice)
                                print(f"Valor '{eliminado}' eliminado de la lista '{clave}'.")
                            else:
                                print("Índice fuera de rango.")
                        except ValueError:
                            print("Entrada inválida. Debe ingresar un número.")
                    else:
                        print("Opción inválida.")
                else:
                    # Modificar un valor que no es una lista
                    nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}': ")
                    try:
                        # Convertir a tipo adecuado si es posible
                        if isinstance(producto[clave], int):
                            nuevo_valor = int(nuevo_valor)
                        elif isinstance(producto[clave], bool):
                            nuevo_valor = nuevo_valor.lower() in ["true", "1", "yes", "si"]
                    except ValueError:
                        print("El tipo del valor ingresado no coincide con el tipo esperado.")
                        continue

                    producto[clave] = nuevo_valor
                    print("Clave actualizada con éxito.")
            else:
                print("La clave no existe en el producto seleccionado.")

        elif opcion == "2":
            # Mostrar las claves disponibles
            print("\nClaves disponibles en el producto seleccionado:")
            for clave in producto.keys():
                print(f"- {clave}")

            # Solicitar clave a eliminar
            clave_eliminar = input("\nIngrese la clave que desea eliminar: ")
            if clave_eliminar in producto:
                del producto[clave_eliminar]  # Eliminar la clave del producto
                print("Clave eliminada con éxito.")
            else:
                print("La clave no existe en el producto seleccionado.")

        elif opcion == "3":
            print("Volviendo al menú principal.")  # Volver al menú principal
            continue
        else:
            print("Opción inválida. Intente nuevamente.")  # Manejar opciones inválidas

        # Mostrar el diccionario actualizado
        print("\nDiccionario actualizado:")
        for p in datos:
            print(p)
        
        # Guardar los cambios después de cada modificación
        guardar_diccionario(datos)

# Cargar datos desde el archivo JSON si existe, de lo contrario usar datos predeterminados
archivo_json = "productos.json"
datos_cargados = cargar_diccionario(archivo_json)

if datos_cargados:
    datos = datos_cargados  # Usar los datos cargados desde el archivo
    print(f"Datos cargados desde '{archivo_json}'")
else:
    # Si no se pudieron cargar los datos, guardar los datos predeterminados
    guardar_diccionario(datos, archivo_json)
    print(f"Datos predeterminados guardados en '{archivo_json}'")

# Llamar a la función con los datos
modificar_diccionario(datos)
