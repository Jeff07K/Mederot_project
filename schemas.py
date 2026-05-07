from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ──────────────────────────────────────────
#  Medarot schemas
# ──────────────────────────────────────────

class MedarotCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: str = Field(..., min_length=1, max_length=50)
    medal_type: str = Field(..., min_length=1, max_length=50)
    attack_power: float = Field(..., gt=0)


class MedarotUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    type: Optional[str] = Field(None, min_length=1, max_length=50)
    medal_type: Optional[str] = Field(None, min_length=1, max_length=50)
    attack_power: Optional[float] = Field(None, gt=0)


class MedarotResponse(BaseModel):
    id: int
    name: str
    type: str
    medal_type: str
    attack_power: float
    created_at: datetime

    class Config:
        from_attributes = True


# ──────────────────────────────────────────
#  Medafighter schemas
# ──────────────────────────────────────────

class MedafighterCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    rank: str = Field(..., min_length=1, max_length=50)
    specialty: str = Field(..., min_length=1, max_length=100)
    wins: int = Field(default=0, ge=0)


class MedafighterUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    rank: Optional[str] = Field(None, min_length=1, max_length=50)
    specialty: Optional[str] = Field(None, min_length=1, max_length=100)
    wins: Optional[int] = Field(None, ge=0)


class MedafighterResponse(BaseModel):
    id: int
    name: str
    rank: str
    specialty: str
    wins: int
    created_at: datetime

    class Config:
        from_attributes = True
