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
    
    def devolver_halter(self,position,halter):
        self.porta_halteres[position] = halter
        return halter

    def calcular_caos(self):
        out_position_list = [i for i, j in self.porta_halteres.items() if i != j]
        return len(out_position_list) / len(self.porta_halteres)

class Usuario:
    def __init__(self, tipo_usuario, academia):
        self.tipo = tipo_usuario # 1 - Normal | 2 - Bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        halter_choose = random.choice(lista_pesos)
        picked_halter = self.academia.pegar_halter(halter_choose)
        return picked_halter

self = Academia()

