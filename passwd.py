#!/user/bin/python
# -*- coding: utf-8 -*-
fichero = open("/etc/passwd", "r")
lista = fichero.readlines()
fichero.close()
diccionario = {}
for linea in lista:
    diccionario[linea.split(":")[0]]  = linea[0:-1]
try:
    print diccionario['root']
    print diccionario['Imaginario']
except KeyError as e: 

   print "Error en la clave del diccionario:", e
