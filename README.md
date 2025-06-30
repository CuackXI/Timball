# Timball

**Timball** es una página web sencilla desarrollada con **Django**. Desarrollado como proyecto personal con fines educativos.

Hace uso de un **plan gratuito** de una API de estadísticas y apuestas de fútbol. Para optimizar el consumo de requests y cuidar los límites del plan, implementa un sistema de **almacenamiento local** en una base de datos, permitiendo reutilizar los datos obtenidos previamente.

## Características

- Integración con una API externa de estadísticas de fútbol.
- Almacenamiento local para minimizar el consumo de requests.
- Backend desarrollado con Django.
- Frontend con JINJA, HTML y CSS puro.
- Aplicación monolítica
- Proyecto pensado para aprendizaje y optimización de recursos.

## Como ejecutar
```bash
make setup
source venv/bin/activate
make runserver
```

---

## ¿Cómo borrar TODO el historial de commits de un proyecto?

Puedes reiniciar el historial de commits de un repositorio con los siguientes pasos:

```bash
# 1. Borra el historial creando una rama huérfana
git checkout --orphan nueva-rama

# 2. Añade todos los archivos y haz un nuevo commit inicial
git add .
git commit -m "Commit inicial"

# 3. Borra la rama principal anterior y renombra la nueva
git branch -D main
git branch -m main

# 4. Fuerza el push al repositorio remoto (¡esto sobrescribe el historial remoto!)
git push -f origin main
```

**Advertencia:** Esto elimina todo el historial anterior. Úsalo solo si estás seguro.
