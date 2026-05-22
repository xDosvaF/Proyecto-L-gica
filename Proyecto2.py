import random 

class Personaje:
    def __init__(self, nombre, vida, accion):
        self.nombre = nombre
        self.vida = vida
        self.accion = accion
    def mostrar_jugador(self):
        return f"{self.nombre} | {self.vida} | {self.accion}"
    def accion_jugador(self, opcion):
        self.accion = opcion
        return self.accion
    
class InterfazJuego:
    def mostrar_pantalla(self):
        pass
    def mostrar_resultado(self,jugador,ia,victoria):
        print("Los resultados de la ronda son: ")
        print(jugador)
        print(ia)
        print(victoria)

nombre = input("Escribe tu nombre: ")

Jugador = Personaje(nombre,100,0)
ia = Personaje("IA",100,0)
interfaz = InterfazJuego()

while (Jugador.vida >0 and ia.vida > 0):
    eleccion_jugador = int(input("Elige: "))
    eleccion_ia = random.randint(1,3)
    Jugador.accion_jugador(eleccion_jugador)
    ia.accion_jugador(eleccion_ia)

    if eleccion_jugador == 1:
        if eleccion_ia == 2:
            interfaz.mostrar_resultado(Jugador.mostrar_jugador(),ia.mostrar_jugador(), f"Ha ganado {Jugador.nombre}")
            ia.vida -= 10
        elif eleccion_ia == 3:
            interfaz.mostrar_resultado(Jugador.mostrar_jugador(),ia.mostrar_jugador(),"Ha ganado la IA")
            Jugador.vida -= 10
    elif eleccion_jugador == 2:
        if eleccion_ia == 1:
            interfaz.mostrar_resultado(Jugador.mostrar_jugador(),ia.mostrar_jugador(),"Ha ganado la IA")
            Jugador.vida -=10
        elif eleccion_ia == 3:
            interfaz.mostrar_resultado(Jugador.mostrar_jugador(),ia.mostrar_jugador(),f"Ha ganado {Jugador.nombre}")
            ia.vida -= 10
    elif eleccion_jugador == 3:
        if eleccion_ia == 1:
            interfaz.mostrar_resultado(Jugador.mostrar_jugador(),ia.mostrar_jugador(),f"Ha ganado {Jugador.nombre}")
            ia.vida -= 10
        elif eleccion_ia == 2:
            interfaz.mostrar_resultado(Jugador.mostrar_jugador(),ia.mostrar_jugador(),"Ha ganado la IA")
            Jugador.vida -= 10
    elif eleccion_jugador == eleccion_ia:
        print("EMPATE")
    else:
        print("OPCIÓN NO VÁLIDA")      
