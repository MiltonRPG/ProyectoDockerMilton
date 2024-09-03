# Usar una imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar dependencias
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar el código de la aplicación desde el directorio app/
COPY app/ /app/

# Crear un directorio para logs
RUN mkdir -p /app/logs

# Exponer el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Establecer el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]




