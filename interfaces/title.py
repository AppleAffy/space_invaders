import pygame,sys
import objects.buttons
import manager
from objects import image

def output(window:pygame.surface.Surface):
    global play_msg
    global button_off
    button_off = False
    if manager.initial:
        play_msg = "Click to Play"
    elif manager.initial == False:
        play_msg = "Click to Retry"
    global title_image
    title_image = "images/space_invaders.png"
    if manager.win == 2:
        title_image = "images/space_invaders_win.png"
    elif manager.win == 3:
        title_image = "images/space_invaders_lose.png"
        manager.score = 0
    btn_play = objects.buttons.no_background(425,500,"Arial",30,(235, 64, 52),(98, 52, 235),play_msg)
    btn_tutorial = objects.buttons.no_background(450,600,"Arial",30,(235, 64, 52),(98, 52, 235),"Tutorial")
    btn_exit = objects.buttons.no_background(475,700,"Arial",30,(235, 64, 52),(98, 52, 235),"Exit")
    title_screen = image.still(150,50,700,400,title_image)
    def display():
        window.fill((0,0,0)) #White background
        if button_off == False:
            btn_exit.draw(window)
            btn_play.draw(window)
            btn_tutorial.draw(window)
            title_screen.draw(window)
            objects.text.blit_text(window,"Space Invaders: Here's how you play the game ",(100,100),manager.font,pygame.Color("White"))

    
    
    
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
            if btn_tutorial.update(pygame.mouse.get_pos(),event):
                button_off = True
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw