import random

class Academia():
    def __init__(self):
        self.halteres = [i for i in range(10,36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        self.porta_halteres = {i:i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def pegar_halter(self,peso):
        halter_position = list(self.porta_halteres.values()).index(peso)
        key_halter = list(self.porta_halteres.keys())[halter_position]
        self.porta_halteres[key_halter] = 0
        return peso
    
    def devolver_halter():
        pass

    def calcular_caos():
        pass


self = Academia()
print(self.pegar_halter(22))
print(self.porta_halteres)