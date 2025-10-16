import interfaces
import pygame,sys
from objects import grid,image,interactions
import manager
#hello
def output(window:pygame.surface.Surface):
    global shields
    running = True
    manager.initial = False
    #Setup of Starting objects

    window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
    pygame.display.set_caption("Space Invaders")
    
   
    spaceship_player = interactions.player(450,800,75,75,"images/space_invaders_player.png",7)
    spaceship_enemy1 = interactions.enemy(450,100,75,75,"images/space_invaders_enemy.png") 
    spaceship_enemy2 = interactions.enemy(375,175,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy3 = interactions.enemy(525,175,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy4 = interactions.enemy(375,250,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy5 = interactions.enemy(525,250,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy6 = interactions.enemy(275,225,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy7 = interactions.enemy(625,225,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy8 = interactions.enemy(275,300,75,75,"images/space_invaders_enemy.png")
    spaceship_enemy9 = interactions.enemy(625,300,75,75,"images/space_invaders_enemy.png")
    bullets = []
    enemy_bullets = []
    # Each shield is a dictionary holding its rect, color, and health
    shields = [
        {"rect": pygame.Rect(450, 700, 125, 50), "color": (0, 255, 0), "health": 5},
        {"rect": pygame.Rect(100, 700, 125, 50), "color": (0, 255, 0), "health": 5},
        {"rect": pygame.Rect(775, 700, 125, 50), "color": (0, 255, 0), "health": 5}
    ]

    enemy_list = [spaceship_enemy1,spaceship_enemy2,spaceship_enemy3, spaceship_enemy4, spaceship_enemy5,spaceship_enemy6, spaceship_enemy7, spaceship_enemy8, spaceship_enemy9]
    max_enemy_len = len(enemy_list)

    def display():
      global shield_list
      global wall_list
      window.fill((0,0,0)) #White background
      #grid.gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT)
      spaceship_player.draw(window)
      for bullet in bullets:
        bullet.draw(window)
      for bullet in enemy_bullets:
        bullet.draw(window)
      for enemy in enemy_list:
        enemy.draw(window)
      
      for shield in shields:
        pygame.draw.rect(window, shield["color"], shield["rect"])
      wall1 = pygame.draw.rect(window,(255,0,0),(25,25,25,950))
      wall2 = pygame.draw.rect(window,(255,0,0),(25,25,950,25))
      wall3 = pygame.draw.rect(window,(255,0,0),(950,25,25,950))
      wall4 = pygame.draw.rect(window,(255,0,0),(25,950,950,25))
      
      wall_list = [wall1,wall2,wall3,wall4]
   
    display()

    while running:
        
        interactions.enemy.move_preplaned(enemy_list,50,875,max_enemy_len)

        shots = interactions.enemy.enemy_shoot(enemy_list)
        for index, bullet in shots:
            enemy_bullets.append(bullet)
        for bullet in enemy_bullets:
          bullet.rect.y += 10
          if bullet.rect.y > manager.WINDOW_HEIGHT -25:
            enemy_bullets.remove(bullet)
        for bullet in enemy_bullets:
            if pygame.sprite.collide_mask(bullet,spaceship_player): # collision with player and enemy bullets
              print("You Lose")
              manager.win = 3
              running = False
              manager.screen = 0
        for shield in shields:  
          for bullet in enemy_bullets:
              if shield["rect"].colliderect(bullet.rect):
                  enemy_bullets.remove(bullet)
                  # reduce shield health
                  shield["health"] -= 1
                  # So the player knows it gets weaker
                  green = max(0, shield["color"][1] - 50)  # 50 less green per hit
                  shield["color"] = (0, green, 0)
                  if shield["health"] <= 0: # taking doubl hit inot consideration
                      shields.remove(shield)
                  break
          for bullet in bullets:
              if shield["rect"].colliderect(bullet.rect):
                  bullets.remove(bullet)
                  # reduce shield health
                  shield["health"] -= 1
                  # So the player knows it gets weaker
                  green = max(0, shield["color"][1] - 50)  # 50 less green per hit
                  shield["color"] = (0, green, 0)
                  if shield["health"] <= 0: # taking doubl hit inot consideration
                      shields.remove(shield)
                  break

        if len(enemy_list) == 0: # all enemies dead?
          running = False
          manager.win = 2
          manager.screen = 0
        for enemy in enemy_list:
          if pygame.sprite.collide_mask(spaceship_player,enemy):# Game Over if all enemies are dead or if they hit player
            running = False
            manager.win = 3
            manager.screen = 0
        #Bullet code and movement aswell as reactions to differnet objects and values
        new_bullet = spaceship_player.keys_pressed(True, False)# take scare of movement AND bullets
        if new_bullet:  # if space was pressed
          bullets.append(new_bullet) # add the created bullet into the list
          
       
        for bullet in bullets:# there only eve one bullet at a time so this is fine as line 70 tkaes care of it
            bullet.rect.y -= 10 # since i want it to go up not down, i make it negative
            for enemy in enemy_list:
              if pygame.sprite.collide_mask(bullet,enemy): # avoid nasty hitbox, and go for spirtite collsion check instead
                bullets.remove(bullet)
                enemy_list.remove(enemy)
              if pygame.sprite.collide_mask(spaceship_player,enemy): # the slowly come down towards the player, so have to take this into consideration
                running = False
                manager.win = 3
                manager.screen = 0
            if bullet.rect.y < 0:
                bullets.remove(bullet)
                print(len(bullets))

        for walls in wall_list:
          if interactions.player.collision(spaceship_player,walls):
            interactions.player.move_back(spaceship_player,True,False)
      
    
          



        display()
        for event in pygame.event.get():
          # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
          
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw
