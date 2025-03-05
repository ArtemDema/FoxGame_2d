import pygame

list_of_text = []

class TextClass():
    def __init__(self, x, y, size, text):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.font1 = pygame.font.Font("fonts/daydream.ttf", size = self.size)
        self.text1 = self.font1.render(self.text, 1, (255, 255, 255))
    def render_text(self, screen):
        screen.blit(self.text1, (self.x, self.y))