import matplotlib
import skyfield
import os
import sys
import json

#Carga los registros a una lista
#ruta=".\datos\satelites.json"
def leer_satelites(ruta:str) -> list:
    """
    Esta funcion lee un json en encoding utf-8 y 
    guarda en una lista los datos del satelite como
    diccionario
    """
	try:
		with open(ruta,'r',encoding='utf-8') as f:
			registros=json.load(f)
						
		return registros
	except FileNotFoundError:
		print("No se encontro el archivo")
		return []

#Lee fecha de un registro
def anio_lanzamiento(registro:dict) -> int:
    """
    Leyendo los 4 primeros digitos del OBJECT_ID
    de un satelite devuelve una fecha.
    La fecha debe tener 4 digitos en caso contrario
    imprime un aviso
    
    """
	ob_id=registro["OBJECT_ID"]
	if len(ob_id) < 4:
		print("Ocurrio un error al leer la fecha")
	anio= int(ob_id[:4])
	return anio

#Buscar a que grupo pertenece nombre
def grupo(nombre:str) -> str:
    """
    Segun como empieza el nombre de un satelite
    separamos el nombre y con la primera parte
    determinamos a que grupo pertenece.
    Los grupos estan dentro de un diccionario llamado grupos
    Las claves son la parte del nombre que leemos y la clave
    es lo que devuelve la funcion.
    En caso de no pertenecer a ningun grupo devuelve Otros
    
    """
    grupos={
        "STARLINK":"Starlink",
        "ONEWEB":"OneWeb",
        "KUIPER":"Kuiper",
        "QIANFAN":"Qianfan",
        "IRIDIUM":"Iridium",
        "GLOBALSTAR":"Globalstar",
        "NAVSTAR":"GPS",
        "BEIDOU":"BeiDou"
    }
	
    if len(nombre)>0:
        #Si esta separado por " " la lista deberia ser mayor
        if len(nombre.split(" "))>1:
            partes=nombre.split(" ")
        #Si no pruebo separando con "-"
        elif len(nombre.split("-")) >1:
            partes=nombre.split("-")
        else:
            partes=[nombre]
    else:
        return print("No hay nombre")
    
    if partes[0] in grupos:
        return grupos[partes[0]]
    else:
        return "Otros"


def contar_por_grupo(registros:list) -> dict:
    """
    Devuelve un diccionario con la cantidad de satelites que
    hay por grupo.
    el grupo es la clave y la cantidad el valor.
    """
	cantidad={}
	for i in range(0,len(registros)):
		if grupo(registros[i]["OBJECT_NAME"]) not in cantidad:
			cantidad[grupo(registros[i]["OBJECT_NAME"])] = 1
		else:
			cantidad[grupo(registros[i]["OBJECT_NAME"])] +=1
	return cantidad
	
def lanzamiento_por_anio(registros:list) -> dict:
    """
    Esta funcion devuelve un diccionario con la cantidad
    de satelites lanzados en cada año. Guarda la clave
    como el año y el valor como la cantidad
    """
	anios={}
	for i in range(0,len(registros)):
		if anio_lanzamiento(registros[i]) not in anios:
			anios[anio_lanzamiento(registros[i])]=1
		else:
			anios[anio_lanzamiento(registros[i])]+=1
	return anios
		
	
