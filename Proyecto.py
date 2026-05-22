import random

ia = random.randint(1,3)

class Bonus():
    def __init__(self, tipo, nombre, emoji, valor):
        self.tipo: str = tipo
        self.nombre: str = nombre
        self.emoji: str = emoji
        self.valor: int = valor

Dinamita = Bonus("Activo","Dinamita","🧨",*5)
Fuego = Bonus("Activo","Fuego","🔥",*2)
Escudo = Bonus("Pasivo","Escudo","🛡️"*0,)
Corazon = Bonus("Pasivo", "Corazon","❤️‍🩹",*0.5)
Espada = Bonus("Activo","Espada","⚔️",+10)
Curacion = Bonus("Pasivo","Curacion","💊",+10)


class Personaje():
    def __init__(self, nombre_personaje, avatar):
        self.nombre_personaje = nombre_personaje
        self.avatar = avatar
    
    def mostrar_presentacion(self):
        return f"{self.nombre} | {self.avatar} "
    
    def accion(self):
        return int(input("Elige tu opción: "))




Esteban = Personaje("Esteban","🦾")
print(f"Valor de la IA: {ia}")
valor = Esteban.accion()

if valor == 1:
    if ia == 2:
        print("Gana IA")
    if ia == 3:
        print(f"Gana {Esteban.mostrar_presentacion()}")
elif valor == 2:
    if ia == 1:
        print("Gana IA")
    if ia == 3:
        print(f"Gana {Esteban.mostrar_presentacion()}")
elif valor == 3:
    if ia == 1:
        print(f"Gana {Esteban.mostrar_presentacion()}")
    if ia == 2:
        print("Gana IA")
elif valor == ia:
    print("Empate")
else:
    print("Error")
