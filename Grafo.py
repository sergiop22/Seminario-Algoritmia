#code
#!/usr/bin/env python
import operator

class Kruskal:
    dato1 = 0
    dato2 = 0
    peso = 0

    def __init__(self, dato1, dato2, peso):
        self.dato1 = dato1
        self.dato2 = dato2
        self.peso = peso
      
def kruskal(edge):  
    ordenamiento = sorted(edge, key=operator.attrgetter('peso')) 
    resultado = []
    datoFinal = set()
    for i in ordenamiento:
        if i.dato1 in datoFinal and i.dato2 in datoFinal:
            continue
        datoFinal.add(i.dato1)
        datoFinal.add(i.dato2)
        resultado.append(i)
    return resultado
