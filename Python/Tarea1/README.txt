Número de Cuenta: 61611100
Alumno: Oscar Alejandro Andnino Rodríguez
Nombre del proyecto: passwordGenerator

====================Explicación====================
La función del software es generar una contraseña de
15 caracteres de los cuales se componen de la tabla
ASCCI en el rango 33 al 125 sin repetirse.

** Importar librerías
Se importo la librería random para generar los caracteres al azar y la librería string para llamar la cadena que contiene los caracteres ASCII.
---------------- 
import random
import string
----------------

** Crear función
------------------------
def passwordGenerator():
------------------------

**Variables / Listas
Se utilizó una variable string vacía denominada S para almacenar la contraseña
----------------------------------------
    s = ""
-----------------------------------------
Utilización de lista con caracteres ASCII
------------------------------------------
    caracteres = list (string.printable)
------------------------------------------
Se condiciona la lista para evitar tomar los ultimos caractes ya que no forman parte
de los ASCII solicitados
----------------------------------------
    caracteres = caracteres[:-6]
----------------------------------------

** Ciclos
Utilización de Ciclo for para generar clave de 15 caracteres.
--------------------------------------
    for i in range(15):
        s += random.choice(caracteres)
---------------------------------------

** Salida por pantalla
Utilización de comando print para dar la salida por pantalla del nuevo password
--------------------------
    print (s)
--------------------------

** Main
Se  crea el método main donde se ejecutará la función que genera las contraseñas

--------------------------------------------
def main():
    #Llamar función que genera el password
    passwordGenerator()

if __name__ == '__main__':
    main()
--------------------------------------------
