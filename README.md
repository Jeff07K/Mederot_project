# 🤖 Medarot Project — FastAPI + Neon DB

API REST para gestionar **Medarots** y **Medafighters** de la franquicia Medarot, construida con FastAPI y PostgreSQL en Neon.

---

## 📁 Estructura del proyecto

```
medarot_project/
├── main.py           # Rutas y lógica de la API
├── models.py         # Modelos SQLAlchemy (tablas en Neon)
├── schemas.py        # Esquemas Pydantic (validación)
├── database.py       # Conexión a Neon DB
├── requirements.txt  # Dependencias
├── .env.example      # Plantilla de variables de entorno
├── .gitignore        # Excluye .env y archivos sensibles
└── test_main.http    # Casos de prueba HTTP
```

---

## 🗄️ Tablas en Neon

### `medarots`
| Campo | Tipo | Descripción |
|---|---|---|
| id | Integer PK | Identificador único |
| name | String | Nombre del Medarot |
| type | String | Tipo (Shooter, Fighter, etc.) |
| medal_type | String | Tipo de medalla (Beetle, Stag, etc.) |
| attack_power | Float | Poder de ataque |
| is_deleted | Boolean | Soft delete (default: false) |
| created_at | DateTime | Fecha de creación |

### `medafighters`
| Campo | Tipo | Descripción |
|---|---|---|
| id | Integer PK | Identificador único |
| name | String | Nombre del entrenador |
| rank | String | Rango (Beginner, Intermediate, etc.) |
| specialty | String | Especialidad de combate |
| wins | Integer | Victorias acumuladas |
| is_deleted | Boolean | Soft delete (default: false) |
| created_at | DateTime | Fecha de creación |

---

## ⚙️ Instalación

```bash
# 1. Clonar el repo
git clone https://github.com/Jeff07K/Mederot_project.git
cd Mederot_project

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Edita .env y agrega tu DATABASE_URL de Neon

# 5. Levantar el servidor
uvicorn main:app --reload
```

---

## 🔒 Manejo de información sensible

- La `DATABASE_URL` (con credenciales de Neon) se guarda **únicamente** en el archivo `.env`.
- El `.env` está en `.gitignore` — **nunca se sube a GitHub**.
- Se provee `.env.example` como plantilla sin datos reales.

---

## 🧪 Casos de prueba

Abre `test_main.http` en IntelliJ/PyCharm o usa la extensión **REST Client** en VS Code.

Los casos cubren:
- ✅ Crear registros (POST)
- ✅ Listar todos los registros (GET)
- ✅ Consultar por ID (GET /{id})
- ✅ Manejo de error 404 para registros inexistentes
- ✅ Modificación parcial (PATCH)
- ✅ Eliminación con soft delete (DELETE)

---

## 🛡️ Estrategia de integridad (Soft Delete)

Los registros eliminados **no se borran físicamente** de la base de datos. En su lugar, se marca el campo `is_deleted = true`. Esto garantiza:
- Trazabilidad y auditoría de datos.
- Posibilidad de recuperar registros si fue un error.
- Integridad referencial en el futuro.

---

## 📖 Documentación interactiva

Con el servidor corriendo, visita:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
