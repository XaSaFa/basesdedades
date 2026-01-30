# Foreign Key

[https://www.mariadbtutorial.com/mariadb-basics/mariadb-foreign-key/](https://www.mariadbtutorial.com/mariadb-basics/mariadb-foreign-key/)

Una clau externa (o forana) és un camp d'una taula que ha de coincidir amb els valors d'una clau principal (Primary Key) d'una altra taula.

Per exemple imaginem que tenim un taula que guarda les dades dels propietaris de mascotes d'una clínica veterinària.

<img width="303" height="70" alt="imatge" src="https://github.com/user-attachments/assets/d649b0ad-9c86-46a9-8654-765f4cd0b986" />

Per saber de qui és cada mascota la taula mascotes serà així:

<img width="303" height="70" alt="imatge" src="https://github.com/user-attachments/assets/718c8b21-410c-47b3-97fb-bec89741e68f" />

On id_mascota és la Primary Key de la taula mascotes però id_propietari és una foreign key que només pot existir si hi ha una entrada amb aquest valor a la taula propietaris.

Per a crear aquestes taules faríem:

<img width="656" height="310" alt="imatge" src="https://github.com/user-attachments/assets/fef6e95e-754d-4fb1-a4e6-e6541cd3b772" />

<img width="676" height="343" alt="imatge" src="https://github.com/user-attachments/assets/d27fcc0a-fd3d-4999-accd-e0a598c4e25b" />

La relació entre les dues taules quedaria com es veu a la imatge:

<img width="664" height="193" alt="imatge" src="https://github.com/user-attachments/assets/aa1d28dc-0a5c-4228-b1b7-a7cfb2dfea27" />

Si intento afegir un registre a la taula mascotes utilitzant un valor de id_propietari que no coincideix amb cap registre de la taula propietaris obtenim un error:

<img width="896" height="100" alt="imatge" src="https://github.com/user-attachments/assets/79ada04a-e9a5-47a6-be4a-b786c4784fb5" />

