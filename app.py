import random
import seaborn as sns

class Academia():
    def __init__(self):
        self.halteres = [i for i in range(10,60) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        self.porta_halteres = {i:i for i in self.halteres}

    def listar_espacos(self):
        return [i for i,j in self.porta_halteres.items() if j == 0]

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
        self.tipo_usuario = tipo_usuario # 1 - Normal | 2 - Bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        picked_halter = self.academia.pegar_halter(self.peso)
        return picked_halter
    
    def finalizar_treino(self):
        espacos_vazios = self.academia.listar_espacos()

        if self.tipo_usuario == 1:
            if self.peso in espacos_vazios:
                self.academia.devolver_halter(self.peso,self.peso)
            else:
                escolha_aleatoria = random.choice(espacos_vazios)
                self.academia.devolver_halter(escolha_aleatoria,self.peso)

        elif self.tipo_usuario == 2:
            escolha_aleatoria = random.choice(espacos_vazios)
            self.academia.devolver_halter(escolha_aleatoria,self.peso)

        self.peso = 0
        return

Academia_Arraiana = Academia()

Usuarios = [Usuario(1,Academia_Arraiana) for i in range(20)]
Usuarios.extend([Usuario(2,Academia_Arraiana) for i in range(1)])

random.shuffle(Usuarios)
list_chaos = []

for _ in range(1000):
    Academia_Arraiana.reiniciar_dia()
    for _ in range(10):
        random.shuffle(Usuarios)
        for user in Usuarios:
            user.iniciar_treino()
        for user in Usuarios:
            user.finalizar_treino()

    list_chaos.append(Academia_Arraiana.calcular_caos())

sns.displot(list_chaos)