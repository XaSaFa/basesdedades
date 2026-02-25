# Creació d'un CRUD per treballar amb registres de localitzacions i camins

## Preparem la bbdd per treballar amb ella

Accedim a mariadb amb ```sudo mariadb```

1. Creem un usuari: 

<img width="584" height="30" alt="imatge" src="https://github.com/user-attachments/assets/f4473877-f5d7-4505-9777-b22102244a96" />

2. Li donem accés a la bbdd:

<img width="482" height="19" alt="imatge" src="https://github.com/user-attachments/assets/250d506d-1bf5-45ee-9377-a707844d7093" />

3. Actualitzem privilegis:

<img width="166" height="28" alt="imatge" src="https://github.com/user-attachments/assets/85e48f9d-6e10-4255-9fb6-e9ba1ae4403d" />

## Instal·lar software necessari:

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

