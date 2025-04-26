from .main_classes import Settings

import pygame

class Button(Settings):
    def __init__(self, x, y, width, height, image):
        super().__init__(x = x, y = y, width = width, height = height, image = image)
    
    def show_image(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def check_click(self, position_mouse_x, position_mouse_y):
        if position_mouse_x >= self.x:
            if position_mouse_x <= self.x + self.width:
                if position_mouse_y >= self.y:
                    if position_mouse_y <= self.y + self.height:
                        return False
        return True

    def screen_darkness(self, screen):
        black_fill = pygame.Surface((1200, 800))
        black_fill.fill((0,0,0))
        black_fill.set_alpha(83)
        screen.blit(black_fill, (0, 0))
    
    def text(self, screen, text, size):
        f1 = pygame.font.Font(None, size)
        text1 = f1.render(f"{text}", 1, (0, 0, 0))
        screen.blit(text1, (self.x, self.y))

def menu(screen: pygame.Surface):
    menu_run = True
    button1 = Button(525, 250, 190, 100, image = "images/resources/play.png")
    exit1 = Button(525, 450, 190, 100, image = "images/resources/exit.png")
    while menu_run:
        screen.fill((0, 0, 0))
        button1.show_image(screen)
        exit1.show_image(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False
                return False
            
            if event.type == pygame.MOUSEMOTION:
                position_mouse = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                menu_run = button1.check_click(position_mouse[0], position_mouse[1])
                if menu_run == False:
                    return True
                menu_run = exit1.check_click(position_mouse[0], position_mouse[1])
                if menu_run == False:
                    return False

        pygame.display.flip()