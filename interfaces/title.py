import pygame,sys
import objects.buttons
import manager
from objects import image

def output(window:pygame.surface.Surface):
    btn_play = objects.buttons.no_background(500,500,"Arial",30,(235, 64, 52),(98, 52, 235),"Click to Play")
    btn_exit = objects.buttons.no_background(500,600,"Arial",30,(235, 64, 52),(98, 52, 235),"Exit")
    title_screen = image.still(150,50,700,400,"images/space_invaders.png")
    def display():
        window.fill((0,0,0)) #White background
        btn_exit.draw(window)
        btn_play.draw(window)
        title_screen.draw(window)
    
    
    
    display()
    run = True
    while run:
        display()
        for event in pygame.event.get():
            if btn_play.update(pygame.mouse.get_pos(),event):
                manager.screen = 1
                run = False
            if btn_exit.update(pygame.mouse.get_pos(),event):
                sys.exit()
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw