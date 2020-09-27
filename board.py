#here is where im going to generate the code to make the board and the window
import pygame

# Init
pygame.init()

class board:
    def __init__(self, dis_width, dis_height, dis, caption):
        caption = "Snaek game Rasmus"
        dis_width = 600
        dis_height = 600
        dis = pygame.display.set_mode((dis_width, dis_width))
        pygame.display.set_caption(caption)