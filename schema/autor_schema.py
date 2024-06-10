from pydantic import BaseModel
from typing import Optional


class AutorSchema(BaseModel):
    id: int | None = None
    cedula: str
    area_investigacion: str
    nombre: str
    apellido: str
    email: str
    celular: str
    institucion: str