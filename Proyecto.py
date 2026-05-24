import random
class Personaje():
    def __init__(self, _nombre_personaje, _avatar, _vida, _eleccion):
        self.nombre_personaje = _nombre_personaje
        self.avatar = _avatar
        self.vida = _vida
        self.eleccion = _eleccion
    def mostrar_personaje(self):
        return f"{self.nombre_personaje}:{self.avatar} | {self.eleccion} | {self.vida}"
    def eleccion(self,opcion):
        if opcion == 1:
            self.eleccion = "✂️"
        elif opcion == 2:
            self.eleccion = "🗞️"
        elif opcion == 3:
            self.eleccion = "🪨"
        else:
            return "Opcion no válida"
    
class InterfazJuego:
    def mostrar_pantalla(self):
        print("""
              Opciones a Elegir:
              1. ✂️
              2. 🗞️
              3. 🪨
              """)
    def mostrar_resultado(self,personaje,ia,victoria):
        print("Los resultado son:")
        print(personaje)
        print(ia)
        print(victoria)

nombre = input("Escribe tu nombre: ")
jugador = Personaje(nombre,"🫩",100,0)
ia = Personaje("IA","🤖",100,0)
interfaz = InterfazJuego()

while True:

    interfaz.mostrar_pantalla()
    opcion_jugador = int(input("Elige una opcion: "))
    opcion_ia = random.randint(1,3)

    jugador.eleccion(opcion_jugador)
    ia.eleccion(opcion_ia)

    if opcion_jugador == 1:
        if opcion_ia == 2:
            interfaz.mostrar_resultado(jugador.mostrar_personaje(),ia.mostrar_personaje(), "Ha ganado el jugador")
        elif opcion_ia == 3:
            interfaz.mostrar_resultado(jugador.mostrar_personaje(),ia.mostrar_personaje(), "Ha ganado la IA")
    elif opcion_jugador == 2:
        if opcion_ia == 1:
            interfaz.mostrar_resultado(jugador.mostrar_personaje(),ia.mostrar_personaje(), "Ha ganado la IA")
        elif opcion_ia == 3:
            interfaz.mostrar_resultado(jugador.mostrar_personaje(),ia.mostrar_personaje(), "Ha ganado el jugador")
    elif opcion_jugador == 3:
        if opcion_ia == 1:
            interfaz.mostrar_resultado(jugador.mostrar_personaje(),ia.mostrar_personaje(), "Ha ganado el jugador")
        elif opcion_ia == 2:
            interfaz.mostrar_resultado(jugador.mostrar_personaje(),ia.mostrar_personaje(), "Ha ganado la IA")
    elif (opcion_jugador == opcion_ia):
        print("EMPATE")
    else:
        print(jugador.eleccion())


