from fastapi import HTTPException, status
from Calculos import schemas
import numpy as np
from io import BytesIO
import math

def karatsuba(request: schemas.Numeros):
	elementos = list(map(lambda x: bin(x)[2:], request.numeros))
	while len(elementos) > 1:
		result = Multiplicar(elementos[0],elementos[1])
		if(len(elementos) > 2):
			elementos = elementos[2:] 
			elementos.append(bin(result)[2:])
		else:
			return {"Response" : result}

def Strassen(request: schemas.Matriz):
	return {"Response": strassen(np.array(request.matrizA), np.array(request.matrizB)).tolist()}  


# Karatsuba 
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


	P1 = Multiplicar(Xl, Yl);
	P2 = Multiplicar(Xr, Yr);
	P3 = Multiplicar(addBitStrings(Xl, Xr), addBitStrings(Yl, Yr));

	return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2
	
def separa(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    linha, coluna = matrix.shape
    linha2, coluna2 = linha//2, coluna//2
    return matrix[:linha2, :coluna2], matrix[:linha2, coluna2:], matrix[linha2:, :coluna2], matrix[linha2:, coluna2:]
 
def strassen(m1, m2):
 
    # Caso Base ou seja nossa matriz ?? uma 1x1
    if len(m1) == 1:
        return m1 * m2
 
    # Separa a matriz em quatro com uma cruz no meio
    a, b, c, d = separa(m1)
    e, f, g, h = separa(m2)
 
    # Calcula os produtos
    p1 = strassen(a, f - h) 
    p2 = strassen(a + b, h)       
    p3 = strassen(c + d, e)       
    p4 = strassen(d, g - e)       
    p5 = strassen(a + d, e + h)       
    p6 = strassen(b - d, g + h) 
    p7 = strassen(a - c, e + f) 
 
    c11 = p5 + p4 - p2 + p6 
    c12 = p1 + p2          
    c21 = p3 + p4           
    c22 = p1 + p5 - p3 - p7 
 
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c