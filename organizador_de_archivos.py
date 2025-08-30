#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Organizador de Archivos
Autor: Automation Project
Descripcion: Script que organiza archivos en carpetas segun su extension
"""

import os
from pathlib import Path


# Configuracion de carpetas y categorias
def obtener_carpeta_objetivo():
    """Obtiene la carpeta objetivo donde organizar archivos"""
    print("\nOpciones de carpeta:")
    print("1. Carpeta Downloads (tu carpeta de descargas)")
    print("2. Carpeta personalizada (escribe la ruta)")
    
    opcion = input("\nElige una opcion (1 o 2): ").strip()
    
    if opcion == "1":
        return Path.home() / "Downloads"
    elif opcion == "2":
        ruta = input("Escribe la ruta de la carpeta a organizar: ").strip()
        carpeta = Path(ruta)
        
        if not carpeta.exists():
            print(f"Error: La carpeta '{ruta}' no existe.")
            return None
        
        if not carpeta.is_dir():
            print(f"Error: '{ruta}' no es una carpeta.")
            return None
            
        return carpeta
    else:
        print("Opcion no valida.")
        return None


# Definir categorias de archivos segun su extension
CATEGORIAS = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programas": [".exe", ".msi", ".deb", ".dmg", ".app"],
    "Codigo": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"],
}


def crear_mapeo_extensiones():
    """
    Crea un diccionario que mapea cada extension a su categoria
    Esto hace mas eficiente la busqueda de categoria por extension
    """
    extension_a_categoria = {}
    
    for categoria, extensiones in CATEGORIAS.items():
        for ext in extensiones:
            # Convertimos a minusculas para hacer coincidencias case-insensitive
            extension_a_categoria[ext.lower()] = categoria
    
    return extension_a_categoria


def organizar_archivos(carpeta_objetivo):
    """
    Organiza los archivos de la carpeta objetivo en subcarpetas segun su tipo
    
    Args:
        carpeta_objetivo (Path): Ruta de la carpeta a organizar
    """
    # Verificar que la carpeta existe
    if not carpeta_objetivo.exists():
        print(f"Error: La carpeta {carpeta_objetivo} no existe.")
        return
    
    if not carpeta_objetivo.is_dir():
        print(f"Error: {carpeta_objetivo} no es una carpeta.")
        return
    
    # Crear el mapeo de extensiones
    extension_a_categoria = crear_mapeo_extensiones()
    
    # Obtener todos los archivos (no directorios) de la carpeta
    archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
    
    if not archivos:
        print("No se encontraron archivos para organizar.")
        return
    
    print(f"Organizando {len(archivos)} archivos en {carpeta_objetivo}")
    print("-" * 50)
    
    archivos_movidos = 0
    archivos_ignorados = 0
    
    for archivo in archivos:
        # Obtener la extension del archivo
        extension = archivo.suffix.lower()
        
        # Ignorar el script actual para evitar moverlo
        if archivo.name == "organizador_de_archivos.py":
            print(f"Ignorando el script: {archivo.name}")
            archivos_ignorados += 1
            continue
        
        # Determinar la categoria del archivo
        categoria = extension_a_categoria.get(extension, "Otros")
        
        # Crear la carpeta de destino si no existe
        carpeta_destino = carpeta_objetivo / categoria
        carpeta_destino.mkdir(exist_ok=True)
        
        # Construir la ruta completa del destino
        ruta_destino = carpeta_destino / archivo.name
        
        # Verificar si ya existe un archivo con el mismo nombre
        if ruta_destino.exists():
            print(f"Ya existe: {archivo.name} en {categoria}/")
            archivos_ignorados += 1
            continue
        
        try:
            # Mover el archivo
            archivo.rename(ruta_destino)
            print(f"MOVIDO: {archivo.name} -> {categoria}/")
            archivos_movidos += 1
            
        except Exception as e:
            print(f"Error moviendo {archivo.name}: {e}")
            archivos_ignorados += 1
    
    # Resumen final
    print("-" * 50)
    print(f"Organizacion completada:")
    print(f"   Archivos movidos: {archivos_movidos}")
    print(f"   Archivos ignorados: {archivos_ignorados}")
    print(f"   Total procesados: {len(archivos)}")


def main():
    """Funcion principal del programa"""
    print("ORGANIZADOR DE ARCHIVOS")
    print("=" * 30)
    
    # Obtener la carpeta objetivo
    carpeta_objetivo = obtener_carpeta_objetivo()
    
    # Verificar si se obtuvo una carpeta valida
    if carpeta_objetivo is None:
        print("No se pudo obtener una carpeta valida. Programa terminado.")
        return
    
    print(f"\nCarpeta objetivo: {carpeta_objetivo}")
    
    # Preguntar al usuario si quiere continuar
    respuesta = input("\nDeseas organizar los archivos? (s/n): ").lower().strip()
    
    if respuesta in ['s', 'si', 'si', 'y', 'yes']:
        print("\nIniciando organizacion...")
        organizar_archivos(carpeta_objetivo)
    else:
        print("Operacion cancelada por el usuario.")


if __name__ == "__main__":
    main()
