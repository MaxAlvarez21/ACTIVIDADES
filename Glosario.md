# Lista de comandos:

## Bash

### Comandos
- **`pwd`**: Imprime directorio de trabajo (ruta actual).
- **`clear`**: Limpia la terminal.
- **`help`**: Se usa junto con un comando para saber como se usa y su funcion.
- **`cd`**: Cambia de directorio, se acompaña con el directorio al cual se desea cambiar.
- **`cd ..`**: Va al directorio de atras.
- **`mkdir`**: Crea un directorio, se acompaña junto con el nombre del directorio.
- **`>`**: Agrega texto o el resultado de un comando a un archivo, si ya existe texto ahi, lo borra.
- **`>>`**: Agrega texto manteniendo el anterior.
- **`touch`**: Crea archivo, se acompaña con el nombre del archivo.
- **`rd -rf`**: Borra un directorio (-rf: recursividad).
- **`cat`**: Imprime lo que esta escrito en un archivo.
- **`echo`**: Imprime un mensaje en la pantalla, se acompaña del mensaje.
- **`ls -a, -l, -al`**: Muestra los archivos, (-a: muestra lo oculto, -l: muestra atributos, -al: ambos)
- **`history`**: Muestra el historial de comandos usados.
- **`!numero`**: Pone la instrucción del indice del historial.
- **`alias NombreDelAlias = ´instrucciones a realizar`**: Crea un alias con esa instruccion, alias sin opciones muestra los alias existentes.
- **`mv`**: Cambia el nombre de un archivo, se acompaña del nombre actual y del nuevo nombre.
- **`code ruta/archivo`**: Abre VSC con la ruta o el archivo.
- **`exit`**: Cierra sesion/terminal.
- **`explorer`**: Abre el explorador de archivos en la ruta escrita (se acompaña con la ruta)
- **`python --version`**: Imprime la version de Python.
- **`python archivo.py`**: Ejecuta archivo en Python.

## GIT
Configuracion antes de realizar algun commit
~~~
git config --global user.name = "Nombre"
git config --global user.email = "correo@dominio.com"
~~~

- **`git status`**: Muestra estatus de git.
- **`git diff`**: Muestra cambios.
- **`git init`**: Inicia proyecto.
- **`git add`**: Se acompaña de un archivo o de . Agrega el/los archivo/s al staying area.
- **`git commit -m "mensaje"`**: Crea un commit, se le debe agregar un comentario entre las comillas.
- **`git restore -–staged`**: Se regresa al último commit guardado.
- **`git clone`**: Clona el repositorio de un link (se acompaña con el link).
- **`git commit -am “mensaje”`**: Subir cambios al commit sin pasar por staying.
- **`git branch`**: Crea una nueva rama (se acompaña del nombre de la rama).
- **`git checkout`**: Cambia de una rama a otra ya existente (se acompaña de la rama a la que se quiere cambiar).
- **`git merge`**: Fusiona 2 ramas, (se acompaña de la rama que se quiere anexar a la rama en la que estamos)
- **`git remote add origin `**: Agregar un conexión remota (se acompaña del link de la rama).
- **`git remote show origin`**: Muestra la conexion remota.
- **`git log --oneline --all --graph --decorate`**: Muestra todos los registros de commit de todas las ramas decorado en una grafica, cada rama en una linea.
- **`git push -u origin main/--all`**: Hace un commit a a la conexion remota, sube toda la rama actual, con --all sube todas las ramas.
- **`git fetch origin main`**: Obtiene los datos del repositorio remoto, y los agrega a la rama espejo.
- `git rm --cache`: elimina el cache de los proyectos.

