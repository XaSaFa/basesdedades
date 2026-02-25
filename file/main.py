from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
import database as db

app = FastAPI(title="Aventura CRUD")

# Configurar templates y archivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# ==================== RUTAS PRINCIPALES ====================

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Página principal con menú"""
    return templates.TemplateResponse("index.html", {"request": request})


# ==================== LOCALITZACIONS ====================

@app.get("/localitzacions", response_class=HTMLResponse)
async def list_localitzacions(request: Request):
    """Lista todas las localizaciones"""
    localitzacions = db.execute_query("SELECT * FROM localitzacions ORDER BY id")
    return templates.TemplateResponse(
        "localitzacions_list.html", 
        {"request": request, "localitzacions": localitzacions}
    )

@app.get("/localitzacions/nova", response_class=HTMLResponse)
async def nova_localitzacio_form(request: Request):
    """Formulario para crear nueva localización"""
    return templates.TemplateResponse("localitzacio_form.html", {"request": request})

@app.post("/localitzacions/nova")
async def crear_localitzacio(
    nom: str = Form(...),
    descripcio: str = Form(""),
    imatge: str = Form("")
):
    """Crea una nueva localización"""
    query = """
        INSERT INTO localitzacions (nom, descripcio, imatge) 
        VALUES (%s, %s, %s)
    """
    db.execute_query(query, (nom, descripcio, imatge), fetch=False)
    return RedirectResponse(url="/localitzacions", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/localitzacions/{id}/editar", response_class=HTMLResponse)
async def editar_localitzacio_form(request: Request, id: int):
    """Formulario para editar localización"""
    localitzacio = db.execute_single("SELECT * FROM localitzacions WHERE id = %s", (id,))
    return templates.TemplateResponse(
        "localitzacio_form.html", 
        {"request": request, "localitzacio": localitzacio}
    )

@app.post("/localitzacions/{id}/editar")
async def actualitzar_localitzacio(
    id: int,
    nom: str = Form(...),
    descripcio: str = Form(""),
    imatge: str = Form("")
):
    """Actualiza una localización"""
    query = """
        UPDATE localitzacions 
        SET nom = %s, descripcio = %s, imatge = %s 
        WHERE id = %s
    """
    db.execute_query(query, (nom, descripcio, imatge, id), fetch=False)
    return RedirectResponse(url="/localitzacions", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/localitzacions/{id}/eliminar")
async def eliminar_localitzacio(id: int):
    """Elimina una localización"""
    # Verificar si hay caninos usando esta localización
    check_query = """
        SELECT COUNT(*) as count FROM canins 
        WHERE localitzacio1 = %s OR localitzacio2 = %s
    """
    result = db.execute_single(check_query, (id, id))
    
    if result['count'] > 0:
        # Si hay caninos usando esta localización, redirigir con error
        # (en producción usaríamos flash messages)
        return RedirectResponse(url="/localitzacions", status_code=status.HTTP_303_SEE_OTHER)
    
    db.execute_query("DELETE FROM localitzacions WHERE id = %s", (id,), fetch=False)
    return RedirectResponse(url="/localitzacions", status_code=status.HTTP_303_SEE_OTHER)


# ==================== CANINS ====================

@app.get("/canins", response_class=HTMLResponse)
async def list_canins(request: Request):
    """Lista todos los caninos con sus localizaciones"""
    query = """
        SELECT 
            c.id,
            c.localitzacio1,
            c.localitzacio2,
            l1.nom as nom_localitzacio1,
            l2.nom as nom_localitzacio2
        FROM canins c
        LEFT JOIN localitzacions l1 ON c.localitzacio1 = l1.id
        LEFT JOIN localitzacions l2 ON c.localitzacio2 = l2.id
        ORDER BY c.id
    """
    canins = db.execute_query(query)
    return templates.TemplateResponse(
        "canins_list.html", 
        {"request": request, "canins": canins}
    )

@app.get("/canins/nou", response_class=HTMLResponse)
async def nou_cani_form(request: Request):
    """Formulario para crear nuevo canino"""
    localitzacions = db.execute_query("SELECT id, nom FROM localitzacions ORDER BY nom")
    return templates.TemplateResponse(
        "cani_form.html", 
        {"request": request, "localitzacions": localitzacions}
    )

@app.post("/canins/nou")
async def crear_cani(
    localitzacio1: int = Form(...),
    localitzacio2: int = Form(...)
):
    """Crea un nuevo canino"""
    query = """
        INSERT INTO canins (localitzacio1, localitzacio2) 
        VALUES (%s, %s)
    """
    db.execute_query(query, (localitzacio1, localitzacio2), fetch=False)
    return RedirectResponse(url="/canins", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/canins/{id}/editar", response_class=HTMLResponse)
async def editar_cani_form(request: Request, id: int):
    """Formulario para editar canino"""
    cani = db.execute_single("SELECT * FROM canins WHERE id = %s", (id,))
    localitzacions = db.execute_query("SELECT id, nom FROM localitzacions ORDER BY nom")
    return templates.TemplateResponse(
        "cani_form.html", 
        {"request": request, "cani": cani, "localitzacions": localitzacions}
    )

@app.post("/canins/{id}/editar")
async def actualitzar_cani(
    id: int,
    localitzacio1: int = Form(...),
    localitzacio2: int = Form(...)
):
    """Actualiza un canino"""
    query = """
        UPDATE canins 
        SET localitzacio1 = %s, localitzacio2 = %s 
        WHERE id = %s
    """
    db.execute_query(query, (localitzacio1, localitzacio2, id), fetch=False)
    return RedirectResponse(url="/canins", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/canins/{id}/eliminar")
async def eliminar_cani(id: int):
    """Elimina un canino"""
    db.execute_query("DELETE FROM canins WHERE id = %s", (id,), fetch=False)
    return RedirectResponse(url="/canins", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
