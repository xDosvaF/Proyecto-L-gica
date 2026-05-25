import random
import time
import os
import json


class Bonus:
    def __init__(self, nombre, emoji, tipo, valor):
        self.nombre = nombre
        self.emoji = emoji
        self.tipo = tipo
        self.valor = valor


class Personaje:
    def __init__(self, nombre, avatar, vida):
        self.nombre = nombre
        self.avatar = avatar
        self.vida = vida
        self.eleccion = "➖"
        self.bonus = None

    def mostrar_informacion(self):
        bonus_texto = self.bonus.emoji + " " + self.bonus.nombre if self.bonus else "Ninguno"
        print(self.nombre, self.avatar, "| Eleccion:", self.eleccion, "| Bonus:", bonus_texto, "| Vida:", self.vida)

    def realizar_eleccion(self, opcion):
        opciones = {1: "✌️", 2: "🗞️", 3: "✊"}
        if opcion in opciones:
            self.eleccion = opciones[opcion]
        else:
            print("Opcion no valida")

    def aplicar_bonus(self, daño):
        if self.bonus == None:
            return daño
        if self.bonus.tipo == "daño_extra_x5":
            daño *= 5
        elif self.bonus.tipo == "daño_extra_x2":
            daño *=  2
        elif self.bonus.tipo == "inmunidad":
            daño = 0
        elif self.bonus.tipo == "resistencia":
            daño = daño // 2
        elif self.bonus.tipo == "ataque":
            daño += 3
        elif self.bonus.tipo == "curacion":
            self.vida = min(self.vida + 10, 100)
        return daño


class InterfazJuego:
    def mostrar_pantalla(self):
        os.system("clear")
        print("PIEDRA PAPEL TIJERA: ")
        print("1. ✌️  Tijera")
        print("2. 🗞️  Papel")
        print("3. ✊  Piedra")

    def mostrar_resultado(self, jugador, ia, mensaje):
        os.system("clear")
        print("Resultados de la ronda: ")
        jugador.mostrar_informacion()
        ia.mostrar_informacion()
        print(mensaje)
        for i in range(50):
            print("[" + "#" * (i+1) + "-" * (49-i) + "]", end="\r")
            time.sleep(0.05)
        print()
        time.sleep(2)
        os.system("clear")


def bonus_aleatorio():
    lista_bonus = [
        Bonus("Daño x5",     "🧨", "daño_extra_x5", 5),
        Bonus("Daño x2",     "🔥", "daño_extra_x2", 2),
        Bonus("Escudo",      "🛡️", "inmunidad",     0),
        Bonus("Resistencia", "❤️‍🩹", "resistencia",  0),
        Bonus("Ataque",      "⚔️", "ataque",        3),
        Bonus("Curacion",    "🌡️", "curacion",      10),
        Bonus("Ninguno",     "➖", "ninguno",       0),
        Bonus("Ninguno",     "➖", "ninguno",       0),
        Bonus("Ninguno",     "➖", "ninguno",       0),
    ]
    return random.choice(lista_bonus)


def guardar_estado(jugador, ia, ronda):
    datos = {"ronda": ronda, "jugador_nombre": jugador.nombre, "jugador_vida": jugador.vida, "ia_vida": ia.vida}
    archivo = open("estado_juego.json", "w")
    json.dump(datos, archivo)
    archivo.close()


def cargar_estado():
    if os.path.exists("estado_juego.json"):
        archivo = open("estado_juego.json", "r")
        datos = json.load(archivo)
        archivo.close()
        return datos
    return None


nombre = input("Escribe tu nombre: ")
jugador = Personaje(nombre, "🫩", 100)
ia = Personaje("IA", "🤖", 100)
interfaz = InterfazJuego()
ronda = 1

datos_guardados = cargar_estado()
if datos_guardados != None:
    print("Partida guardada encontrada - Ronda", datos_guardados["ronda"])
    print(datos_guardados["jugador_nombre"], "vida:", datos_guardados["jugador_vida"], "| IA vida:", datos_guardados["ia_vida"])
    respuesta = input("Deseas continuar? (s/n): ")
    if respuesta == "s":
        jugador.vida = datos_guardados["jugador_vida"]
        ia.vida = datos_guardados["ia_vida"]
        ronda = datos_guardados["ronda"]

while jugador.vida > 0 and ia.vida > 0:
    interfaz.mostrar_pantalla()

    try:
        opcion_jugador = int(input("Elige una opcion: "))
    except ValueError:
        print("Debes escribir un numero")
        time.sleep(1)
        continue

    opcion_ia = random.randint(1, 3)
    jugador.realizar_eleccion(opcion_jugador)
    ia.realizar_eleccion(opcion_ia)
    jugador.bonus = bonus_aleatorio()
    ia.bonus = bonus_aleatorio()

    daño_base = 10
    mensaje = ""
    gana_jugador = (opcion_jugador == 1 and opcion_ia == 2) or (opcion_jugador == 2 and opcion_ia == 3) or (opcion_jugador == 3 and opcion_ia == 1)
    gana_ia = (opcion_jugador == 1 and opcion_ia == 3) or (opcion_jugador == 2 and opcion_ia == 1) or (opcion_jugador == 3 and opcion_ia == 2)

    if opcion_jugador == opcion_ia:
        mensaje = "EMPATE!"
    elif gana_jugador:
        daño = ia.aplicar_bonus(daño_base)
        ia.vida = max(ia.vida - daño, 0)
        mensaje = f"Gano {jugador.nombre}! IA recibió {daño} daño"
    elif gana_ia:
        daño = jugador.aplicar_bonus(daño_base)
        jugador.vida = max(jugador.vida - daño, 0)
        mensaje = f"Gano la IA! {jugador.nombre} recibió {daño} daño"

    interfaz.mostrar_resultado(jugador, ia, mensaje)
    guardar_estado(jugador, ia, ronda)
    ronda = ronda + 1

print("FIN DEL JUEGO")
if jugador.vida <= 0:
    print("Gano la IA!")
else:
    print(f"Gano {jugador.nombre}!")

if os.path.exists("estado_juego.json"):
    os.remove("estado_juego.json")