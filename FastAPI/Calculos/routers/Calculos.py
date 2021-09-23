from fastapi import APIRouter, status, HTTPException
from Calculos.repository import Calculos as Calc
from Calculos import schemas

router = APIRouter(
	prefix="/Calculos",
	tags=['Calculos']
)

@router.post('/Karatsuba', status_code=status.HTTP_201_CREATED)
def Karatsuba(request: schemas.Numeros):
	return Calc.karatsuba(request)

@router.post('/Strassen', status_code=status.HTTP_201_CREATED)
def Strassen(request: schemas.Matriz):
	return Calc.Strassen(request)