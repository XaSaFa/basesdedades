# Bases de dades

Petit projecte amb bases de dades utilitzant MariaDB.

## Instal·lar la base de dades (BBDD) Mariadb

```
sudo apt update
sudo apt install mariadb-server
sudo service mariadb restart
```

## Utilitzar la bbdd

Per utilitzar la bbdd hem d'entrar al programa amb la següent instrucció.

```
sudo mariadb
```

<img width="705" height="182" alt="imatge" src="https://github.com/user-attachments/assets/94cb182a-80e5-44fb-99c0-41c46e13ac23" />

## SQL

Totes les comandes dins de MariaDB utilitzen la notació SQL (Structured Query Language) amb línies que acaben en punt i coma (;).

- [Guia de referència MariaDB](https://mariadb.com/docs/server/reference)
- [Tutorials SQL](https://www.mariadbtutorial.com)

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

Per utilitzar una taula d'una bbdd primer he de dir a MariaDB que vull utilitzar-la, amb la comanda:

USE nom_bbdd;

Exemple:

<img width="402" height="111" alt="imatge" src="https://github.com/user-attachments/assets/8127984f-5f37-45a1-a16a-dca248a51b54" />

Si vull veure les taules que hi ha a una bbdd utilitzo la comanda **SHOW TABLES**.

<img width="402" height="76" alt="imatge" src="https://github.com/user-attachments/assets/926b549d-edd8-4a76-b40f-10835e396e36" />

Dins d'una bbdd la informació es divideix per taules, a cada taula es guarden camps d'informació.

Per exemple la taula persones podria ser així:

<img width="318" height="274" alt="imatge" src="https://github.com/user-attachments/assets/cf187aa6-c919-49e3-a9d8-f591fbc89f49" />

Existeixen utilitats per dibuixar les taules d'una bbdd com [https://drawsql.app/](https://drawsql.app/).

#### Crear una taula

Per a crear la taula fel servir la comanda **CREATE TABLE**:

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
<img width="621" height="208" alt="imatge" src="https://github.com/user-attachments/assets/1f687004-a11f-4de9-9b35-beddc3a0933b" />

Podem veure una taula com una quadrícula en la que la primera filera té el nom de la informació que es guardarà, és el **camp**, mentre que la resta de fileres es diuen **registres** i és la informació emmagatzemada a la taula.

<img width="1186" height="599" alt="imatge" src="https://github.com/user-attachments/assets/b93b0da5-f55a-4b57-8000-4dfb952f7c15" />

#### Modificar l'estructura de la taula

Si en algun moment ens adonem que no hem construït bé la taula però ja tenim informació ficada podem utilitzar la instrucció **ALTER TABLE**.

[https://www.mariadbtutorial.com/mariadb-basics/mariadb-alter-table/](https://www.mariadbtutorial.com/mariadb-basics/mariadb-alter-table/)

#### Esborrar una taula

Per esborrar una taula fem servir la comanda **DROP TABLE**.

<img width="355" height="137" alt="imatge" src="https://github.com/user-attachments/assets/cfb69515-6abe-4fd6-8834-9c4c8fe47518" />

#### Primary Key

Les taules de dades moltes vegades tenen un camp anomenat PK (**Primary Key**), aquest camp serveix per identificar un registre (una línia d'una taula) de forma inequívoca, perque no poden existir dos valors PK iguals dins la mateixa taula.

En la taula anterior la clau principal és id, un camp que hem inventat i que es sol fer servir a totes les taules.

#### Afegir un registre a una taula

Per a afegir informació a la taula utilitzem la instrucció **INSERT INTO**.

[https://www.mariadbtutorial.com/mariadb-basics/mariadb-insert-into-select/](https://www.mariadbtutorial.com/mariadb-basics/mariadb-insert-into-select/)

Per exemple, per la nostra taula persones si volem afegir un registre farem:

```
INSERT INTO persones(nom, cognom1, cognom2, dni, data_naixement)
VALUES('Xavier','Ordóñez','López','12345678T','1999-03-11');
```

<img width="748" height="96" alt="imatge" src="https://github.com/user-attachments/assets/a5040b15-6842-4ac7-a4f5-15e558710314" />

#### Consultar registres de la taula

Per consultar els registres d'una taula farem servir la comanda **SELECT**.

[https://www.mariadbtutorial.com/mariadb-basics/mariadb-select/](https://www.mariadbtutorial.com/mariadb-basics/mariadb-select/)

Per exemple, per consultar tots els registres de la taula persones fem servir:

```
SELECT * FROM persones;
```
<img width="606" height="169" alt="imatge" src="https://github.com/user-attachments/assets/8eea7004-ad02-4550-8e97-5f8a7e745af7" />

Si només vull camps concrets ho dic a la comanda enlloc de l'asterisc:

```
SELECT id, nom FROM persones;
```

<img width="606" height="169" alt="imatge" src="https://github.com/user-attachments/assets/05be7972-f74c-48db-840f-daf641777877" />

Si vull seleccionar només els registres que compleixin una condició faig servir la clausula WHERE dins del SELECT.

<img width="766" height="319" alt="imatge" src="https://github.com/user-attachments/assets/9aecaeb2-36d5-4b86-9241-454396f8ec7e" />

<img width="586" height="173" alt="imatge" src="https://github.com/user-attachments/assets/715ab0f6-bc8f-41ef-96c4-1c22ce5d6854" />

#### Esborrar un registre

Per esborrar registres fem servir la comanda **DELETE**.

Per exemple per esborrar tots els registres de la taula persones utilitzem la comanda:

```
DELETE FROM persones;
```

<img width="414" height="135" alt="imatge" src="https://github.com/user-attachments/assets/426513c1-cad7-4425-bdeb-84f62339201d" />

Però aquesta instrucció és molt perillosa, sempre es sol utilitzar amb un WHERE que indiqui quins registres volem eliminar.

<img width="624" height="384" alt="imatge" src="https://github.com/user-attachments/assets/8aa5816d-fc96-40a3-a138-fc23e279ad02" />

#### Modificar un registre

Per modificar un registre farem servir la comanda **UPDATE**.

[https://www.mariadbtutorial.com/mariadb-basics/mariadb-update/](https://www.mariadbtutorial.com/mariadb-basics/mariadb-update/)

Per exemple, vull canviar el nom de Petra per Dimitri ja que m'he equivocat a l'hora d'introduir la informació.

<img width="617" height="146" alt="imatge" src="https://github.com/user-attachments/assets/dee0ee56-2388-4f0b-b77d-e847fd1a44e5" />

Faré servir la comanda:

```
UPDATE persones
SET nom='Dimitri'
WHERE id='2';
```

<img width="383" height="109" alt="imatge" src="https://github.com/user-attachments/assets/cebf1938-baca-4fcb-9317-355234228876" />

<img width="641" height="154" alt="imatge" src="https://github.com/user-attachments/assets/579b4612-e7a3-4d41-88be-fc30e3ff2abb" />

