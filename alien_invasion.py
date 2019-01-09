import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():

	# Inicializa o pygame e carrega as configurações de settings
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Cria uma espaçonave
	ship = Ship(ai_settings, screen)
	# Cria um grupo para armazenato dos projeteis
	bullets = Group()
	
	# Inicia o laço principal do jogo
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()