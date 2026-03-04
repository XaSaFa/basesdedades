# Creació d'un CRUD per treballar amb registres de localitzacions i camins

Creem la bbdd:

```
DROP DATABASE Aventura
CREATE DATABASE Aventura
```

Creem les taules:

```
CREATE TABLE `camins` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `localitzacio1` bigint(20) unsigned NOT NULL,
  `localitzacio2` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

```
CREATE TABLE `localitzacions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `descripcio` text DEFAULT NULL,
  `imatge` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

```

## Preparem la bbdd per treballar amb ella

Accedim a mariadb amb ```sudo mariadb```

1. Creem un usuari: 

<img width="584" height="30" alt="imatge" src="https://github.com/user-attachments/assets/f4473877-f5d7-4505-9777-b22102244a96" />

2. Li donem accés a la bbdd:

<img width="482" height="19" alt="imatge" src="https://github.com/user-attachments/assets/250d506d-1bf5-45ee-9377-a707844d7093" />

3. Actualitzem privilegis:

<img width="166" height="28" alt="imatge" src="https://github.com/user-attachments/assets/85e48f9d-6e10-4255-9fb6-e9ba1ae4403d" />

## Descarregar el CRUD:

Tenim el CRUD [aquí](https://github.com/XaSaFa/crud_bbdd).

El baixem i descarreguem a la MV.

<img width="946" height="746" alt="imatge" src="https://github.com/user-attachments/assets/22982435-b4f3-4e32-86d9-ebb05dfde982" />

<img width="598" height="188" alt="imatge" src="https://github.com/user-attachments/assets/83f78d7c-9aa6-483f-9a82-077dfb1a1a08" />

<img width="873" height="469" alt="imatge" src="https://github.com/user-attachments/assets/bcf69234-2782-45d2-99a5-628135c7bdec" />

Obrim aquest projecte amb Pycharm a la MV.

<img width="1294" height="901" alt="imatge" src="https://github.com/user-attachments/assets/825448d7-9555-4cb7-b059-b3bedd77377d" />

Editem el fitxer config.py i fiquem la informació correcta del nom de la bbdd, usuari creat i la seva contrasenya:

<img width="410" height="234" alt="imatge" src="https://github.com/user-attachments/assets/bc3b3f14-a526-4a93-9369-b6f1e5419b11" />

## Executar el CRUD

Executem el fitxer main.py

<img width="1278" height="893" alt="imatge" src="https://github.com/user-attachments/assets/5abd6fde-715b-4cba-80dc-d2a5cece010b" />

Cliquem el link http://0.0.0.0:8000

<img width="608" height="26" alt="imatge" src="https://github.com/user-attachments/assets/fe588ee6-1c31-41dd-bd5e-1760ced1fbc8" />

Ja el tenim funcionant:

<img width="1458" height="600" alt="imatge" src="https://github.com/user-attachments/assets/2b5e2666-1162-4ba0-873f-2855a126dd68" />

## (Només si no funciona el CRUD) Instal·lar software necessari:

1. Fem un fitxer anomenat requeriments.txt amb aquest text:

- fastapi>=0.104.0
- uvicorn>=0.24.0
- jinja2>=3.1.0
- pymysql>=1.0.0
- python-multipart>=0.0.5

Podeu fer servir qualsevol editor com nano o gedit:

<img width="592" height="156" alt="imatge" src="https://github.com/user-attachments/assets/4f4f77a3-e677-452b-ad8f-61ee1be18009" />

Aneu al terminal i executeu ```pip install -r requeriments.txt```, si fa falta instal·leu pip.

<img width="723" height="127" alt="imatge" src="https://github.com/user-attachments/assets/c54ad729-9e21-4f92-8f46-4395f5026417" />

<img width="716" height="325" alt="image" src="https://github.com/user-attachments/assets/654ded06-aaca-4d27-94fa-84e2776d5fda" />
