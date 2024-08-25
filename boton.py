import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Inicializa los atributos del botón."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Establece las dimensiones y propiedades del botón
        self.width, self.height = 360, 60
        self.button_color = (183, 0, 166)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Cooper Black', 35)

        # Construye el rectángulo del botón y lo centra
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # El mensaje del botón debe ser preparado solo una vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Convierte msg en una imagen renderizada y la centra en el botón."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Dibuja el boton y el mensaje
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)   