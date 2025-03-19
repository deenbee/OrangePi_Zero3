import pygame
import wiringpi
import os
import json
from config.variables import *
from src.jsncodes import load_settings, save_settings
from src.handle import update_sequencer, handle_input
from src.draw_ui import draw_ui, draw_steps

# Comando shell para ejecutar el código según el driver del sonido
# sudo SDL_AUDIODRIVER=alsa AUDIODEV=hw:1,0 python3 v2b.py

load_settings() # Load saved settings (Colors & Sound Card)

print("Audio.freq ", Audio.freq, " Audio.bits ", Audio.bits, " Audio.chan ", Audio.chan, " Audio.buffer, ", Audio.buffer, "Background ", Color.bg)


if not os.path.exists("presets"):
    os.makedirs("presets")

# Bucle principal
running = True
clock = pygame.time.Clock()

#print(f"Seq.Seq.tpo_txt inicial: {Seq.Seq.tpo_txt}")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_input(event.pos)
        elif event.type == pygame.KEYDOWN:
            if Seq.tempo_BOX.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    Seq.tpo_txt = Seq.tpo_txt[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        Seq.tempo = int(Seq.tpo_txt)
                    except ValueError:
                        Seq.tempo = 100
                    Seq.tpo_txt = str(Seq.tempo)
                elif event.unicode.isdigit():
                    Seq.tpo_txt += event.unicode

    screen.fill(Color.bg)
    draw_steps()
    draw_ui()
    update_sequencer()
    print("Active patt ", Seq.apt, "Total patt ", Seq.tpt)
    pygame.display.flip()
    clock.tick(60)

# Apagar todos los LEDs al salir
for pin in led_pins:
    wiringpi.digitalWrite(pin, 0)

save_settings()
pygame.quit()
