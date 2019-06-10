# Module: Tablero

class Lugar:
    """ Clase de tipo Lugar"""
    def __init__(self,nombre,descripcion,costo,renta,status):
        self.nombre = nombre
        self.desc = descripcion
        self.costo= costo
        self.renta = renta
        self.status = status

DescMetro = "La estacion de metro en ciudad Universitaria."
Metro = Lugar("Metro C.U",DescMetro,400,30,0)
DescPumaBici = "Una bonita estacion de Pumabicis"
Bicimetro = Lugar("Estacion de PumaBici",DescPumaBici) 
    
