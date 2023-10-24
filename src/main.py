# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV

import os, datetime




path = '/workspaces/oscar-exercise-terminal-challenge/'

def list_all(path):
    contenido = os.listdir(path)
    print(path)
    for file in contenido:
        low_path = os.path.join(path,file)
        size = os.path.getsize(low_path) 
        last_time = os.path.getmtime(low_path)
        cool_date = datetime.datetime.fromtimestamp(last_time)
        if os.path.isdir(low_path):
            list_all(low_path)
        else:
            print("\t",file, "\t", size, "\t", cool_date)
list_all(path)

