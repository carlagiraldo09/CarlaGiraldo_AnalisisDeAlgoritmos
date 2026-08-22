# Entorno Virtual del Proyecto

Este proyecto utiliza un entorno virtual para aislar las dependencias necesarias de las clases.

## Configuración y Activación

Para crear y activar este entorno virtual en mi sistema (macOS) ejecuté en la raíz del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Reproducción del Entorno

Si desea clonar este repositorio y reproducir exactamente el entorno con las dependencias instaladas, asegúrese de tener activo su entorno virtual y ejecute el siguiente comando:

```bash
pip install -r requirements.txt
```