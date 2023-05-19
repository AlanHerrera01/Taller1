#UNIVERSIDAD DE LAS FUERZAS ARMADAS //ESTRUCTURA DE DATOS
# Chafla
# Herrera
# Chasipanta
# CONVERTIR DECIMAL A BINARIO USANDO PILAS
# https://github.com/AlanHerrera01/Taller1/blob/main/DecimalABinario.py
class Pila:
    def _init_(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

def decimal_a_binario(numero):
    pila = Pila()

    if numero == 0:
        pila.apilar(0)
    else:
        while numero > 0:
            residuo = numero % 2
            pila.apilar(residuo)
            numero //= 2

    numero_binario = ''
    while not pila.esta_vacia():
        numero_binario += str(pila.desapilar())

    return numero_binario


# Ejemplo de uso
numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print(f"El número binario correspondiente es: {numero_binario}")
