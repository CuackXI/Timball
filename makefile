.PHONY: setup venv install-env create-env runserver

# Instala el entorno y dependencias
setup: venv install-env create-env

# Crea entorno virtual
venv:
	@echo "🐍 Creando entorno virtual..."
	@python3 -m venv venv

# Activa el entorno e instala dependencias
install-env:
	@echo "📦 Instalando dependencias..."
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install -r requirements.txt

# Crea .env si existe la plantilla
create-env:
	@if [ -f ".env.template" ]; then \
		echo "📝 Creando .env desde .env.template..."; \
		cp .env.template .env; \
	else \
		echo "❗ .env.template no encontrado. .env no creado."; \
	fi

# Ejecutar el servidor Django
runserver:
	@venv/bin/python manage.py runserver
