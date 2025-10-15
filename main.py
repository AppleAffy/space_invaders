#By: <Affan Qadeer>
#Date: 2025-09-18
#Program Details: <Space Invaders in pyhton. The official ripoff>
from objects import grid, image, interactions
import pygame,sys
import manager
import pygame,sys
import interfaces.game
import interfaces.title
import interfaces.retry
pygame.init()


#Setup of Starting objects

window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Maze")

while True:
    if manager.screen == 0:
        interfaces.title.output(window)
    elif manager.screen == 1:
        interfaces.game.output(window)
    elif manager.screen == 2:
        interfaces.retry.output(window)
