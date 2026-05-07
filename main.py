from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine
from models import Base, Medarot, Medafighter
from schemas import (
    MedarotCreate, MedarotUpdate, MedarotResponse,
    MedafighterCreate, MedafighterUpdate, MedafighterResponse,
)

# Crea las tablas en Neon si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Medarot API",
    description="API para gestionar Medarots y Medafighters usando FastAPI + Neon DB",
    version="1.0.0",
)


# ──────────────────────────────────────────
#  Root
# ──────────────────────────────────────────

@app.get("/")
def root():
    return {"message": "¡Medarot API activa! Visita /docs para la documentación."}


# ══════════════════════════════════════════
#  MEDAROTS
# ══════════════════════════════════════════

@app.post("/medarots/", response_model=MedarotResponse, status_code=status.HTTP_201_CREATED)
def create_medarot(medarot: MedarotCreate, db: Session = Depends(get_db)):
    """Inserta un nuevo Medarot en la base de datos."""
    db_medarot = Medarot(**medarot.model_dump())
    db.add(db_medarot)
    db.commit()
    db.refresh(db_medarot)
    return db_medarot


@app.get("/medarots/", response_model=List[MedarotResponse])
def get_all_medarots(db: Session = Depends(get_db)):
    """Recupera todos los Medarots activos (no eliminados)."""
    return db.query(Medarot).filter(Medarot.is_deleted == False).all()


@app.get("/medarots/{medarot_id}", response_model=MedarotResponse)
def get_medarot(medarot_id: int, db: Session = Depends(get_db)):
    """Busca un Medarot por su ID."""
    medarot = db.query(Medarot).filter(
        Medarot.id == medarot_id,
        Medarot.is_deleted == False
    ).first()
    if not medarot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medarot con id={medarot_id} no encontrado."
        )
    return medarot


@app.patch("/medarots/{medarot_id}", response_model=MedarotResponse)
def update_medarot(medarot_id: int, updates: MedarotUpdate, db: Session = Depends(get_db)):
    """Modifica parcialmente un Medarot."""
    medarot = db.query(Medarot).filter(
        Medarot.id == medarot_id,
        Medarot.is_deleted == False
    ).first()
    if not medarot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medarot con id={medarot_id} no encontrado."
        )
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(medarot, field, value)
    db.commit()
    db.refresh(medarot)
    return medarot


@app.delete("/medarots/{medarot_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medarot(medarot_id: int, db: Session = Depends(get_db)):
    """Soft-delete: marca el Medarot como eliminado sin borrarlo de la BD."""
    medarot = db.query(Medarot).filter(
        Medarot.id == medarot_id,
        Medarot.is_deleted == False
    ).first()
    if not medarot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medarot con id={medarot_id} no encontrado."
        )
    medarot.is_deleted = True
    db.commit()


# ══════════════════════════════════════════
#  MEDAFIGHTERS
# ══════════════════════════════════════════

@app.post("/medafighters/", response_model=MedafighterResponse, status_code=status.HTTP_201_CREATED)
def create_medafighter(medafighter: MedafighterCreate, db: Session = Depends(get_db)):
    """Inserta un nuevo Medafighter en la base de datos."""
    db_medafighter = Medafighter(**medafighter.model_dump())
    db.add(db_medafighter)
    db.commit()
    db.refresh(db_medafighter)
    return db_medafighter


@app.get("/medafighters/", response_model=List[MedafighterResponse])
def get_all_medafighters(db: Session = Depends(get_db)):
    """Recupera todos los Medafighters activos."""
    return db.query(Medafighter).filter(Medafighter.is_deleted == False).all()


@app.get("/medafighters/{medafighter_id}", response_model=MedafighterResponse)
def get_medafighter(medafighter_id: int, db: Session = Depends(get_db)):
    """Busca un Medafighter por su ID."""
    medafighter = db.query(Medafighter).filter(
        Medafighter.id == medafighter_id,
        Medafighter.is_deleted == False
    ).first()
    if not medafighter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medafighter con id={medafighter_id} no encontrado."
        )
    return medafighter


@app.patch("/medafighters/{medafighter_id}", response_model=MedafighterResponse)
def update_medafighter(medafighter_id: int, updates: MedafighterUpdate, db: Session = Depends(get_db)):
    """Modifica parcialmente un Medafighter."""
    medafighter = db.query(Medafighter).filter(
        Medafighter.id == medafighter_id,
        Medafighter.is_deleted == False
    ).first()
    if not medafighter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medafighter con id={medafighter_id} no encontrado."
        )
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(medafighter, field, value)
    db.commit()
    db.refresh(medafighter)
    return medafighter


@app.delete("/medafighters/{medafighter_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medafighter(medafighter_id: int, db: Session = Depends(get_db)):
    """Soft-delete: marca el Medafighter como eliminado."""
    medafighter = db.query(Medafighter).filter(
        Medafighter.id == medafighter_id,
        Medafighter.is_deleted == False
    ).first()
    if not medafighter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medafighter con id={medafighter_id} no encontrado."
        )
    medafighter.is_deleted = True
    db.commit()