import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ uma classe que representa um único alienigena da frota"""
    def __init__(self, ai_settings,screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo recente
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        """ Desenha o alienigena em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ Devolve True se o alienigena estiver na borda da tela"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """ Move o alienigena para a direita"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        