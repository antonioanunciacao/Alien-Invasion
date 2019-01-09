import sys
import pygame

def check_keydown_events(event, ship):
	"""Responde a pressionamento de tecla"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event, ship):
	"""Responde a soltura de tecla"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ship):
	"""Responde a eventos de pressionamento de teclas e mouse."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
				
def update_screen(ai_settings, screen, ship):
	"""Atualiza imagens na tela"""
	#Redesenha a tela a cada ciclo do laço
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	#Atualiza tela
	pygame.display.flip()