import sys
import pygame
from settings import Settings
from ship import Ship


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
        # Observa eventos de teclado e de mouse
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()
