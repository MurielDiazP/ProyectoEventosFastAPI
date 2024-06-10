from fastapi import FastAPI
from router.router import autor, trabajo_enviado

app = FastAPI()
app.include_router(autor)
app.include_router(trabajo_enviado)