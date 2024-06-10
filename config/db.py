from sqlalchemy import create_engine, MetaData

engine = create_engine ("mysql+pymysql://root:database@localhost:3306/eventos")

conn =engine.connect()

meta_data = MetaData()

