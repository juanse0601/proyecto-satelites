import catalogo
import satelite
import funciones_base


def contar_por_tipo(satelites):
    diccionario={}
    for satelite in satelites:
        if satelite.tipo_orbita() not in diccionario:
            diccionario[satelite.tipo_orbita()]=1
        else:
            diccionario[satelite.tipo_orbita()]+=1
    return diccionario

def mas_bajo(satelites):
    menor=satelites[0].altitud_km
    salida=satelites[0]
    for satelite in satelites:
        if satelite.altitud_km<menor:
            menor=satelite.altitud_km
            salida=satelite
    return salida

def mas_alto(satelites):
    mayor=satelites[0].altitud_km
    salida=satelites[0]
    for satelite in satelites:
        if satelite.altitud_km>mayor:
            mayor=satelite.altitud_km
            salida=satelite
    return salida

def en_zona(satelites, zona):
    lista=[]
    for satelite in satelites:
        if satelite.esta_en_zona == True:
            lista.append(satelite)
    return lista

def ordenar_por(satelites,atributo,descendente=False):
    lista_ordenada=sorted(satelites,key=lambda satelite:getattr(satelite,atributo),reverse=descendente)
    return lista_ordenada

def top_n(satelites,n,mas_altos=True):
    if mas_altos==True:
        lista_ordenada=ordenar_por(satelites,'altitud_km',True)
    else:
        lista_ordenada=ordenar_por(satelites,'altitud_km',False)
    return lista_ordenada[:n]

def resumen_por_grupo(satelites):
    diccionario={}
    ##Creamos diccionario con lista de altitudes para luego trabjar con ellas.
    for satelite in satelites:
        nombre=catalogo.grupo(satelite.nombre)
        altitud=satelite.altitud_km
        if nombre not in diccionario:
            diccionario[nombre]=[]
        diccionario[nombre].append(altitud)
    resumen = {}
    ##Trabajamos con los datos guardados
    for nombre,altitudes in diccionario.items():
        resumen[nombre]={
            "Cantidad":len(altitudes),
            "Minima":min(altitudes),
            "Maxima":max(altitudes),
            "Media":sum(altitudes)/len(altitudes)
        }
    return resumen