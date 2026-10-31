import matplotlib
import skyfield
import os
import sys
import json
import funciones_base

class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud
        self.altitud_km=altitud_km

    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""
        if self.altitud_km<2000:
            return "LEO"
        elif self.altitud_km>=2000 and self.altitud_km<34000:
            return "MEO"
        elif self.altitud_km>=34000 and self.altitud_km<=37000:
            return "GEO"
        elif self.altitud_km>37000:
            return "HEO"
        
    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""
        estado=False   # lon_min, lat_min, lon_max,  lat_max
        if self.longitud >= zona[0] and self.longitud <= zona[2] and self.latitud >= zona[1] and self.latitud <= zona[3]:
            estado=True
        return estado
        
    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""
        return f"{self.nombre} | {self.tipo_orbita()} | Altitud:{self.altitud_km}"

def crear_satelites(registros:list, momento) -> list:
    """
    Usando la clase Satelite creamos objetos satelites y los guardamos dentro de una lista
    Los satelites deben estar a una altura mayor o igual a 100, de esta forma no guardamos
    satelites que hayan caido
    """
    satelites = []   # lista de objetos satélite
    for registro in registros:
        objeto = funciones_base.crear_objeto_skyfield(registro)
        latitud, longitud, altitud_km = funciones_base.obtener_posicion(objeto, momento)
        if altitud_km >= 100:  # que no se haya caído!
            satelites.append(  Satelite(registro["OBJECT_NAME"], latitud, longitud, altitud_km) )
    return satelites
    