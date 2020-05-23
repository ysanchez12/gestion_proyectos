# GESTION DE PROECTOS

este es un repositorio que facilita el calculo de costos asociados a acciones unitarias dentro de un proyecto 

## Instalacion

- descargar el repositorio
- crear el entorno virtual y activar
- correr migracion y crear super usuario
- correr el servidor



### Descargar el repositorio

´´´
https://github.com/ysanchez12/gestion_proyectos.git
´´´

### Crear el entorno virtual y activar
´´´
pip install virtualenv
virtualenv venv
venv/Script/activate
´´´

### Correr migracion y crear super usuario
´´´
python manage.py migrate
python manage.py createsueperuser
´´´

### Correr el servidor
´´´
python manage.py runserver
´´´



## Modelo
un proyecto seforma a partir de una serie de actividades que son desarrolladas por una o mas trabajadores, este programa permite agilizar el calculo de presupuestos por actividad.
