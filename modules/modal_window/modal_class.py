from ..main_classes import Settings

import pygame, random

pygame.init()


class Modal_Window(Settings):
    def __init__(self, text):
        self.text = text
        self.you_claim = pygame.font.Font(None, 56)
        self.what_claim = pygame.font.Font(None, 58)
        self.width = 120
        self.height = 100
        self.x_continue = 600 - self.width // 2 - 60
        self.y_continue = 600

    def print_text_on_screen(self, WIDTH, HEIGHT, screen, claim):
        self.width = 120

        black_fill = pygame.Surface((WIDTH, HEIGHT))
        black_fill.fill((0,0,0))
        black_fill.set_alpha(83)
        screen.blit(black_fill, (0, 0))

        text = self.you_claim.render("You open the chest and claim:", True, (255, 255, 255)) #текст, сглаживание, цвет
        screen.blit(text, (WIDTH // 2 - 280, HEIGHT // 2 - 150))

        if claim == "nothing":
            text = self.what_claim.render(claim, True, (255, 255, 255))
            self.image = "images/resources/nothing.jpg"
            self.load_image() 
            screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2 + 50))
        elif claim == "meat":
            self.image = "images/resources/meat.png"
            self.width = 150
            self.load_image()
        elif claim == "egg":
            self.image = "images/resources/egg.png"
            self.width = 100
            self.load_image()
        else:
            self.image = "images/resources/heart.png"
            self.load_image()
        
        screen.blit(self.image, (WIDTH // 2 - (self.width // 2), HEIGHT // 2 - 60))

        self.image = "images/resources/continue.png"
        self.width = 225
        self.load_image()
        screen.blit(self.image, (self.x_continue, self.y_continue))
        



modal_w = Modal_Window(random.randint(0, 3))