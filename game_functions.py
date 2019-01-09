import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Responde a pressionamento de tecla"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# Cria um novo projetil e o adciona ao grupo de projeteis
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""Responde a soltura de tecla"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""Responde a eventos de pressionamento de teclas e mouse."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
				
def update_screen(ai_settings, screen, ship, bullets):
	"""Atualiza imagens na tela"""
	#Redesenha a tela a cada ciclo do laço
	screen.fill(ai_settings.bg_color)
	
	# Redesenha todos os projeteis atras da nave e dod alienigenas
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	
	#Atualiza tela
	pygame.display.flip()