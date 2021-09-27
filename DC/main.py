from fastapi import FastAPI
from Calculos.routers import Calculos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

app.include_router(Calculos.router);

@app.get("/")
def main():
    return {"message": "Hello World"}