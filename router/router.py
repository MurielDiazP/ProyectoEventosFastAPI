from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.autor_schema import AutorSchema
from schema.trabajo_schema import TrabajoSchema
from config.db import engine
from model.autor import autors
from model.trabajo_enviado import trabajo_enviados
from typing import List

autor =APIRouter()

trabajo_enviado = APIRouter()

@autor.get("/")
def root():
    return {"message":"Hello World router"}

@autor.get("/api/autor", response_model=List[AutorSchema])
def get_autors():
    with engine.connect() as conn:
        result = conn.execute(autors.select()).fetchall()

        return result
    
@trabajo_enviado.get("/api/trabajo", response_model=List[TrabajoSchema])
def get_trabajos():
    with engine.connect() as conn:
        result = conn.execute(trabajo_enviados.select()).fetchall()

        return result  
    
@autor.get("/api/autor/{autor_id}", response_model=AutorSchema)
def get_autor(autor_id: str):
    with engine.connect() as conn:
        result = conn.execute(autors.select().where(autors.c.id == autor_id)).first()

        return result
    
@trabajo_enviado.get("/api/trabajo/{trabajo_id}", response_model=TrabajoSchema)
def get_trabajo_enviado(trabajo_id: str):
    with engine.connect() as conn:     
        result = conn.execute(trabajo_enviados.select().where(trabajo_enviados.c.id ==trabajo_id)).first()

        return result 

@autor.post("/api/autor", status_code=HTTP_201_CREATED, response_model=AutorSchema)
def create_autor(data_autor: AutorSchema):
    with engine.connect () as conn:
        new_autor = data_autor.model_dump(exclude_none=True)
        
        conn.execute(autors.insert().values(new_autor))
        conn.commit()

        return Response(status_code=HTTP_201_CREATED)

@trabajo_enviado.post("/api/trabajo", status_code=HTTP_201_CREATED, response_model=TrabajoSchema)
def create_trabajo(data_trabajo: TrabajoSchema):
    with engine.connect () as conn:
        new_trabajo = data_trabajo.model_dump(exclude_none=True)
        
        conn.execute(trabajo_enviados.insert().values(new_trabajo))
        conn.commit()

        return Response(status_code=HTTP_201_CREATED)
    
@autor.put("/api/autor/{autor_id}}", response_model=AutorSchema)
def update_autor(autor_id: str, data_update:AutorSchema):
    with engine.connect() as conn:
        
        conn.execute(autors.update().values(cedula=data_update.cedula, area_investigacion=data_update.area_investigacion, nombre=data_update.nombre,
            apellido=data_update.apellido, email=data_update.email, celular=data_update.celular, institucion=data_update.celular).where(autors.columns["id"] == autor_id))
        conn.commit()
        result = conn.execute(autors.select().where(autors.columns["id"] == autor_id)).first()

        return result

@trabajo_enviado.put("/api/trabajo/{trabajo_id}}",response_model=TrabajoSchema)
def update_trabajo(trabajo_id: str, data_update1:TrabajoSchema):
    with engine.connect() as conn:
        
        conn.execute(trabajo_enviados.update().values(titulo=data_update1.titulo, abstractt=data_update1.abstractt, autor_cedula=data_update1.autor_cedula).where(trabajo_enviados.columns["id"] == trabajo_id))
        conn.commit()
        result = conn.execute(trabajo_enviados.select().where(trabajo_enviados.columns["id"] == trabajo_id)).first()

        return result

@autor.delete("/api/autor/{autor_id}")
def delete_autor(autor_id: str):
    with engine.connect() as conn:

        conn.execute(autors.delete().where(autors.columns["id"] == autor_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)

@trabajo_enviado.delete("/api/tarbajo/{trabajo_id}")
def delete_trabajo(trabajo_id: str):
    with engine.connect() as conn:

        conn.execute(trabajo_enviados.delete().where(trabajo_enviados.columns["id"] == trabajo_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)