import select
#from turtle import pos
import pygame
#import #wiringpi
import os



class Samples:
    
    select_bank = 0
    
    # Ajustar base_path para apuntar al directorio raíz del proyecto
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


    # Lista de archivos WAV
    wav_files = [
        os.path.join(base_path, "samples/808/Kick Basic.wav"),
        os.path.join(base_path, "samples/808/Kick Long.wav"),
        os.path.join(base_path, "samples/808/Kick Mid.wav"),
        os.path.join(base_path, "samples/808/Kick Short.wav"),
        os.path.join(base_path, "samples/808/Snare Mid.wav"),
        os.path.join(base_path, "samples/808/Snare Low.wav"),
        os.path.join(base_path, "samples/808/Snare High.wav"),
        os.path.join(base_path, "samples/808/Snare Bright.wav"),
        os.path.join(base_path, "samples/808/Rimshot.wav"),
        os.path.join(base_path, "samples/808/Open Hat Short.wav"),
        os.path.join(base_path, "samples/808/Open Hat Long.wav"),
        os.path.join(base_path, "samples/808/Hihat.wav"),
        os.path.join(base_path, "samples/808/Cymbal.wav"),
        os.path.join(base_path, "samples/808/Cowbell.wav"),
        os.path.join(base_path, "samples/808/Clap.wav"),
        os.path.join(base_path, "samples/808/Conga Mid.wav"),
        os.path.join(base_path, "samples/808/Conga Low.wav"),
        os.path.join(base_path, "samples/808/Conga High.wav"),
        os.path.join(base_path, "samples/808/Claves.wav"),
        os.path.join(base_path, "samples/808/Maracas.wav"),
        os.path.join(base_path, "samples/808/Tom Mid.wav"),
        os.path.join(base_path, "samples/808/Tom Low.wav"),
        os.path.join(base_path, "samples/808/Tom High.wav"),
        os.path.join(base_path, "samples/808/808.wav"),
    ]

    T909 = [
        os.path.join(base_path, "samples/909/bd01.wav"),
        os.path.join(base_path, "samples/909/bd02.wav"),
        os.path.join(base_path, "samples/909/bd03.wav"),
        os.path.join(base_path, "samples/909/bd04.wav"),
        os.path.join(base_path, "samples/909/bd05.wav"),
        os.path.join(base_path, "samples/909/bd06.wav"),
        os.path.join(base_path, "samples/909/cp01.wav"),
        os.path.join(base_path, "samples/909/cr01.wav"),
        os.path.join(base_path, "samples/909/cp02.wav"),
        os.path.join(base_path, "samples/909/cr02.wav"),
        os.path.join(base_path, "samples/909/rd01.wav"),
        os.path.join(base_path, "samples/909/rs01.wav"),
        os.path.join(base_path, "samples/909/hh01.wav"),
        os.path.join(base_path, "samples/909/rs02.wav"),
        os.path.join(base_path, "samples/909/rd03.wav"),
        os.path.join(base_path, "samples/909/hh02.wav"),
        os.path.join(base_path, "samples/909/rd04.wav"),
        os.path.join(base_path, "samples/909/mt03.wav"),
        os.path.join(base_path, "samples/909/sd01.wav"),
        os.path.join(base_path, "samples/909/oh01.wav"),
        os.path.join(base_path, "samples/909/sd02.wav"),
        os.path.join(base_path, "samples/909/oh02.wav"),
        os.path.join(base_path, "samples/909/mt01.wav"),
        os.path.join(base_path, "samples/909/mt02.wav"),
    ]

    C64 = [
        os.path.join(base_path, "samples/c64/kick1.wav"),
        os.path.join(base_path, "samples/c64/clap.wav"),
        os.path.join(base_path, "samples/c64/kick2.wav"),
        os.path.join(base_path, "samples/c64/cowbell.wav"),
        os.path.join(base_path, "samples/c64/kick3.wav"),
        os.path.join(base_path, "samples/c64/hihat1.wav"),
        os.path.join(base_path, "samples/c64/kick4.wav"),
        os.path.join(base_path, "samples/c64/hihat2.wav"),
        os.path.join(base_path, "samples/c64/kick5.wav"),
        os.path.join(base_path, "samples/c64/snare1.wav"),
        os.path.join(base_path, "samples/c64/kick6.wav"),
        os.path.join(base_path, "samples/c64/snare2.wav"),
        os.path.join(base_path, "samples/c64/kick7.wav"),
        os.path.join(base_path, "samples/c64/snare3.wav"),
        os.path.join(base_path, "samples/c64/kick8.wav"),
        os.path.join(base_path, "samples/c64/snare4.wav"),
        os.path.join(base_path, "samples/808/Tom High.wav"),
        os.path.join(base_path, "samples/c64/snare6.wav"),
        os.path.join(base_path, "samples/808/Conga Low.wav"),
        os.path.join(base_path, "samples/c64/snare7.wav"),
        os.path.join(base_path, "samples/808/Hihat.wav"),
        os.path.join(base_path, "samples/c64/snare8.wav"),
        os.path.join(base_path, "samples/c64/tom1.wav"),
        os.path.join(base_path, "samples/c64/tom2.wav"),
    ]

    @staticmethod
    def verify_files():
        """Verifica si los archivos existen y muestra un mensaje si no se encuentran."""
        for file_list in [Samples.wav_files, Samples.T909, Samples.C64]:
            for file in file_list:
                if not os.path.exists(file):
                    print(f"Archivo no encontrado: {file}")
    
    
    

class Audio:
    freq = 44100
    bits = -16
    chan = 2
    buffer = 512

class Color:
    g = (150, 150, 150)
    r = (255, 0, 0) 
    w = (255, 255, 255)
    bg = (0, 0, 0)
    gn = (0, 0, 0)

class Patt:
    mtx_p = [[[0] * 16 for _ in range(24)] for _ in range(32)]  # Matrix de 32 patterns
    mtx_p_2 = [[[0] * 16 for _ in range(24)] for _ in range(32)]  # Matrix de 32 patterns


        
# Configuración del secuenciador
class Seq:
    tempo = 100
    tpo_txt = str(tempo)  # tempo_text
    m_vol = 1.0           # master_volume: Volumen master
    m_opn = False # menu_open
    playing = False
    lstime = 0 # last_step_time
    s_idx = 0 # step_index
    tpt = 1    # total_patt : Total numbers of patterns (máximo 32)
    apt = 1   # Active Song position (VARIABLE PRINCIPAL)
    act_chs = {} # Active channels
    s_mem = 1 # Selected_memory
    channel_volumes = [1.0] * 24  # Volumen por canal (0.0 a 1.0)
    pan_volumes = [0.0] * 24      # Panorama por canal (-1.0 a 1.0)
    
    pattern_num = 1             # Pattern seleccionada por los numeros del 1 al 32
    patt_state = [1] * 32       # Segun la posicion de la cancion (variable apt), se inician todos en 1 porque no puede haber 0
    patt = 1                    # Pattern actual de 1 a 32

    pulsador_stop = False



# Lista de drivers a probar
drivers_audio = ["wasapi", "directsound", "winmm", "dummy"]

for driver in drivers_audio:
    try:
        print(f"Intentando inicializar audio con: {driver}")
        os.environ["SDL_AUDIODRIVER"] = driver
        pygame.mixer.pre_init(Audio.freq, Audio.bits, Audio.chan, Audio.buffer)
        pygame.mixer.init()
        print(f"Audio inicializado con: {driver}")
        break
    except pygame.error as e:
        print(f"Fallo con {driver}: {e}")

print(f"Driver de audio utilizado: {driver}")

# Inicializar Pygame y #wiringpi
pygame.init()
#pygame.mixer.pre_init(Audio.freq, Audio.bits, Audio.chan, Audio.buffer)  # 44.1kHz, 16-bit, estéreo, buffer 512
#pygame.mixer.init()
pygame.mixer.set_num_channels(24)
#wiringpi.#wiringpiSetup()

# Configuración de la ventana
WINDOW_WIDTH = 830
WINDOW_HEIGHT = 850

# Configurar ventana
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bottle Beats 0.2.0 Alpha")

# Fuentes
font = pygame.font.SysFont("Arial", 16)
font_small = pygame.font.SysFont("Arial", 12)

font_bold = pygame.font.SysFont("Arial", 18)
font_bold.set_bold(True)


# Pines GPIO para 24 LEDs
led_pins = [0, 7, 14, 15, 9, 6, 12, 10, 8, 4, 11, 2] * 2
#for pin in led_pins:
    #wiringpi.pinMode(pin, 1)

# Pre-cargar sonidos y configurar volúmenes/paneo
# Initialize channels for audio playback
channels = [pygame.mixer.Channel(i) for i in range(24)]
sound_objects = [pygame.mixer.Sound(file) for file in Samples.wav_files] # Default Sound Bank
sound_objects_2 = [pygame.mixer.Sound(file) for file in Samples.T909]
sound_objects_3 = [pygame.mixer.Sound(file) for file in Samples.C64]
sound_objects_4 = [pygame.mixer.Sound(file) for file in Samples.wav_files]

class Tabs:

    def __init__(self):
        self.confirm_close = False # Confirma si quiere salir de la aplicacion 

    def confirm_clse(self):
        Seq.playing = False
        Seq.pulsador_stop = True
        Botones.write_mode = False               # Quita el modo de escritura
        Botones.color_write = Botones.off_color     # Quita el color de escritura
        Seq.s_idx = 0       
        self.confirm_close = True
        
    def close(self, pos, running):
        
        if Botones.BTN_CLOSE_NO.collidepoint(pos) and self.confirm_close == True:
            self.confirm_close = False
            return running
        if Botones.BTN_CLOSE_YES.collidepoint(pos) and self.confirm_close == True:
            return False
        return running


Pestania = Tabs() # Make tabs object


class Buttons:
         
    def __init__(self):
        #self.confirm_close = False      # Confirma si quiere salir de la aplicacion 

        self.color_text = (255, 255, 255) # Color de texto de los botones
        self.color_actual = (255, 225, 255)
        self.on_color = (255, 0, 0)   # Color por defecto de los botones activos
        self.off_color = (60, 20, 20) # Color por defecto de los botones inactivos
        self.color_bank = [self.on_color, self.off_color, self.off_color, self.off_color] # Color por default de los bancos
                        
        self.color_bank_numbers = [self.on_color, self.off_color, self.off_color, self.off_color, self.off_color, self.off_color, self.off_color, self.off_color]
        
        self.bank_number = 0           # Nuero del digitos 1-8 del banco seleccionado
        self.number_state = [0] * 8
        self.number_state[0] = 1       # Inicia por defecto un valor en la primera posicion

        self.bank = 0                  # Numero del banco seleccionado A-B-C-D        
        self.state = [0] * 4
        self.state[0] = 1              # Inicia por defecto un valor en la primera posicion
        
        self.gupo = 0
        self.numero = 0

        self.color_write = self.off_color
        self.write_mode = False

        self.pulsador = False              # Control de botones de las flechas del song position
        self.pulsador_patt_num = False     # Control de pulsador de 1-8
        self.pulsador_bank_num = False     # Control de pulsador de banco A-B-C-D
                
        self.clipboard = [[0] * 16 for _ in range(24)] # Copied temp memory of active pattern
                  
        self.patterns_numeros = [[0] * 8 for _ in range(4)]

        self.color_copy = (self.off_color)
        self.color_paste = (self.off_color)
        self.COPY_BTN = pygame.Rect(700, 250, 50, 30)
        self.PASTE_BTN = pygame.Rect(760, 250, 50, 30)

        self.color_flechas_izq = (self.on_color)
        self.color_flechas_der = (self.on_color)

        self.skin_color = [self.off_color, self.off_color, self.off_color, self.off_color, self.off_color, self.off_color]

        self.BTN_CLOSE_NO = pygame.Rect(WINDOW_WIDTH / 3 - 50, WINDOW_HEIGHT / 3 + 50, 100, 40)
        self.BTN_CLOSE_YES = pygame.Rect(WINDOW_WIDTH / 3 + 70, WINDOW_HEIGHT / 3 + 50, 100, 40)
        self.BOX_CLOSE = pygame.Rect(WINDOW_WIDTH / 3 - 140, WINDOW_HEIGHT / 3 - 5, 400, 130)
        
        
        self.STOP_BUTTON = pygame.Rect(100, WINDOW_HEIGHT - 61, 80, 40)

        # Triangulos Flechas de Song Position
        self.T1V1 = (700 + 1, 190 - 19) # Vertices
        self.T1V2 = (730 + 1, 200 - 19) # Vertices
        self.T1V3 = (730 + 1, 180 - 19) # Vertices
        self.TRI_BL = [self.T1V1, self.T1V2, self.T1V3]  # Triangulo izquierdo
        self.T2V1 = (790 + 10, 190 - 19) # Vertices
        self.T2V2 = (760 + 10, 200 - 19) # Vertices
        self.T2V3 = (760 + 10, 180 - 19) # Vertices
        self.TRI_BR = [self.T2V1, self.T2V2, self.T2V3] # Triangulo derecho

        # Referencia de las flechas de Song Position
        self.RF_T1 = pygame.Rect(688, 160, 45, 30) # Botones de ref. triangulo 1
        self.RF_T2 = pygame.Rect(760, 160, 45, 30) # Botones de ref. triangulo 2        
        
        # Pattern BOX diseño cuadrado de la caja
        self.PTN_BOX_D = pygame.Rect(690, 290, 130, 170)

        # Pattern BOX 1-2-3-4-5-6-7-8
        self.PTN_1 = pygame.Rect(700, 300, 20, 25)
        self.PTN_2 = pygame.Rect(730, 300, 20, 25)
        self.PTN_3 = pygame.Rect(760, 300, 20, 25)
        self.PTN_4 = pygame.Rect(790, 300, 20, 25)
        self.PTN_5 = pygame.Rect(700, 330, 20, 25)
        self.PTN_6 = pygame.Rect(730, 330, 20, 25)
        self.PTN_7 = pygame.Rect(760, 330, 20, 25)
        self.PTN_8 = pygame.Rect(790, 330, 20, 25)
        
        # Pattern BOX A-B-C-D
        self.PTN_A = pygame.Rect(700, 380, 20, 25)
        self.PTN_B = pygame.Rect(730, 380, 20, 25)
        self.PTN_C = pygame.Rect(760, 380, 20, 25)
        self.PTN_D = pygame.Rect(790, 380, 20, 25)

        # Pattern BOX Write Mode
        self.PIN_WRITE = pygame.Rect(718, 430, 80, 22)
    
    

    def draw(self):
        draw_ref = False

        if Pestania.confirm_close == True:
            pygame.draw.rect(screen, (100, 0, 0), self.BTN_CLOSE_NO)
            pygame.draw.rect(screen, (100, 0, 0), self.BTN_CLOSE_YES)
            pygame.draw.rect(screen, (255, 0, 0), self.BOX_CLOSE, 1)

        pygame.draw.polygon(screen, self.color_flechas_izq, self.TRI_BL) # Triangle
        pygame.draw.polygon(screen, self.color_flechas_der, self.TRI_BR) # Triangle

        if draw_ref == True:
            pygame.draw.rect(screen, Color.r, self.RF_T1)
            pygame.draw.rect(screen, Color.r, self.RF_T2)
            print("Botones de referencia para los triangulos")
        
        pygame.draw.rect(screen, Color.w, self.PTN_BOX_D, 1)
        pygame.draw.rect(screen, self.color_copy, self.COPY_BTN)
        pygame.draw.rect(screen, self.color_paste, self.PASTE_BTN)
        
        pygame.draw.rect(screen, self.color_bank_numbers[0], self.PTN_1)
        pygame.draw.rect(screen, self.color_bank_numbers[1], self.PTN_2)
        pygame.draw.rect(screen, self.color_bank_numbers[2], self.PTN_3)
        pygame.draw.rect(screen, self.color_bank_numbers[3], self.PTN_4)
        pygame.draw.rect(screen, self.color_bank_numbers[4], self.PTN_5)
        pygame.draw.rect(screen, self.color_bank_numbers[5], self.PTN_6)
        pygame.draw.rect(screen, self.color_bank_numbers[6], self.PTN_7)
        pygame.draw.rect(screen, self.color_bank_numbers[7], self.PTN_8)
        
        pygame.draw.rect(screen, self.color_bank[0], self.PTN_A)
        pygame.draw.rect(screen, self.color_bank[1], self.PTN_B)
        pygame.draw.rect(screen, self.color_bank[2], self.PTN_C)
        pygame.draw.rect(screen, self.color_bank[3], self.PTN_D)

        pygame.draw.rect(screen, self.color_write, self.PIN_WRITE)

        pygame.draw.rect(screen, self.skin_color[0], COLOR_BTN1)
        pygame.draw.rect(screen, self.skin_color[1], COLOR_BTN2)
        pygame.draw.rect(screen, self.skin_color[2], COLOR_BTN3)
        pygame.draw.rect(screen, self.skin_color[3], COLOR_BTN4)
        pygame.draw.rect(screen, self.skin_color[4], COLOR_BTN5)
        pygame.draw.rect(screen, self.skin_color[5], COLOR_BTN6)
        
        pygame.draw.rect(screen, Color.g, Botones.STOP_BUTTON)
        
        
    def text(self):
        
        self.stop_text = font.render("Stop", True, Color.bg)
        
        self.confirm_close_txt = font_bold.render("Confirm close?", True, Color.w)
        self.conf_close_yes = font_bold.render("Yes", True, (255, 255, 255))
        self.conf_close_no = font_bold.render("No", True, (255, 255, 255))

        self.skin_txt = font.render("Skin color" , True, Color.w)
        self.patt_text = font.render(f"Pattern: {Seq.patt}", True, Color.w)
       
        self.song_pos_txt = font.render("Song position", True, Color.w)
        self.copy_text = font.render("Copy", True, Color.w)
        self.paste_text = font.render("Paste", True, Color.w)
        
        self.p1_text = font.render("1", True, self.color_actual)
        self.p2_text = font.render("2", True, self.color_actual)
        self.p3_text = font.render("3", True, self.color_actual)
        self.p4_text = font.render("4", True, self.color_actual)
        self.p5_text = font.render("5", True, self.color_actual)
        self.p6_text = font.render("6", True, self.color_actual)
        self.p7_text = font.render("7", True, self.color_actual)
        self.p8_text = font.render("8", True, self.color_actual)
        
        self.a_text = font.render("A", True, self.color_actual)
        self.b_text = font.render("B", True, self.color_actual)
        self.c_text = font.render("C", True, self.color_actual)
        self.d_text = font.render("D", True, self.color_actual)

        if self.write_mode == True:
            self.write_mode_text = font.render("Write", True, self.color_actual)
        else:
            self.write_mode_text = font.render("Read", True, self.color_actual)    
                        
    
    def show(self):
        if Pestania.confirm_close == True:
            screen.blit(self.confirm_close_txt, (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 3))
            screen.blit(self.conf_close_no, (self.BTN_CLOSE_NO.x + 35, self.BTN_CLOSE_NO.y + 10))
            screen.blit(self.conf_close_yes, (self.BTN_CLOSE_YES.x + 35, self.BTN_CLOSE_YES.y + 10))
            
        
        screen.blit(self.skin_txt, (COLOR_BTN1.x + 5, COLOR_BTN1.y - 22))
        screen.blit(self.patt_text, (705, 110))
        
        screen.blit(self.song_pos_txt, (705, 130))
        screen.blit(self.copy_text, (self.COPY_BTN.x + 5, self.COPY_BTN.y + 5))
        screen.blit(self.paste_text, (self.PASTE_BTN.x + 5, self.PASTE_BTN.y + 5))
        
        screen.blit(self.p1_text, (self.PTN_1.x + 6, self.PTN_1.y +5 ))
        screen.blit(self.p2_text, (self.PTN_2.x + 6, self.PTN_2.y +5 ))
        screen.blit(self.p3_text, (self.PTN_3.x + 6, self.PTN_3.y +5 ))
        screen.blit(self.p4_text, (self.PTN_4.x + 6, self.PTN_4.y +5 ))
        screen.blit(self.p5_text, (self.PTN_5.x + 6, self.PTN_5.y +5 ))
        screen.blit(self.p6_text, (self.PTN_6.x + 6, self.PTN_6.y +5 ))
        screen.blit(self.p7_text, (self.PTN_7.x + 6, self.PTN_7.y +5 ))
        screen.blit(self.p8_text, (self.PTN_8.x + 6, self.PTN_8.y +5 ))
        
        screen.blit(self.a_text, (self.PTN_A.x + 5, self.PTN_A.y +5 ))
        screen.blit(self.b_text, (self.PTN_B.x + 5, self.PTN_B.y +5 ))
        screen.blit(self.c_text, (self.PTN_C.x + 5, self.PTN_C.y +5 ))
        screen.blit(self.d_text, (self.PTN_D.x + 5, self.PTN_D.y +5 ))

        screen.blit(self.write_mode_text, (self.PIN_WRITE.x + 20, self.PIN_WRITE.y + 2))

        screen.blit(self.stop_text, (self.STOP_BUTTON.x + 10, self.STOP_BUTTON.y + 10))


    
    def stop_song_(self, pos):
        if self.STOP_BUTTON.collidepoint(pos):
            Seq.playing = False
            Seq.pulsador_stop = True
            self.write_mode = False               # Quita el modo de escritura
            self.color_write = self.off_color     # Quita el color de escritura
            
            Seq.s_idx = 0        


    def write_mode_button(self, pos):
        if self.PIN_WRITE.collidepoint(pos) and Seq.playing == False:  # Si se pulsa el botón de escritura o lectura
            self.write_mode = not self.write_mode                      # Cambiar el modo de escritura
            Seq.patt_state[Seq.apt - 1] = Seq.pattern_num              # Graba en el momento de presionar write mode

        if Seq.playing == True:
            self.write_mode = False

        if self.write_mode == True:
            self.color_write = self.on_color
        else:  
            self.color_write = self.off_color  
        
       
           
    def copy_paste(self, pos):
            if self.COPY_BTN.collidepoint(pos):
                #print("Pattern Copied ", "POS ", pos)
                self.color_copy = self.on_color
                for channel_idx in range(24):
                    for step_idx in range(16):
                        self.clipboard[channel_idx][step_idx] = Patt.mtx_p[Seq.patt - 1][channel_idx][step_idx]
                    
            
            if self.PASTE_BTN.collidepoint(pos):
                #print("Pattern Copied ", "POS ", pos)
                self.color_paste = self.on_color
                for channel_idx in range(24):
                    for step_idx in range(16):
                        Patt.mtx_p[Seq.patt - 1][channel_idx][step_idx] = self.clipboard[channel_idx][step_idx]

    
    def reset_colors_copy_paste(self):
        if not hasattr(self, '_last_reset_time'):
            self._last_reset_time = pygame.time.get_ticks()
        
        current_time = pygame.time.get_ticks()
        if current_time - self._last_reset_time > 200:  # 500 ms delay
            self.color_copy = self.off_color
            self.color_paste = self.off_color
            self._last_reset_time = current_time
        
 
    def reset_colors_flechas_song_position(self):
        if not hasattr(self, '_last_reset_time_'):
            self._last_reset_time_ = pygame.time.get_ticks()
        
        current_time_ = pygame.time.get_ticks()
        if current_time_ - self._last_reset_time_ > 200:
            self.color_flechas_izq = self.off_color
            self.color_flechas_der = self.off_color
            self._last_reset_time_ = current_time_

    def pattern_sel(self):
        # Obtener el índice del botón activo (A=0, B=1, C=2, D=3)
        self.grupo = self.state.index(1)  
        # Obtener el índice del botón numérico activo (1 al 8)
        self.numero = self.number_state.index(1) + 1  
        # Calcular el valor total
        valor = self.grupo * 8 + self.numero
        print("VALOR PATTERNS ", valor)
        Seq.pattern_num = valor

        
        
        
     
    def toggle_bank(self, bank, button, pos):
               
        if button.collidepoint(pos) and not Seq.playing:

            self.pulsador_bank_num = True
            # Si el banco ya está activo, no hace nada
            if self.state[bank] == 1:
                print("Bank already active, no changes made.")
                return
            
            # Desactiva todos los demás bancos y resetea sus patrones
            for i in range(4):
                if i != bank:
                    self.state[i] = 0
                    self.color_bank[i] = self.off_color
                    for nums in range(8):
                        #print("Nums ---------------------------------", nums)
                        self.patterns_numeros[i][nums] = 0

            # Activa el banco seleccionado
            self.state[bank] = 1
            self.color_bank[bank] = self.on_color
            # Marca el patrón actual en ese banco
            self.patterns_numeros[bank][self.bank_number] = 1
            
            self.pattern_sel()

            print(f"Activando bank {bank}, bank_number: {self.bank_number}")
            print("Estado de bancos: ", self.state)
                          

    def handle_patterns(self, pos):
        self.toggle_bank(0, self.PTN_A, pos)
        self.toggle_bank(1, self.PTN_B, pos)
        self.toggle_bank(2, self.PTN_C, pos)
        self.toggle_bank(3, self.PTN_D, pos)
        

        


    
    def handle_pattern_numbers(self, pos):
        if not Seq.playing:
            for num, button in enumerate([self.PTN_1, self.PTN_2, self.PTN_3, self.PTN_4, 
                                          self.PTN_5, self.PTN_6, self.PTN_7, self.PTN_8]):
                if button.collidepoint(pos):
                    self.number_state = [1 if i == num else 0 for i in range(8)]
                    self.color_bank_numbers = [self.on_color if i == num else self.off_color for i in range(8)]
                    self.pulsador_patt_num = True
                    self.pattern_sel()
                    print(f"Botón {num + 1}")
                    
                    break
        
        # Mostrar el valor de pattern y los bancos seleccionados      
        for i in range(8):
            print("Numbers 1-8 ", self.number_state[i])

        for i in range(4):
            print("Banks A-B-C-D ", self.state[i])
    
    

    def handle_botones_triangulo(self, pos):
        print("Valor de la pattern en la funcion botones del trianguos", Seq.patt, "La posicion de la cancion es ", Seq.apt)    
        if self.RF_T1.collidepoint(pos) and Seq.apt > 1 : # Triangulo izquierdo
            if pygame.mouse.get_pressed()[0]:
               self.color_flechas_izq = self.on_color
               Seq.apt -= 1
               self.pulsador = True        # Controla si se pulso
         
         
        if self.RF_T2.collidepoint(pos) and Seq.apt < 32 and Seq.apt < Seq.tpt: # Triangulo derecho
            if pygame.mouse.get_pressed()[0]:
               self.color_flechas_der = self.on_color
               Seq.apt += 1
               self.pulsador = True        # Controla si se pulso
               
              
Botones = Buttons() # Make Object from class Buttons               
                


## - CONSTANTES - ##

# Configuración de los pasos, volúmenes y paneo
STEP_WIDTH = 20
STEP_HEIGHT = 25
STEP_MARGIN = 5
COLOR_SIZE = 20
CHANNEL_HEIGHT = STEP_HEIGHT + STEP_MARGIN
VOL_WIDTH = 40
VOL_HEIGHT = 20
PAN_WIDTH = 60  # Definimos ancho para el paneo
PAN_HEIGHT = 20
DRAW_X = 150  # Posición inicial x de steps

# Botones y cuadros

PLAY_BUTTON = pygame.Rect(10, WINDOW_HEIGHT - 61, 80, 40)

TEMPO_BOX = pygame.Rect(200, WINDOW_HEIGHT - 61, 117, 40)
MASTER_VOL_BOX = pygame.Rect(320, WINDOW_HEIGHT - 61, 130, 40)
PATTERN_BOX = pygame.Rect(690, 152, 130, 40)
PATTERN_TOTAL = pygame.Rect(690, 190, 130, 40)
SETTING_BOX = pygame.Rect(PATTERN_TOTAL.x, PATTERN_TOTAL.y + 350, 95, 60)

# Botones load/save y menú desplegable para las memorias
SAVE_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 61, 80, 40)
LOAD_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 105, 80, 40)
MENU_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 155, 100, 40)

COLOR_BTN1 = pygame.Rect(MASTER_VOL_BOX.x + 220 + 22, WINDOW_HEIGHT - 65, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN2 = pygame.Rect(MASTER_VOL_BOX.x + 250 + 22, WINDOW_HEIGHT - 65, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN3 = pygame.Rect(MASTER_VOL_BOX.x + 280 + 22, WINDOW_HEIGHT - 65, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN4 = pygame.Rect(MASTER_VOL_BOX.x + 220 + 22, WINDOW_HEIGHT - 40, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN5 = pygame.Rect(MASTER_VOL_BOX.x + 250 + 22, WINDOW_HEIGHT - 40, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN6 = pygame.Rect(MASTER_VOL_BOX.x + 280 + 22, WINDOW_HEIGHT - 40, COLOR_SIZE, COLOR_SIZE)

BNK_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 205, 95, 40)

MENU_WIDTH = 100
MENU_ITEM_HEIGHT = 30
MENU_ITEMS = 10  # 10 memorias (1 a 10)

# Variable para el nombre del preset
current_preset = "default_preset"

LED_DURATION = 50