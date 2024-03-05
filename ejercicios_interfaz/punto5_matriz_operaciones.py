import numpy as np
class AngulosMatriz:
    
    def angulox(valor1):
        radianes = np.radians(valor1)
        matriz_rotacion_x = np.array([
            [1,0,0],
            [0,np.cos(radianes), -np.sin(radianes)],
            [0,np.sin(radianes), np.cos(radianes)]
        ])
        return matriz_rotacion_x
    
    def anguloy(valor1):
        radianes = np.radians(valor1)
        matriz_rotacion_y = np.array([
            [np.cos(radianes), 0, np.sin(radianes)],
            [0, 1, 0],
            [-np.sin(radianes), 0, np.cos(radianes)]
        ])
        return matriz_rotacion_y
    
    def anguloz(valor1):
        radianes = np.radians(valor1)
        matriz_rotacion_z = np.array([
            [np.cos(radianes), -np.sin(radianes), 0],
            [np.sin(radianes), np.cos(radianes), 0],
            [0, 0, 1]
        ])
        return matriz_rotacion_z
        
    