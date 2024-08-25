class Settings():
    # Clase para almacenar todas las configuraciones del juego

    def __init__(self):
        # Inicializa la configuración del juego
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (19,27,58)

        # Configuración de la nave
        self.ship_limit = 3

        # Configuración de la bala
        self.bullet_width = 40
        self.bullet_height = 30
        self.bullet_color = 255, 176, 251
        self.bullets_allowed = 3

        # Ajusta la velocidad del juego
        self.speedup_scale = 1.1  # Asegúrate de que este valor sea mayor que 1.0

        #que tan rápido aumenta el puntaje de los aliens
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Inicializa las configuraciones que cambian a lo largo del juego
        self.ship_speed_factor = 1.3
        self.bullet_speed_factor = 1.2
        self.alien_speed_factor = 0.3

        # fleet_direction de 1 representa la derecha; -1 representa la izquierda
        self.fleet_direction = -1

        self.aliens_points = 10

    def increase_speed(self):
        # Ajusta la velocidad de la nave, de la bala y de los aliens
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.aliens_points = int(self.aliens_points * self.score_scale)
        print(self.aliens_points)
