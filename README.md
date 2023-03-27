Ci sono due modalità per eseguire la seguente applicazione:

# Modalità con Docker e Docker Compose

Come prerequisito bisogna installare nella propria macchina:

- Docker
- Docker Compose

Per installare Docker su Mac seguire questo link [Docker x Mac](https://docs.docker.com/desktop/install/mac-install/)
Per installare Docker su Windows seguire questo link [Docker x Windows](https://docs.docker.com/desktop/install/windows-install/)
Per installare Docker su Linux seguire questo link [Docker x Linux](https://docs.docker.com/desktop/install/linux-install/)

Per installare Docker Compose seguire la seguente guida [Docker Compose](https://docs.docker.com/compose/install/)

fatto ciò basterà eseguire pochi comandi per far partire l'applicativo e non bisognerà installare nè Mysql, nè Python nè le librerie
che sono necessarie al funzionamento dell'app.

## Next Step

una volta scaricato il repo, basterà digitare quanto segue:

```bash 
$ docker compose up -d
```

Docker si occuperà di fare il resto (installerà il Container di Mysql ed installerà il Container con l'applicativo scritto in Python)

Una volta terminato il processo di installazione bisognerà digitare quanto segue:

```bash 
$ docker compose exec -it $(docker ps -a --filter 'name=python' --format "{{.Names}}") sh
```
oppure

```bash 
$ docker exec -i -t $(docker ps -a --filter 'name=python' --format "{{.ID}}") sh
```

questo comando ci porterà all'interno del container dove c'è l'applicativo scritto in python.

una volta dentro basterà digitare il seguente comando:

```bash 
$ python3 main.py
```

e verrà eseguito l'applicativo (Verranno create le tabelle, popolate con i valori, eseguite le istruzioni di CRUD)


# Modalità senza Docker e Docker Compose

nella modalità senza Docker e Docker compose, partiamo con l'assunto che dovranno essere già installate quanto segue:

- Mysql
- Python3
- pip

## Installazione pacchetti

per far funzionare l'applicazione bisognerà installare quanto segue: 

```bash 
$ pip install sqlalchemy
```
```bash 
$ pip install PyMySQL
```
```bash 
$ pip install python-dotenv
```

Nella cartella mysql-db c'è il file init.sql dove crea il database di nome `ecommerce`.

## Eseguire l'applicazione in Python

dopo aver creato il database di nome `ecommerce` sarà possibile lanciare il seguente comando:

```bash 
$ python3 /sql-py/main.py
```

### NB

per easy reference all'interno del repository troverà anche i ddl-mysql.sql ed il dml-mysql.sql contenenti le istruzioni sql
per la creazione delle tabelle con relativi indici (ddl-mysql.sql) e con il Seed delle relative tabelle (dml-mysql.sql) che
altro non è che le istruzioni SQL per l'inserimento dei dati all'interno delle tabelle.
Lato applicativo le seguenti istruzioni sono da ricercare all' interno della cartella "sql-py/commandInsert/insertValue.py"

