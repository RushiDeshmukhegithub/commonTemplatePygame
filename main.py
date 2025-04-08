import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game Name")


def load_image(path,pos,size):
    img = pygame.image.load(path)
    return pygame.transform.scale(img,size)


def game_loop():
    while(True):
        screen.fill((255,255,255))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return

game_loop()
