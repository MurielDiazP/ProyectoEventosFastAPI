from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data


autors = Table ("autors", meta_data,
                Column ("id", Integer, primary_key=True),
                Column ("cedula", String (45), nullable=False),
                Column ("area_investigacion", String(45), nullable=False),
                Column ("nombre", String(45), nullable=False),
                Column ("apellido", String(45), nullable=False),
                Column ("email", String (45), nullable=False),
                Column ("celular", String(45), nullable=False),
                Column ("institucion", String (45), nullable=False))

meta_data.create_all(engine)