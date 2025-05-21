# PIA_LMPr
PIA de  Lenguajes Modernos de Programacion
CRUD de Catalogo de Peliculas

By Dayla Carrizales

# Archivo bash
Debido a la manera como se dan de alta los contenedores de Docker para la base de datos y la aplicacion Web en el docker-compose, a pesar de que primero se ejecuta el servicio de MySQL, no hay garantia de que cuando la applicacion Web este ejecutandose, el contenedor de la base de datos ya este ejecutandose igual. 

El archivo **wait-for-db.sh**, sirve para garantizar que ese orden se cumpla. Primero el servico de MySQL ya este corriendo y posteriormente la aplicacion Web.

# Ejecutar el project
Para una ejecucion limpia se puede ejecutar los siguientes comandos:

```
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```