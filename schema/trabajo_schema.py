from pydantic import BaseModel
from typing import Optional


class TrabajoSchema(BaseModel):
    id: int | None = None
    titulo: str
    abstractt: str
    autor_cedula: str
   