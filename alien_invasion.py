import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela 
    pygame.init()
    ai_settings = Settings()

    # # Define a cor de fundo
    # bg_color = (230, 230, 230)

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Cria uma espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        # Observa eventos de teclado e de mouse
        # Redesenha a tela a cada passagem pelo laço
run_game()
