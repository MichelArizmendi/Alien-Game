#Guardar y cargar score
import pygame.font

class Scoreboard():
    """Clase para guardar info de score"""

    def __init__(self, ai_settings, screen, stats):
        """Inicializa los atributos de score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configuración de la fuente para mostrar puntajes
        self.text_color = (255,240,254)
        self.font = pygame.font.SysFont('Cooper Black', 48)

        # Prepara la imagen de score inicial
        self.prep_score()
        self.prep_high_score() #se llama a la función para preparar el puntaje máximo
    
    def prep_score(self):
        """Convierte el puntaje en una imagen renderizada"""
        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Muestra el puntaje en la esquina superior derecha de la pantalla
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Dibuja el puntaje en la pantalla"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
    
    def prep_high_score(self):
        """Convierte el puntaje máximo en una imagen renderizada"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
         # Muestra el puntaje máximo en la esquina superior izquierda de la pantalla
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20  # Ajusta la posición según sea necesario
        self.high_score_rect.top = 20