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
        if altitud_km<2000:
            return "LEO"
        elif altitud_km>=2000 and altitud_km<34000:
            return "MEO"
        elif altitud_km>=34000 and altitud_km<=37000:
            return "GEO"
        elif altitud_km>37000:
            return "HEO"
        
    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""
        estado=False
        BARILOCHE = (-76.30, -46.13, -66.30, -36.13)   # lon_min, lat_min, lon_max,  lat_max
        if longitud >= zona[0] and longitud <= zona[2] and latitud >= zona[1] and latitud <= zona[3]:
            estado=True
        return estado
        
    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""
        print(f"{nombre} | {tipo_orbita} | Estado de zona:{esta_en_zona((-76.30, -46.13, -66.30, -36.13))} ")

def crear_satelites(registros, momento):
    """Devuelve una lista de objetos Satelite con su posición en `momento`."""
    lista=[]
    for i in registros:
        pass
    