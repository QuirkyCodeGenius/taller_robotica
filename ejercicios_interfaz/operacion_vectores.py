import numpy as np
class Operaciones:
    a=2
    b=2
    c=2
    d=2
    e=2
    f=2
    

    
    def suma(valor1, valor2, valor3, valora, valorb, valorc):
        
        vectora = np.array([valor1,valor2,valor3])
        vectorb = np.array([valora,valorb,valorc])
        #x = valor1 * valora
        #y = valor2 * valorb
        #z = valor3 * valorc
        
        resultado_producto_punto = vectora + vectorb
        #print(resultado_producto_punto)
        return resultado_producto_punto


    def resta(valor1, valor2, valor3, valora, valorb, valorc):
        
        #x = valor1 * valora
        #y = valor2 * valorb
        #z = valor3 * valorc
        vectora = np.array([valor1,valor2,valor3])
        vectorb = np.array([valora,valorb,valorc])
        resultado_producto_punto = vectora - vectorb
        #resultado_producto_punto = x - y - z
        #print(resultado_producto_punto)
        return resultado_producto_punto
    
    def multiplicacion(valor1, valor2, valor3, valora, valorb, valorc):
        
        #x = valor1 * valora
        #y = valor2 * valorb
        #z = valor3 * valorc
        vectora = np.array([valor1,valor2,valor3])
        vectorb = np.array([valora,valorb,valorc])
        resultado_producto_punto = np.dot(vectora,vectorb)
        resultado_producto_cruz = np.cross(vectora,vectorb)
        
        #resultado_producto_punto = x * y * z
        #print(resultado_producto_punto)
        return resultado_producto_punto,resultado_producto_cruz
    
    def division(valor1, valor2, valor3, valora, valorb, valorc):
        
        #x = valor1 * valora
        #y = valor2 * valorb
        #z = valor3 * valorc
        vectora = np.array([valor1,valor2,valor3])
        vectorb = np.array([valora,valorb,valorc])
        resultado_producto_punto = vectora/vectorb
        #resultado_producto_punto = (x+y+z)/3
        #print(resultado_producto_punto)
        return resultado_producto_punto
    
    #print(suma(a,b,c,d,e,f))
    
