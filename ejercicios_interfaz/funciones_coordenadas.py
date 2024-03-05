import math
class  Conversion:
    def cartesiana_a_cilindrica(x,y,z):
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y,x)
        return r, theta, z
    def  cartesina_a_esferica(x,y,z):
        r = math.sqrt(x**2 + y**2 + z**2)
        theta = math.atan2(y,x)
        phi= math.acos(z/r)
        return r, theta, phi
        