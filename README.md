# FAST_API

## Acerca del proyecto:
Este proyecto está basado en Python 3.12.7, implementando FastAPI V0.115.5.
Es un CRUD (Create Read Update Delete) tragos donde se pueden agregar, leer, modificar o borrar datos de nuevos tragos en una base de datos para lograr la persistencia de los mismos.
Utiliza alembic como dependencia de terceros para realizar la gestion de migraciones de la base de datos.
Utiliza SQLAlchemy como ORM para gestionar las consultas a la base de datos.
 
### Pasos a seguir para su funcionamiento
#### 1. Crear un entorno virtual
Se debe ejecutar la siguiente linea de código por terminal ubicado sobre la carpeta raiz del proyecto
python -m  venv env
Luego para activarlo se ejecuta:
env\Scripts\activate
Para desactivarlo (solo de ser necesario) se ejecuta:
deactivate

#### 2. Instalar dependencias de terceros
Una vez creado el entorno virtual (Ver paso 1 y no ejecutar el comando "deactivate")
Se debe ejecutar la siguiente linea de código por terminal ubicado sobre la carpeta raiz del proyecto
pip install -r .\requirements.txt

#### 3. Ejecutar el programa
Se debe ejecutar la siguiente linea de código por terminal ubicado sobre la carpeta raiz del proyecto
python main.py

##### 3.1 Docker
Instalar y poner en funcionamiento Docker para levantar nuestra base de datos

Configuración:
1_ Abrimos Docker
2_ Ejecutamos por terminal: docker pull postgres:17.0 
3_ Dentro de Docker en la pestaña "Images" buscamos Postgres
4_ Tocamos el botón "Run"
5_ Desplegamos "Optional Settings":
    . Container name: tragos-db
    . HostPort: se puede dejar el 5432 como defecto o si esta en uso levantarlo en otro puerto Ej 5433
    . Host path: ... (buscar carpeta donde se guarda la base de datos click en los 3 puntos)
    . Conteiner path: /var/lib/posgresql/data
    . Variable: POSTGRES_DB         Valor:tragos_db (setear en DBeaver)
    . Variable: POSTGRES_USER       Valor: root (setear en DBeaver)
    . Variable: POSTGRES_PASSWORD   Valor: **** (setear en DBeaver)
6_ RUN

##### 3.2 DBeaver
Instalar y poner en funcionamiento DBeaver para ver nuestra base de datos y que se conecte con nuesta API

Configuración: 
1_ Vamos a: Nueva Conexión o (Ctrl + Shift + N)
2_ Elegimos: PostgreSQL
3_ Configuramos la conexión:
    Conect by host (*)
    Host: localhost Port: (el mismo que definimos en Docker)
    Database: (el nombre de la db como se definio en Docker)
    Nombre de usuario:(como se definio en Docker)
    Contraseña: (como se definio en Docker)
4_ Probar conexión
5_ Finish

#### 4. Menu principal
Al ejecutar el comando del punto anterior la terminal nos devuelve el siguiente mensaje:
    Conexión a la base de datos exitosa 
    INFO:     Application startup complete.
Lo cual indica que el programa se esta ejecuntado.

se puede ungresar a la siguiente url http://127.0.0.1:9000/docs
para poder interactuarl con el CRUD

#### 5. Notas
##### 5.1 Usar Alembic

Comandos por consola parados en la carpeta del repo agregar alembic al archivo requirements.txt

1_ Activar el entorno virtual
env\Scripts\activate

2_ Instalar las dependencias de terceros del archivo requirements.txt
pip install -r requirements.txt

3_ Verificar que la dependencia este instalada correctamente
pip list

4_ Inicializar alembic en el proyecto (crea automaticamente la carpeta migrations)
alembic init migrations

5_ Agregar mensajes para el registro de modificaciones
alembic revision --autogenerate -m "init database"

6_ Implementar la ultima modificación realizada
alembic upgrade head

## Propietario:
Araya, Pablo.