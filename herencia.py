class padre():
    def hola(self):
        print("Hola, soy la clase Padre")

class hijo(padre):
    def hola(self):
        super().hola()
        print("Hola, soy la clase hijo")

objeto = hijo()

objeto.hola()
