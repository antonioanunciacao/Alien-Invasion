# Classe de configurações gerais

class Settings():
	"""Uma classe para armazenar todas as configurações do jogo."""
	
	def __init__(self):
		"""Inicializa as configurações do jogo."""
		# Configurações da tela
		self.screen_width = 1200
		self.screen_height = 674
		self.bg_color = (230, 230, 230)
		
		# Confugurações de nave
		self.ship_speed_factor = 1.5
		
		# Configurações dos projéteis
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)