# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:41:10 2023

@author: Jaime Lomeli y Monjaraz Luis
"""

import threading
import time
import random
import keyboard
import os

# Buffer
buffer = [' ']*20
indice_productor = 0
indice_consumidor = 0

# Variable para controlar si el programa debe continuar ejecutándose
running = True

class Productor(threading.Thread):
    def run(self):
        global buffer
        global indice_productor
        while running:
            elementos_producir = random.randint(4, 7)
            for _ in range(elementos_producir):
                if buffer[indice_productor] == ' ':
                    buffer[indice_productor] = random.choice(['a', 'b', 'c', '1', '2', '3', '#', '@', '&'])
                    print('\n')
                    print(f'Productor trabajando, produjo: {buffer[indice_productor]}')
                    indice_productor = (indice_productor + 1) % 20
                else:
                    print('Productor durmiendo')
                    break
            print(f'Buffer: {list(enumerate(buffer, start=1))}')
            time.sleep(random.randint(3, 6))
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla

class Consumidor(threading.Thread):
    def run(self):
        global buffer
        global indice_consumidor
        while running:
            elementos_consumir = random.randint(4, 7)
            for _ in range(elementos_consumir):
                if buffer[indice_consumidor] != ' ':  
                    print('\n')
                    print(f'Consumidor trabajando, consumió: {buffer[indice_consumidor]}')
                    buffer[indice_consumidor] = ' '  
                    indice_consumidor = (indice_consumidor + 1) % 20
                else:
                    print('Consumidor durmiendo')
                    break
            print(f'Buffer: {list(enumerate(buffer, start=1))}')
            time.sleep(random.randint(4, 8))
            os.system('cls' if os.name == 'nt' else 'clear')

# Función para detectar la tecla ESC y detener el programa
def check_for_escape_key(e):
    global running
    running = False

p = Productor()
c = Consumidor()


keyboard.on_press_key("esc", check_for_escape_key)

p.start()
c.start()

p.join()
c.join()
