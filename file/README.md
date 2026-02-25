# Aventura CRUD - Sistema de Gestió

Aplicació web CRUD per gestionar localitzacions i canins utilitzant FastAPI, Jinja2 i MariaDB.

## Característiques

- ✅ Gestió completa de Localitzacions (Crear, Llegir, Actualitzar, Eliminar)
- ✅ Gestió completa de Canins (Crear, Llegir, Actualitzar, Eliminar)
- ✅ Interfície web responsive sense JavaScript
- ✅ Renderització server-side amb Jinja2
- ✅ Validació de dades i relacions
- ✅ Disseny modern i professional

## Requisits

- Python 3.8 o superior
- MariaDB/MySQL
- Accés a la base de dades "Aventura" amb les taules `localitzacions` i `canins`

## Instal·lació

### 1. Configurar la base de dades

Executa l'script SQL per crear l'usuari de la base de dades:

```bash
mysql -u root -p < setup_database.sql
```

Aquest script crea:
- Usuari: `aventura_user`
- Contrasenya: `Aventura2024!`
- Permisos sobre la base de dades `Aventura`

### 2. Instal·lar dependències Python

```bash
cd aventura_crud
pip install -r requirements.txt
```

Dependències instal·lades:
- `fastapi` - Framework web
- `uvicorn` - Servidor ASGI
- `jinja2` - Motor de plantilles
- `pymysql` - Connector MariaDB/MySQL
- `python-multipart` - Suport per formularis

### 3. Configurar la connexió (opcional)

Si necessites canviar les credencials de la base de dades, edita el fitxer `config.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'aventura_user',
    'password': 'Aventura2024!',
    'database': 'Aventura',
    'charset': 'utf8mb4'
}
```

## Ús

### Iniciar l'aplicació

```bash
cd aventura_crud
python main.py
```

O alternativament amb uvicorn directament:

```bash
uvicorn main:app --reload
```

### Accedir a l'aplicació

Obre el navegador a:
- **Aplicació principal:** http://localhost:8000
- **Documentació API automàtica:** http://localhost:8000/docs

## Estructura del Projecte

```
aventura_crud/
├── main.py              # Aplicació FastAPI principal
├── config.py            # Configuració de base de dades
├── database.py          # Funcions d'accés a base de dades
├── requirements.txt     # Dependències Python
├── templates/           # Plantilles Jinja2
│   ├── base.html
│   ├── index.html
│   ├── localitzacions_list.html
│   ├── localitzacio_form.html
│   ├── canins_list.html
│   └── cani_form.html
└── static/
    └── css/
        └── style.css    # Estils CSS
```

## Funcionalitats

### Localitzacions

- **Llistar:** Visualitza totes les localitzacions amb opció d'editar o eliminar
- **Crear:** Afegeix noves localitzacions amb nom, descripció i imatge
- **Editar:** Modifica localitzacions existents
- **Eliminar:** Esborra localitzacions (comprova que no estiguin en ús per canins)

### Canins

- **Llistar:** Visualitza tots els canins amb les seves dues localitzacions
- **Crear:** Afegeix nous canins seleccionant dues localitzacions
- **Editar:** Modifica les localitzacions assignades
- **Eliminar:** Esborra registres de canins

## Seguretat

⚠️ **Important:** Aquesta aplicació està dissenyada per ús local i no inclou autenticació. Per a entorns de producció, considera afegir:
- Autenticació d'usuaris
- HTTPS
- Validació CSRF
- Rate limiting
- Logging d'auditoria

## Solució de Problemes

### Error de connexió a la base de dades

```
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server...")
```

**Solució:**
- Verifica que MariaDB estigui en marxa: `systemctl status mariadb`
- Comprova les credencials a `config.py`
- Assegura't que l'usuari tingui permisos: `mysql -u aventura_user -p`

### Error "No module named 'fastapi'"

```
ModuleNotFoundError: No module named 'fastapi'
```

**Solució:**
```bash
pip install -r requirements.txt
```

### Port 8000 ja en ús

```
ERROR: [Errno 48] error while attempting to bind on address ('0.0.0.0', 8000)
```

**Solució:**
Canvia el port al fitxer `main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)
```

## Desenvolupament

### Executar en mode desenvolupament

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

L'opció `--reload` reiniciarà automàticament el servidor quan detecti canvis en els fitxers.

### Afegir noves funcionalitats

1. Afegeix rutes a `main.py`
2. Crea queries a `database.py`
3. Crea plantilles a `templates/`
4. Afegeix estils a `static/css/style.css`

## Llicència

Aquest projecte és de codi obert i lliure per a ús educatiu i comercial.

## Suport

Per a problemes o preguntes, consulta la documentació de:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [PyMySQL](https://pymysql.readthedocs.io/)
