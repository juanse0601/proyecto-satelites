import catalogo
import satelite
import funciones_base


def contar_por_tipo(satelites:list) -> dict:
    """
    Esta funcion guarda los 4 grupos LEO MEO GEO HEO
    como clave en un diccionario y como valor se cuenta
    cuantos satelites pertenecen a cada grupo.
    """
    diccionario={}
    for satelite in satelites:
        if satelite.tipo_orbita() not in diccionario:
            diccionario[satelite.tipo_orbita()]=1
        else:
            diccionario[satelite.tipo_orbita()]+=1
    return diccionario

def mas_bajo(satelites:list):
    """
    Esta funcion busca el satelite que tiene menor altitud
    y devuelve el objeto satelite
    """
    menor=satelites[0].altitud_km
    salida=satelites[0]
    for satelite in satelites:
        if satelite.altitud_km<menor:
            menor=satelite.altitud_km
            salida=satelite
    return salida

def mas_alto(satelites):
    """
    Esta funcion busca el satelite que tiene mayor altitud
    y devuelve el objeto satelite
    """
    mayor=satelites[0].altitud_km
    salida=satelites[0]
    for satelite in satelites:
        if satelite.altitud_km>mayor:
            mayor=satelite.altitud_km
            salida=satelite
    return salida

def en_zona(satelites:list, zona:tuple) ->list:
    """
    Esta funcion busca los satelites que esten
    dentro de la zona. 
    La zona esta definida por 4 cordenadas dentro
    de una tupla.
    Devuelve una lista con todos los satelites dentro
    de la zona
    """
    lista=[]
    for satelite in satelites:
        if satelite.esta_en_zona == True:
            lista.append(satelite)
    return lista

def ordenar_por(satelites:list,atributo:str,descendente=False)->list:
    """
    Recibe una lista y un atributo con la que ordenar la lista
    Devuelve la lista ordenada de mayor a menor si descendente=True
    En caso de descendente=False devuelve la lista ordenada
    segun el atributo de menor a mayor
    """
    lista_ordenada=sorted(satelites,key=lambda satelite:getattr(satelite,atributo),reverse=descendente)
    return lista_ordenada

def top_n(satelites:list,n:int,mas_altos=True)->list:
    """
    Usando la funcion ordenar_por devolvemos una lista
    con los n satelites con mayor altitud en caso de que
    mas_altos sea True en caso de ser False devuelve los n mas bajos
    """
    if mas_altos==True:
        lista_ordenada=ordenar_por(satelites,'altitud_km',True)
    else:
        lista_ordenada=ordenar_por(satelites,'altitud_km',False)
    return lista_ordenada[:n]

def resumen_por_grupo(satelites:list) -> dict:
    """
    Esta funcion crea un diccionario con los grupos
    como clave y sus alittudes en una lista como valor
    Luego usando ese diccionario creamos otro diccionario que 
    tiene los grupos como clave y un diccionario con datos de las
    altitudes(cantidad,minima,maxima,media).
    """
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