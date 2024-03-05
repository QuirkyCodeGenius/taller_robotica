#from scipy.linalg import cross
import numpy as np

class ArraysOperaciones:
    

    def crear_matriz(filas, columnas):
        return np.zeros((filas, columnas))

    def mostrar_matriz(matriz):
        print(matriz)

    def modificar_valor(matriz, fila, columna, nuevo_valor):
        matriz[fila, columna] = nuevo_valor
        return matriz

    def suma(matriz_a,matriz_b):
        if np.shape(matriz_a) != np.shape(matriz_b):
            raise ValueError("las matrices deben tener las mismas posiciones")
        
        totalSuma = matriz_a + matriz_b
        
        return totalSuma
    
    def resta(matriz_a,matriz_b):
        if np.shape(matriz_a) != np.shape(matriz_b):
            raise ValueError("las matrices deben tener las mismas posiciones")
        
        totalResta = matriz_a - matriz_b
        return totalResta
    
    def multiplicacionPunto(matriz_a,matriz_b):
        
        totalPunto = np.dot(matriz_a,matriz_b)
        
        return totalPunto
        
    def multiplicacionCruz(matriz_a,matriz_b):
        
        totalCruz = np.cross(matriz_a,matriz_b,axisa =0, axisb =0)
        
        return totalCruz
    def division(matriz_a,matriz_b):
        
        totalDivision = np.divide(matriz_a,matriz_b)
        
        return totalDivision
    
    
        
        
        
        