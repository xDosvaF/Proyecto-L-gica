import random

ia = random.randint(1,3)

class Personaje():
    def __init__(self, nombre, avatar):
        self.nombre = nombre
        self.avatar = avatar
    
    def accion(self):
        return int(input("Elige tu opción: "))




Esteban = Personaje("Esteban","🦾")
print(f"Valor de la IA: {ia}")
valor = Esteban.accion()

if valor == 1:
    if ia == 2:
        print("Gana IA")
    if ia == 3:
        print(f"Gana Esteban")
elif valor == 2:
    if ia == 1:
        print("Gana IA")
    if ia == 3:
        print(f"Gana Esteban")
elif valor == 3:
    if ia == 1:
        print(f"Gana Esteban")
    if ia == 2:
        print("Gana IA")
elif valor == ia:
    print("Empate")
else:
    print("Error")