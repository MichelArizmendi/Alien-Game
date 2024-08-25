#Clase para grabar estadisticas del juego

class GameStats():
    """Seguimiento de las estadísticas del juego"""

    def __init__(self, ai_settings):
        """Inicializa las estadísticas"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Inicia el juego en un estado activo
        self.game_active = False

        #La puntuación más alta nunca debe reiniciarse
        self.high_score = 0

        

    def reset_stats(self):
        """Inicializa las estadísticas que pueden cambiar durante el juego"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # self.level = 1