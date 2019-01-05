import sys
import pygame

from settings import Settings

def run_game():
	# Inicializa o pygame e carrega as configurações de settings
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Inicia o laço principal do jogo
	while True:
		# Observa eventos do teclado e mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		# Atualiza tela
		screen.fill(ai_settings.bg_color)
		pygame.display.flip()
		
run_game()