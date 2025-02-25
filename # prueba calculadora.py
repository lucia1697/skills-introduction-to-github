# prueba calculadora
class Calculadora:
    def __init__ (self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2
    def restar(self):
        return self.numero1 - self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def división(self):
        if self.numero2 == 0:
            return "Error: división por cero"
        return self.numero1 / self.numero2
    def operacion(self,eleccion):
        if eleccion == 1:
            return self.sumar()
        if eleccion == 2:
            return self.restar()
        if eleccion == 3:
            return self.multiplicar()
        if eleccion == 4:
            return self.división()
        else:
            return "eleccion incorrecta"
