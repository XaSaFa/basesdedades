# Bases de dades

Petit projecte amb bases de dades utilitzant MariaDB.

## Instal·lar la base de dades (BBDD) Mariadb

```
sudo apt install mariadb-server
```

## Utilitzar la bbdd

Per utilitzar la bbdd hem d'entrar al programa amb la següent instrucció.

```
sudo mariadb
```

<img width="705" height="182" alt="imatge" src="https://github.com/user-attachments/assets/94cb182a-80e5-44fb-99c0-41c46e13ac23" />

## SQL

Totes les comandes dins de MariaDB utilitzen la notació SQL (Structured Query Language) amb línies que acaben en punt i coma (;).

-[Guia de referència MariaDB](https://mariadb.com/docs/server/reference)
-[Tutorials SQL](https://www.mariadbtutorial.com)

### Mostrar les bbdd de la base de dades:

```
SHOW DATABASES;
```

<img width="702" height="231" alt="imatge" src="https://github.com/user-attachments/assets/56d89bc7-3b12-4277-aecc-ed9a30991a92" />

### Crear una bbdd:

```
CREATE DATABASE nom;
```

<img width="704" height="307" alt="imatge" src="https://github.com/user-attachments/assets/76543697-f72d-4ea6-8e6a-2a3875351990" />

### Eliminar una bbdd:

```
DROP DATABASE nom;
```
<img width="703" height="282" alt="imatge" src="https://github.com/user-attachments/assets/1a3c722d-8e5e-4392-bd70-10af3dc05d91" />

### Tipus de dades a MariaDB

Dins la bbdd enmagatzenarem informació en camps, cada camp ha de ser d'un tipus de dades determinat, [aquí tens els tipus de dades que admet MariaDB](https://www.mariadbtutorial.com/mariadb-basics/mariadb-data-types/).

Per exemple, si vull una bbddd per emmagatzemar les dades d'una persona he de pensar en les dades a guardar:

- nom
- cognom1
- cognom2
- dni
- data de naixement
- ...

Després mirem de quin tipus de dades pot ser cada camp d'informació:

- nom ->
- cognom1 ->
- cognom2 ->
- dni ->
- data de naixement ->

Amb aquesta informació podré crear una taula d'informació.

### TAULES

Dins d'una bbdd la informació es divideix per taules, a cada taula es guarden camps d'informació.

Per exemple la taula persones podria ser així:

<img width="318" height="274" alt="imatge" src="https://github.com/user-attachments/assets/cf187aa6-c919-49e3-a9d8-f591fbc89f49" />

I per a crear-la la comanda que farem servir és:

```
CREATE TABLE `persones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(255) NOT NULL,
    `cognom1` VARCHAR(255) NOT NULL,
    `cognom2` VARCHAR(255) NOT NULL,
    `dni` VARCHAR(9) NOT NULL,
    `data_naixement` DATE NOT NULL
);
```

#### Primary Key

Les taules de dades moltes vegades tenen un camp anomenat PK (Primary Key), aquest camp serveix per identificar un registre (una línia d'una taula) de forma inequívoca, perque no poden existir dos valors PK iguals dins la mateixa taula.

En la taula anterior la clau principal és id, un camp que hem inventat i que es sol fer servir a totes les taules.
