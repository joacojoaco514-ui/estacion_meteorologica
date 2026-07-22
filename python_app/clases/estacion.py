import random

class Sensor:
    def __init__(self, nombre, pin):
        self.nombre = nombre
        self.pin_conexion = pin
        self.valor_actual = 0

    # Definimos un método (acción)
    def simular_lectura(self):
        if self.nombre == "TMP36":
            self.valor_actual = random.randint(10, 35) # Simula grados
        else:
            self.valor_actual = random.randint(40, 90) # Simula % humedad
            
        print(f"[{self.nombre}] Nueva lectura procesada: {self.valor_actual}")

# --- Pruebas del Sistema ---
sensor_temperatura = Sensor("TMP36", "A0")
sensor_humedad = Sensor("DHT11", "A1")

# Ejecutamos las acciones de nuestros objetos
sensor_temperatura.simular_lectura()
sensor_humedad.simular_lectura()
