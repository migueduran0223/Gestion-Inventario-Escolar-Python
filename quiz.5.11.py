import csv
import os

def gestión_inventario_escolar():
    archivo_db='inventario_escolar.csv'

    inventario={
        "lapices": 50,
        "cuadernos": 20,
        "reglas": 15,
        "borradores": 30
    }

    print("Control de Inventario Escolar")
    try:
        while True:
            print("1. Agregar/Editar Artículo")
            print("2. Eliminar Artículo")
            print("3. Mostrar Todo")
            print("4. Salir")
            opcion=input("Seleccione una opción: ").strip()

            if opcion=="1":
                articulo=input("Nombre del artículo: ").strip().lower()
                cantidad=input("Cantidad:{articulo} ").strip()

                if not articulo or not cantidad:
                    raise ValueError("El nombre y la cantidad son obligatorios")
                
                inventario[articulo]=int(cantidad)
                print(f"{articulo.capitalize()} procesado correctamente.")

            elif opcion=="2":
                articulo=input("Nombre del artículo a eliminar: ").strip().lower()
                if articulo in inventario:
                    del inventario[articulo]
                    print(f"{articulo.capitalize()} eliminado correctamente.")
                else:
                    print(f"{articulo.capitalize()} no encontrado en el inventario.")

            elif opcion=="3":
                if inventario:
                    print("Inventario Actual:")
                    for articulo, cantidad in inventario.items():
                        print(f"{articulo.capitalize()}: {cantidad}")
                else:
                    print("El inventario está vacío.") 

            elif opcion=="4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    except ValueError as e:
        print(f"Error de entrada: {e if str(e) else 'La cantidad debe ser un número'}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    finally:
        print("Programa finalizado.")

       
gestión_inventario_escolar()
