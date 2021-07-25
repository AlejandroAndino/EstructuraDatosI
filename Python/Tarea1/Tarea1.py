# Importar librerías
import random
import string

# Crear función de generación de password
def passwordGenerator():

    # Variable string vacía
    s = ""
    # Lista para llamar caracteres ASCII
    caracteres = list(string.printable)
    # Igualar lista de caracteres para omitir los ultimos 6
    caracteres = caracteres[:-6]
    # Ciclo for
    for i in range(15):
        # Concatenación de variable string vacia con la lista
        s += random.choice(caracteres)
    # Imprimir contenido de la lista
    print(s)

#Main
def main():
    #Llamar función que genera el password
    passwordGenerator()

if __name__ == '__main__':
    main()
