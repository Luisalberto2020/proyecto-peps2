<h1>Producion</h1>
Levantar el proyecto  docker-compose.yml
```
docker-compose up -d 
```
<b>Si es la primera vez que arrancas la aplicacion descomenta la función de crear tablas del archivo app.py</b>
<h1>Desarrollo</h1>
Necesario utilizar  dev-container del vscode para levantar el proyecto
En caso de trabajar con el server abriremos esa  carpeta en el vscode o en caso de trabajar con angular  abriremos esa carpeta en el vscode. Una vez abierta la carpeta en el vscode nos aparecera un boton en la parte inferior derecha que dice "Reopen in container" le damos click y se nos abrira el proyecto en el dev-container.
<img src="./imagenes-docs/containers.png" alt="Girl in a jacket" >



<h2>Estructura del proyecto</h2>
Aqui encontramos dos carpetas principales:
<h3>Server</h3>
Es la api de python que se encarga de hacer las consultas a la base de datos y devolver los datos en formato json
<br>
<br>
<h4>Estructura</h4>
<b>Repository</b> : Aqui encontramos los archivos que se encargan de hacer las consultas a la base de datos
<br>
<b>Service</b> : Aqui encontramos los archivos que se encargan de hacer las consultas a los repositorios
<br>
<b>Controller</b> : Aqui encontramos los archivos que se encargan de hacer las consultas a los servicios
<br>
<b>app.py</b> : Archivo principal de la api
<br>
<b>Model</b> : Aqui encontramos los archivos que se encargan de los modelos de la base de datos (no dejan de ser clases)

<h3>Angular</h3>
Es la aplicacion de angular que se encarga de consumir los datos de la api y mostrarlos en una aplicación web con ficheros estaticos solo son <b>css html y javascript </b>
<br>
<br>
<b>Aqui en el proyecto nos fijamos solo en la carpeta de src </b> ya que es donde se encuentra toda la logica de la aplicacion y el html
<br>
<br>
<h4>Estructura</h4>
<b>Assets</b> carpeta donde iran las imagens y otros ficheros
<br>
<b>Components</b> carpeta donde iran los componentes (trozos de html )  de angular dentro de aqui hay subcarpetas con las url de la aplicacion web y a su vez subcarpetas con los componentes de cada url
<br>
<b>Models</b> carpeta donde iran los modelos de los datos que se van a utilizar en la aplicacion
que no dejan de ser clases que contienen los datos de la base de datos
<br>
<b>Services</b> carpeta donde iran los servicios que se van a utilizar en la aplicacion no dejan de ser un conjunto de funciones (utilidades) que se encargan de hacer las consultas a la api y devolver los datos que se van a utilizar en los componentes de angular ya que es acceible desde cualquier sitio de la aplicacion

<h4>Componentes</h4>
Aqui encontramos un archivo html que es el que se va a mostrar en la aplicacion web , un archivo ts que nodeja de ser javascript y los estilos usados
<br>
<h4>Urls</h4>
Para esto debemos mirar el archiivo app.module.ts que esta dentro de src/app
<img src="./imagenes-docs/rutas.png" alt="Girl in a jacket" >
Recordemos que el componentes ahi que refrerenciar <b>&ltrouter-outlet&gt &lt/router-outlet&gt</b> es donde se van a mostrar los componentes de angular
<h4>Servicios</h4>