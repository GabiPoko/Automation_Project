# 📁 Organizador de Archivos

Un script de Python que organiza automáticamente tus archivos en carpetas según su tipo de extensión. Perfecto para mantener ordenadas tus carpetas de Descargas o cualquier directorio con archivos dispersos.

## 🚀 Características

- **Organización automática**: Clasifica archivos por tipo (imágenes, documentos, videos, música, etc.)
- **Múltiples categorías**: Soporta 7 categorías principales con más de 20 tipos de archivo
- **Carpeta personalizable**: Permite organizar Downloads o cualquier carpeta que elijas
- **Seguro**: No sobrescribe archivos existentes y permite confirmar antes de ejecutar
- **Registro detallado**: Muestra qué archivos se movieron y cuántos se procesaron

## 📋 Categorías de Archivos

El script organiza los archivos en las siguientes categorías:

| Categoría | Extensiones |
|-----------|-------------|
| **Imágenes** | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg`, `.webp` |
| **Documentos** | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.xls`, `.pptx`, `.ppt` |
| **Videos** | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm` |
| **Música** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a` |
| **Comprimidos** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| **Programas** | `.exe`, `.msi`, `.deb`, `.dmg`, `.app` |
| **Código** | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.php` |
| **Otros** | Cualquier archivo que no coincida con las categorías anteriores |

## 🛠️ Requisitos

- Python 3.6 o superior
- No requiere bibliotecas externas (usa solo módulos estándar de Python)

## 📖 Cómo usar

### 1. Descarga el script
```bash
git clone https://github.com/tu-usuario/Automation_project.git
cd Automation_project
```

### 2. Ejecuta el script
```bash
python organizador_de_archivos.py
```

### 3. Sigue las instrucciones
El script te guiará paso a paso:

1. **Selecciona la carpeta a organizar:**
   - Opción 1: Carpeta Downloads (automática)
   - Opción 2: Carpeta personalizada (escribes la ruta)

2. **Confirma la operación:**
   - El script te mostrará la carpeta seleccionada
   - Confirma si deseas proceder con la organización

3. **Observa los resultados:**
   - Ve en tiempo real qué archivos se están moviendo
   - Recibe un resumen final con estadísticas

## 💡 Ejemplo de uso

```
ORGANIZADOR DE ARCHIVOS
==============================

Opciones de carpeta:
1. Carpeta Downloads (tu carpeta de descargas)
2. Carpeta personalizada (escribe la ruta)

Elige una opcion (1 o 2): 1

Carpeta objetivo: C:\Users\Usuario\Downloads

Deseas organizar los archivos? (s/n): s

Iniciando organizacion...
Organizando 15 archivos en C:\Users\Usuario\Downloads
--------------------------------------------------
MOVIDO: foto.jpg -> Imagenes/
MOVIDO: documento.pdf -> Documentos/
MOVIDO: video.mp4 -> Videos/
MOVIDO: cancion.mp3 -> Musica/
...
--------------------------------------------------
Organizacion completada:
   Archivos movidos: 12
   Archivos ignorados: 3
   Total procesados: 15
```

## 🔒 Características de seguridad

- **No sobrescribe archivos**: Si ya existe un archivo con el mismo nombre, lo omite
- **Ignora el script**: No mueve el propio script `organizador_de_archivos.py`
- **Confirmación del usuario**: Siempre pide confirmación antes de mover archivos
- **Manejo de errores**: Captura y reporta errores sin detener el proceso

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si quieres:

- Agregar nuevas categorías o extensiones
- Mejorar la funcionalidad
- Reportar bugs
- Sugerir mejoras

Siéntete libre de abrir un issue o enviar un pull request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## 👨‍💻 Autor

**Automation Project** - Proyecto de automatización desarrollado para mantener organizados los archivos de manera eficiente.

---

⭐ ¡Si te resulta útil este proyecto, no olvides darle una estrella!