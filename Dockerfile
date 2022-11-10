# Imagen base
FROM python:3
# Directorio de trabajo
WORKDIR /code
# Copiar archivo de dependencias
COPY requirements.txt /code/
# Instalación de dependencias
RUN pip install -r requirements.txt
# Hacer copia del código a el directorio de trabajo
COPY . /code/
