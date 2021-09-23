from pydantic import BaseModel
from typing import List

class Matriz(BaseModel):
	matrizA: List[List[float]] = [[]]
	matrizB: List[List[float]] = [[]]

class Numeros(BaseModel):
	numeros: List[int] = []