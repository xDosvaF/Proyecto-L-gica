class padre():
    def __init__(self, nombre):
        self.nombre = nombre
    def hola(self):
        print("Hola, soy la clase Padre")

class hijo(padre):
    def __init__(self,nombre):
        super().__init__(nombre)
    def hola(self):
        super().hola()
        print("Hola, soy la clase hijo")


hi

