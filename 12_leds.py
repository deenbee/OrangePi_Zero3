import wiringpi
import time

# Inicializar GPIO
wiringpi.wiringPiSetup()

# Definir pines de LEDs
LEDS = {
    "RED": [0, 7, 14],
    "YELLOW": [15, 9, 6],
    "BLUE": [12, 10, 8],
    "GREEN": [4, 11, 2]
}

# Configurar pines como salida
for color in LEDS.values():
    for pin in color:
        wiringpi.pinMode(pin, 1)
        
def turn_all_off(delay_time):
    for i in range(3):
        wiringpi.digitalWrite(LEDS["RED"][i], 0)
        wiringpi.digitalWrite(LEDS["YELLOW"][i], 0)
        wiringpi.digitalWrite(LEDS["BLUE"][i], 0)
        wiringpi.digitalWrite(LEDS["GREEN"][i], 0)
    time.sleep(delay_time)           

def ola(dl_time):
    """Efecto de ola de luces"""
    for i in range(3):
        for color in LEDS.values():
            wiringpi.digitalWrite(color[i], 1)
            time.sleep(dl_time)
            wiringpi.digitalWrite(color[i], 0)

def parpadeo_alternado(dl_time):
    """Parpadeo alternado entre grupos de colores"""
    for _ in range(5):
        for i in range(3):
            wiringpi.digitalWrite(LEDS["RED"][i], 1)
            wiringpi.digitalWrite(LEDS["GREEN"][i], 1)
        time.sleep(dl_time)
        for i in range(3):
            wiringpi.digitalWrite(LEDS["RED"][i], 0)
            wiringpi.digitalWrite(LEDS["GREEN"][i], 0)
        
        for i in range(3):
            wiringpi.digitalWrite(LEDS["YELLOW"][i], 1)
            wiringpi.digitalWrite(LEDS["BLUE"][i], 1)
        time.sleep(dl_time)
        for i in range(3):
            wiringpi.digitalWrite(LEDS["YELLOW"][i], 0)
            wiringpi.digitalWrite(LEDS["BLUE"][i], 0)

def explosion(dl_time):
    """Explosión desde el centro hacia los extremos"""
    for i in range(3):
        for color in LEDS.values():
            wiringpi.digitalWrite(color[i], 1)
        time.sleep(dl_time)
        for color in LEDS.values():
            wiringpi.digitalWrite(color[i], 0)
        time.sleep(dl_time)

def carrera_luces(dl_time):
    """Las luces avanzan una por una y regresan"""
    for i in range(3):
        for color in LEDS.values():
            wiringpi.digitalWrite(color[i], 1)
            time.sleep(dl_time)
            wiringpi.digitalWrite(color[i], 0)

    for i in reversed(range(3)):
        for color in LEDS.values():
            wiringpi.digitalWrite(color[i], 1)
            time.sleep(dl_time)
            wiringpi.digitalWrite(color[i], 0)

def espiral(dl_time):
    """Efecto de luces encendiéndose en espiral"""
    orden = [0, 15, 12, 4, 7, 9, 10, 11, 14, 6, 8, 2]  # Orden en espiral
    for i in range(4):
        for pin in orden:
            wiringpi.digitalWrite(pin, 1)
            time.sleep(dl_time)
        
        for pin in reversed(orden):
            wiringpi.digitalWrite(pin, 0)
            time.sleep(dl_time)

def zigzag(dl_time):
    """Luces en patrón de zigzag"""
    loop = 0
    repeat = 4
    for i in range(repeat):
        for i in range(3):
            wiringpi.digitalWrite(LEDS["RED"][i], 1)
            wiringpi.digitalWrite(LEDS["BLUE"][2 - i], 1)
            time.sleep(dl_time)
            wiringpi.digitalWrite(LEDS["RED"][i], 0)
            wiringpi.digitalWrite(LEDS["BLUE"][2 - i], 0)

        for i in range(3):
            wiringpi.digitalWrite(LEDS["YELLOW"][i], 1)
            wiringpi.digitalWrite(LEDS["GREEN"][2 - i], 1)
            time.sleep(dl_time)
            wiringpi.digitalWrite(LEDS["YELLOW"][i], 0)
            wiringpi.digitalWrite(LEDS["GREEN"][2 - i], 0)
        loop += 1    
        print("Loop number: ", loop)
loop = 0 # Reset count       

def pulsacion(dl_time):
    """Efecto de pulsación: todas las luces se encienden y apagan suavemente"""
    for _ in range(3):  # Número de pulsos
        for color in LEDS.values():
            for pin in color:
                wiringpi.digitalWrite(pin, 1)
        time.sleep(dl_time)
        for color in LEDS.values():
            for pin in color:
                wiringpi.digitalWrite(pin, 0)
        time.sleep(dl_time)


import random

def destello_aleatorio(dl_time):
    """Encender y apagar LEDs aleatoriamente"""
    for _ in range(10):  # Número de destellos
        pin = random.choice(sum(LEDS.values(), []))  # Elegir LED aleatorio
        wiringpi.digitalWrite(pin, 1)
        time.sleep(dl_time)
        wiringpi.digitalWrite(pin, 0)

turn_all_off(0)

# Prueba de secuencias
try:
    while True:
          ola(0.15)
          parpadeo_alternado(0.15)
          explosion(0.15)
          carrera_luces(0.15)
          espiral(0.15)
          zigzag(0.2)
          pulsacion(0.2)

except KeyboardInterrupt:
    print("\nExiting program.")
    turn_all_off(0)  # Ensure LED is OFF before exiting

    
