
class Calculadora:
    def Sumar(self,cadena):
        if cadena =="":
            return 0
        elif "," in cadena:
            return int(cadena[0]) + int(cadena[2])
        else:
            return int(cadena)