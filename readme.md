# KERNEL / OS

`uname`

`uname -a`

# DIRECTORIOS

`pwd` Muestra directorio actual. \n

`pwd -P` Muestra directorio físico actual (útil para distinguir de links).

`cd -P` Ídem pero change-dir.

`pushd`y `popd` Para trabajar con directorios apilados.

`mount` Ver todos los directorios de montaje.

`dirname` `basename` 

# ARCHIVOS

### ls

`file` Ver info sobre tipo de archivo

`ls` Ver contenido del directorio.

`ls -a` All (muestra ocultos).

`ls -l`	List.

`ls -h` Human readable size.

`ls -lsa` Combinar.

### cat

`cat`	Ver contenido de archivo.

### less

`less`	Idem pero permite browse y search.

### head/tail

`head/tail`	Ver primeras o últimas líneas de un archivo.

`tail -f`	Queda escuchando...

### cp

`cp` Copiar archivos.

`cp -a`	Copiar directorio.

### rsync

`rsync`	Copiar archivos (más inteligente, puede resumirse).

`rsync -av`	Copiar directorio y ver progreso.

### touch

`touch` Crear archivo vacío.

Igual a `> archivo.txt`.

### stat

`stat` Ver información sobre un archivo.

### diff

`diff` Comparar dos archivos.

### md5sum

`md5sum archivo` Print or check MD5 (128-bit) checksums.

### zip

`zip` Comprimir.

`zip -r`	Comprimir directorio.

`unzip`		Descomprimir.

`zipinfo`	Ver sin descomprimir.

### tree

`tree` Árbol de directorios.

### find

`find`	Buscar archivo.

`find -mtime +5`	Más viejos que 5 días.

`find -iname`	Insensitive case, buscar por nombre.

### locate

`locate`	Buscar archivo (más rápido, necesita `updatedb`).

### ln (links)

`ln -s`  Crear un link simbólico.

### Here Documents

```
cat <<EOF
...
$VAR
...
EOF
```

o literal:

```
cat <<"EOF"
...
$VAR
...
EOF
```

# ESPACIO / DISCO

### du

`du`	Ver espacio usado.

`du -sh`	Sumar contenido, human readable.

`du -sh *` Ver cuánto pesa cada archivo y directorio.

### ncdu

`ncdu -x /`  Muestra el tamaño archivo x archivo, directorio x directorio, descendente.

### df

`df`	Ver discos y espacio disponible.

# PROCESOS / CPU

### loadavg

`cat /proc/loadavg`	Ver uso de procesador.

### ps

`ps`	Ver procesos.

`ps fax`	Ordenados como árbol.

### kill

`kill`	Mata proceso por id.

`killall`	Matar todos los procesos que compartan el nombre.

### top/htop

`top`	Ver procesos ordenados por consumo (shortcuts P M q).

`htop`	Top más tuneado (buscar, filtrar, etc, usar F1-10).

### crontab

`crontab -l` Ver cronograma de tareas.

`crontab -e` Editar cronograma.

# MEMORIA

### free

`free` Ver RAM libre.

`free -m`	Ver en megas (-g -b etc).

# TEXTO

### grep

`grep`	Filtrar por texto.

`grep -v`	Filtrar por texto (reverso).

`grep -l`	Mostrar archivos que contienen el texto.

`grep -r`	Recursivo.

### awk

`awk` Es un lenguaje.

`awk { print $2; } archivo` Imprimir la segunda columna de archivo.txt

`awk 'NR==4 { print $2; }'` Imprimir la segunda columna de la cuarta línea de archivo.txt

### sed
Stream editor

`sed REGEX|OPCIÓN ARCHIVO`

`sed 's/A/B/g' ARCHIVO` Reemplazar todas las ocurrencias de A por B (Ver REGEX).

`sed -n NÚMEROp` Mostrar línea nro NÚMERO.

`sed '/^$/d' texto.txt`  ^ es comienzo de línea, $ es final, d es delete.

### tr
Translate, squeeze, and/or delete characters from standard input, writing to standard output.

`tr -d '\n'`  Eliminar todos los CR

### diff

Comparar archivos

### uniq

Filtrar líneas repetidas

# VARIABLES ÚTILES

`$?` retorna el exit code del último programa ejecutado.

# MISC

### sleep

`sleep`	Esperar tiempo.

`sleep 1m`	Un minuto.

`sleep 1d`	Un día.

`sleep 0.5`	Medio segundo.

## HTTP

### curl

`curl` Ver contenido de una url.

`curl ifconfig.me`	Averiguar tu IP pública.

`wget` Descargar desde una url.

## FECHA y HORA 

### cal

`cal` Calendario.

`cal 11 2020`	Noviembre del 2020

### date

`date`	Fecha actual.

`date -d "+7 days"`	Mostrar fecha + 7 días.

### zona horaria

`timedatectl`

### EPOCH

`$EPOCHINSECONDS` Igual a `date +s%`.

## CALCULADORA

### bc

`bc`

## ALIAS

### alias

`alias nombre='comando'`

---

# SESIONES Y TERMINAL

### screen

`ctrl+a` +d detatch

### tmux

`tmux ls`  Ver sesiones
`tmux attach-session`  Attachear a una sesión

#### Shortcuts

`ctrl+b`

`c` crear nueva ventana.

`w` ver y seleccionar, sesiones y ventanas.

`d` detatch.

## SHORTCUTS DEL TERMINAL

`ctrl-r`	Buscar en el historial.

`ctrl-e`	Ir al final de la línea.

`ctrl-a`	Ir al comienzo de la línea.

`ctrl-ARROW`	Mover por palabras.

`ctrl-l`	Limpiar pantalla.

`ctrl+w`	Borrar última palabra.

`ESC T`		Intercambia últimas dos palabras.

`TAB`			Autocompletar.

`ctrl-z`	Llevar al background (`fg` para regresar al foreground).

# CONEXIONES

### ip

`ip address` Averiguar ip de la computadora (inet).

### ping

`ping`	Probar velocidad de comunicación.

`ping -c10`	Probar 10 respuestas y salir.

### iperf

`iperf -c localhost`

### ssh

`ssh`	Secure shell.

`ssh usuario@ip`	Conectar remotamente.

`ssh -i`	Para conectar usando una key específica.

`ssh ... 'comando'`	 Ejecuta comando.

### ssh tunneling

`ssh -L local-port:ip:ext-port usuario@ip`  Hacer un tunel local.

`ssh -L 3030:127.0.0.1:22 gede@192.168.1.159`	Conectar de la desktop, a través del puerto 3030, a la notebook de gede 
(192.168.1.159) por el puerto 22 (convencionalmente para ssh) en todas las interfaces (127.0.0.1).

### scp
Secure copy.

`scp`	Copar archivos.

`scp username@from_host:file.txt /local/directory/` O a la inversa!

`scp -r username@from_host:dir /local/` Copiar directorio recursivamente.

### sshfs
`sshfs [user@]host:[dir] mountpoint [options]`  montar un network file system

# RED

### nmap

`nmap ip`	Escanea puertos usados.

### netstat

`netstat` Ver interfaces de red.

`netstat -nr`	Ver ruteo de puertos.

`netstat -i`	Estadísticas.

`nstat -natup`	Ver todos los procesos tcp ucp.

### tcpdump

`tcpdump`	Escuchar tráfico.

`tcpdump -i any -p tcp port 80` Filtrar.

`tcpdump -i any host ip` ?

---

# ANSIBLE

`ansible-galaxy install -r requirements.yml` Instalar requirements.

`. venv/bin/activate`	Activar venv de ansible.

`ansible-playbook`	Correr libro de tareas.

`ansible-playbook site.yml --limit testproxy --tag common`	Tareas site.yml para el servidor testproxy que tengan el tag common.

---

# GIT

### Hacer un pull descartando los cambios locales

`git stash --include-untracked && git reset --hard && git clean -fd && git pull`

---

# Python

## VENV

Crear: `python3 -m venv /path/to/new/virtual/environment`

Activar: `. venv/bin/activate`

Instalar requirements: `pip install -r requirements.txt`

Ver pkgs en formato requirements: `pip freeze`

---

# REPOS de Debian

```
deb http://httpredir.debian.org/debian buster main non-free contrib
deb-src http://httpredir.debian.org/debian buster main non-free contrib

deb http://security.debian.org/debian-security buster/updates main contrib non-free
deb-src http://security.debian.org/debian-security buster/updates main contrib non-free
```

```
deb http://deb.debian.org/debian buster-backports main contrib non-free
deb-src http://deb.debian.org/debian buster-backports main contrib non-free
```
---

# AWS CLI, instalar

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
---

# IMÁGENES

Del pkg **imagemagick**, convertir png a jpg:

`mogrify -format jpg *.png`
