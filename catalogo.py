import matplotlib
import skyfield
import os
import sys
import json

#Carga los registros a una lista
#ruta=".\datos\satelites.json"
def leer_satelites(ruta:str) -> list:
	try:
		with open(ruta,'r',encoding='utf-8') as f:
			registros=json.load(f)
						
		return registros
	except FileNotFoundError:
		print("No se encontro el archivo")
		return []

#Lee fecha de un registro
def anio_lanzamiento(registro:dict) -> int:
	ob_id=registro["OBJECT_ID"]
	if len(ob_id) < 4:
		print("Ocurrio un error al leer la fecha")
	anio= int(ob_id[:4])
	return anio

#Buscar a que grupo pertenece nombre
def grupo(nombre:str):
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
	cantidad={}
	for i in range(0,len(registros)):
		if grupo(registros[i]["OBJECT_NAME"]) not in cantidad:
			cantidad[grupo(registros[i]["OBJECT_NAME"])] = 1
		else:
			cantidad[grupo(registros[i]["OBJECT_NAME"])] +=1
	return cantidad
	
def lanzamiento_por_anio(registros):
	anios={}
	for i in range(0,len(registros)):
		if anio_lanzamiento(registros[i]) not in anios:
			anios[anio_lanzamiento(registros[i])]=1
		else:
			anios[anio_lanzamiento(registros[i])]+=1
	return anios
		
	
