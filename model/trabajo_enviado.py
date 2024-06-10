from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data


trabajo_enviados = Table ("trabajo_enviados" , meta_data,
                          Column ("id", Integer, primary_key=True),
                          Column ("titulo", String (45), nullable=False),
                          Column ("abstractt", String(45), nullable=False),
                          Column("autor_cedula", String (45), nullable=False))

meta_data.create_all(engine)