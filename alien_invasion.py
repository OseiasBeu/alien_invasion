import pygame
from pygame.sprite import Group
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
    ship = Ship(ai_settings, screen)

    #Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    # Cria um alienigena
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    
    #Cria frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True: 
        gf.check_events(ai_settings, screen,ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        # Observa eventos de teclado e de mouse
        # Redesenha a tela a cada passagem pelo laço
run_game()

