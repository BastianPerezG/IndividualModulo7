# IndividualModulo7
En este repositorio estará todo el proyecto del módulo 7 del bootcamp Full Stack Python

Requisitos
Los requisitos de la aplicación son:

asgiref==3.7.2
Django==4.2.3
psycopg2==2.9.6
python-dotenv==1.0.0
sqlparse==0.4.4
typing_extensions==4.7.1
tzdata==2023.3

El programa está configurado para usar PostgreSQL como motor de base de datos

Instalación

Para instalar el sistema primero cree un entorno virtual mediante el comando
    python -m venv .venv

Después, active el entorno virtual
    .venv\scripts\activate

Clone el proyecto usando el archivo ZIP en

https://github.com/BastianPerezG/IndividualModulo7.git
Y descomprima el archivo en el mismo directorio donde se encuentra el directorio .venv. También puede clonar el proyecto usando git, con las indicaciones señaladas anteriormente.

y utilice el siguiente comando para instalar los requisitos de sistema:
    (.venv) píp install -r requeriments.txt


Cree un archivo .env en el directorio raíz del sistema y proporcione los datos para acceder a una base de datos de PostgreSQL:

SECRET_KEY= 'Secret_key'     # secret_key de Django
DB_ENGINE= 'django.db.backends.postgresql_psycopg2'
DB_DATABASE= 'database'      # Nombre de la base de datos
DB_USER= 'user'              # Usuario de la base de datos
DB_PASSWORD= 'password'      # Contraseña del usuario 
DB_HOST= 'host'              # Dirección del servidor PostgreSQL 
DB_PORT= '5432'              # Puerto del servidor PostgreSQL, habitualmente 5432

Finalmente para ejecutar el proyecto utilice el comando (.venv) python manage.py runserver

Estructura de directorios principales
Los directorios principales de Django son:

misTareas: Contiene las configuraciones principales, rutas, vistas
tareasApp: Contiene la aplicación interna para usuarios, modelos y relacionados

Usuarios

Superusuario
    username: admin
    email   : admin@gmail.com
    password: hola.123
Usuario
    username: rgonzalez
    email   : rgonzalez@gmail.com
    password: hola.123

