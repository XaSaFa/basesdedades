# 🚀 GUÍA RÁPIDA DE INICIO - Aventura CRUD

## Instalación Express (5 pasos)

### 1️⃣ Configura la Base de Datos
```bash
mysql -u root -p < setup_database.sql
```
Esto crea el usuario `aventura_user` con contraseña `Aventura2024!`

### 2️⃣ Instala las Dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Inicia la Aplicación
```bash
python main.py
```

### 4️⃣ Abre tu Navegador
Visita: http://localhost:8000

### 5️⃣ ¡Listo!
Ya puedes crear, editar y eliminar localitzacions y canins.

---

## 🎯 Inicio Automático

### Linux/Mac
```bash
chmod +x start.sh
./start.sh
```

### Windows
```cmd
start.bat
```

---

## 📋 Rutas Disponibles

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal |
| `/localitzacions` | Lista de localitzacions |
| `/localitzacions/nova` | Crear localització |
| `/localitzacions/{id}/editar` | Editar localització |
| `/canins` | Lista de canins |
| `/canins/nou` | Crear caní |
| `/canins/{id}/editar` | Editar caní |
| `/docs` | Documentación API automática |

---

## 🔧 Configuración Personalizada

Edita `config.py` para cambiar:
- Host de base de datos
- Puerto
- Usuario/contraseña
- Nombre de la base de datos

---

## 🆘 Problemas Comunes

### No conecta a la base de datos
```bash
# Verifica que MariaDB esté corriendo
systemctl status mariadb

# Prueba la conexión manualmente
mysql -u aventura_user -p
# Contraseña: Aventura2024!
```

### Port 8000 ocupado
Edita `main.py`, línea final:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Cambia 8000 a 8001
```

### Error de dependencias
```bash
# Reinstala todas las dependencias
pip install --upgrade -r requirements.txt
```

---

## 💡 Tips

- **Modo desarrollo**: Usa `uvicorn main:app --reload` para auto-reload
- **Ver logs**: La consola muestra todas las peticiones HTTP
- **API docs**: FastAPI genera docs automáticas en `/docs`
- **Sin JavaScript**: Toda la app funciona con formularios HTML puros

---

## 📚 Estructura de Datos

### Tabla: localitzacions
- `id`: bigint (PK, auto)
- `nom`: varchar(100)
- `descripcio`: blob
- `imatge`: varchar(250)

### Tabla: canins
- `id`: bigint (PK, auto)
- `localitzacio1`: bigint (FK → localitzacions.id)
- `localitzacio2`: bigint (FK → localitzacions.id)

---

## 🎨 Personalización

### Cambiar colores
Edita `static/css/style.css`:
```css
/* Colores principales */
:root {
    --primary-color: #3498db;
    --success-color: #27ae60;
    --danger-color: #e74c3c;
}
```

### Añadir campos
1. Modifica la tabla en MariaDB
2. Actualiza las queries en `database.py`
3. Añade campos en los formularios de `templates/`

---

## 📞 Soporte

- Documentación FastAPI: https://fastapi.tiangolo.com/
- Jinja2 Templates: https://jinja.palletsprojects.com/
- PyMySQL: https://pymysql.readthedocs.io/

---

**¡Disfruta de tu aplicación CRUD! 🎉**
