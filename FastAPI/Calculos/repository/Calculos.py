from fastapi import HTTPException, status
import matplotlib.pyplot as plt
from Calculos import schemas
import pandas as pd
import random
import numpy as np
from io import BytesIO
from base64 import b64encode
import pyimgur
import math

def karatsuba(request: schemas.Numeros):
	return Multiplicar(bin(request.numeros[0])[2:],bin(request.numeros[1])[2:])

def Strassen(request: schemas.Matriz):
	return request


def Igualar(str1, str2):
	if(len(str1) < len(str2)):
		str1 = "0" *  (len(str2) - len(str1)) + str1
	if(len(str1) > len(str2)):
		str2 = "0" *  (len(str1) - len(str2)) + str2
	return (str1, str2)

def addBitStrings(first, second):
	result = ""
	first, second = Igualar(first, second)
	length = len(first)
	carry = 0
	i = length - 1
	while i >= 0:
		firstBit = ord(first[i]) - ord('0')
		secondBit = ord(second[i]) - ord('0')
		soma = (firstBit ^ secondBit ^ carry) + ord('0')
		result = chr(soma) + result
		carry = (firstBit&secondBit) | (secondBit&carry) | (firstBit&carry)
		i -=1
	if carry:
		result = '1' + result
	return result

def multiplyiSingleBit(a: str, b: str):
  return (ord(a[0]) - ord('0')) * (ord(b[0]) - ord('0'))

def Multiplicar(str1, str2):
	str1, str2 = Igualar(str1, str2);
	n = len(str(str1))
	if(n == 0):
		return 0
	if(n == 1):
		return multiplyiSingleBit(str1, str2) 
	fh = math.floor(n/2)
	sh = (n-fh)

	Xl = str1[0:fh]
	Xr = str1[fh:]
	Yl = str2[0:fh]
	Yr = str2[fh:]

  # XR e Yr tรก bugado

	P1 = Multiplicar(Xl, Yl);
	P2 = Multiplicar(Xr, Yr);
	P3 = Multiplicar(addBitStrings(Xl, Xr), addBitStrings(Yl, Yr));

	return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2
