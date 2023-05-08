
'''
- Hacer un programa de línea de comandos que recibe un directorio como parámetro y regresa el número de archivos que haye en el directorio

* Entrada
- Ruta: externa

* Errores:
- No existe el directorio
- No es un directorio 
- No permisos

* Medidas de manejo de errores
- Cachar excepción
- Evitar lanzar excepciones adelantándonos al error
- Relanzar excepción para que se maneje en otro lado
- Terminar el programa
- Regresar un valor neutro/error 

MVC
* Interfaz de usuario: código que tiene que ver con cosas del usuario, es la parte visual 
* lógica de negocios: 
* Manejo de datos: persistencia, querys, acceso a manejador, etc.
'''

import os
import sys

def regresar_numero_archivos(path: str) -> int: 
    '''
    regresa el número de archivos que existen en un directorio

    argumentos
    path: str ruta de un diretorio

    returns
    int número de archivos

    Errores
    FileNotFoundError: si no existe path
    PermissionError: si no hay permisos sobre el directorio path
    '''
    return len(os.listdir(path))



if __name__ == '__main__':
    # Interfaz de usuario
    ruta = sys.argv[1]
    try:
        total = regresar_numero_archivos(ruta)
        print(total)
    except FileNotFoundError:
        print('La entrada no existe')
        exit(1)
    except PermissionError:
        print('No tienes permisos sobre ese directorio')
        exit(1)
