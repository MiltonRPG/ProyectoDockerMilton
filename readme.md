# ProyectoDockerMilton

Este proyecto es un microservicio desarrollado en Flask que interactúa con una base de datos MySQL. El microservicio permite la creación, consulta y obtención de items a través de una API REST.

## Requisitos Previos

Antes de empezar, asegúrate de tener instalados los siguientes programas en tu máquina:

- [Docker](https://www.docker.com/get-started) (versión 19.03 o superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versión 1.27.0 o superior)

## Estructura del Proyecto

ProyectoDockerMilton/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
├── instance/
├── logs/
├── .env
├── docker-compose.yml
├── Dockerfile
└── README.md

## Descripción de los Ficheros

app.py: Archivo principal de la aplicación Flask que define los endpoints y la lógica del servidor.
models.py: Define los modelos de la base de datos usando SQLAlchemy.
requirements.txt: Lista de dependencias de Python necesarias para el proyecto.
Dockerfile: Define cómo construir la imagen Docker para la aplicación Flask.
docker-compose.yml: Configura y orquesta los contenedores Docker para el microservicio y la base de datos MySQL.

# Instrucciones de Configuración y Ejecución
Sigue los pasos a continuación para poner en funcionamiento el microservicio:

1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

git clone <URL_DEL_REPOSITORIO>
cd ProyectoDockerMilton

2. Construir y Levantar los Contenedores

Ejecuta el siguiente comando para construir las imágenes Docker y levantar los contenedores:

docker-compose up --build

Esto levantará dos contenedores:
web: Contenedor que ejecuta la aplicación Flask.
db: Contenedor que ejecuta MySQL.

3. Verificar que los Contenedores Están Corriendo

docker-compose ps

Deberías ver algo similar a:

Name                      Command               State            Ports
-------------------------------------------------------------------------
proyectodockermilton-web-1   python app.py         Up      0.0.0.0:5000->5000/tcp
proyectodockermilton-db-1    docker-entrypoint.s…  Up      0.0.0.0:3306->3306/tcp

4. Probar la Aplicación

Puedes probar la aplicación usando curl o una herramienta como Postman.

- Crear un nuevo item:
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"name": "item1"}'

- Obtener todos los items:
curl http://localhost:5000/items

- Obtener un item por ID:
curl http://localhost:5000/items/1

5. Monitorear los Logs
Puedes ver los logs generados por la aplicación utilizando PowerShell:
Get-Content logs/log.txt -Wait

O abrir el archivo logs/log.txt en un editor de texto para monitorear la actividad de la aplicación.

6. Detener los Contenedores

Cuando hayas terminado, puedes detener y limpiar los contenedores usando:
docker-compose down

## Notas Adicionales
Asegúrate de que el puerto 5000 esté libre en tu máquina, ya que la aplicación Flask se ejecuta en ese puerto.
Puedes modificar los parámetros de la base de datos en el archivo docker-compose.yml si es necesario.

## Contribuciones
Si deseas contribuir al proyecto, por favor abre un issue o envía un pull request. ¡Toda ayuda es bienvenida!




