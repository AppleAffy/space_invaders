import pygame
import sys
from objects import image
import random

class player(image.still):
        
    def __init__(self, x, y,width,height,image_to_use,speed):# bob = interactions.player(10,20,200,100,"images/image_show.png",1)
        super().__init__(x, y,width,height,image_to_use)
        self.speed = speed
        self.shoot_cooldown = 1000
        self.last_shot_time = 0


    def keys_pressed(self, boolean_x, boolean_y):
        self.key_input = pygame.key.get_pressed()
        global new_bullet
        new_bullet = None
        if boolean_x:
            self.move_x = (self.key_input[pygame.K_RIGHT]*self.speed) + (self.key_input[pygame.K_LEFT] * -self.speed)
            self.rect.x += self.move_x
        if boolean_y:
            self.move_y = (self.key_input[pygame.K_DOWN]* self.speed) + (self.key_input[pygame.K_UP] *-self.speed)
            self.rect.y += self.move_y
        if self.key_input[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time >= self.shoot_cooldown:
                bullet_x = self.rect.x + 12
                new_bullet =  image.still(bullet_x,self.rect.y,50,70,"images/laser.png")
                self.last_shot_time = current_time
            return new_bullet
        
    def move_back(self, boolean_x, boolean_y):
        if boolean_x:
            self.rect.x -= self.move_x
        if boolean_y:
            self.rect.y -= self.move_y
    
 

    def collision(object1, object2):
        return object1.rect.colliderect(object2)
    
class enemy(image.still):
    global direction,enemy_shoot_delay,last_enemy_shot_time

    direction = 1 # this stuff is shred across oall objects of teh class
    
    enemy_index = [] # keeps a record of all the objects in the class
    global speed
    speed = 0.5 # shared across all 
    last_enemy_shot_time = 0
    enemy_shoot_delay = 2000
    def __init__(self, x, y,width,height,image_to_use):
        super().__init__(x, y,width,height,image_to_use)
        self.start_x = x
        self.start_y = y
        enemy.enemy_index.append(self)
        
    def move_preplaned(obj_list,x1,x2,max_enemy_len):    
        global direction,speed
        hitwall = False
        
        for e in obj_list:
            if e.rect.x >= x2 or e.rect.x <= x1:
                hitwall = True
                break
        if hitwall:
            direction *= -1 # multiplyuing by -1 reverses the direction
            for e in obj_list:
                e.rect.y += 25
                if e.rect.y >= 875:
                    print("game over")
                    break
        for e in obj_list:
            e.rect.x += direction * speed
            speed = (max_enemy_len + 1) - len(obj_list)
        
   

        
    def enemy_shoot(obj_list): # enemy shoot
        global last_enemy_shot_time, enemy_shoot_delay
        shots = []
        current_time = pygame.time.get_ticks()

        if current_time - last_enemy_shot_time >= enemy_shoot_delay:
            for i, e in enumerate(obj_list):
                shoot_chance = random.randint(0, 3)
                print(f"shoot chance {shoot_chance}")
                if shoot_chance == 1:
                    print(f"enemy {i} shoot")
                    new_enemy_bullet = image.still(e.rect.x+12, e.rect.y, 50, 70, "images/laser.png")
                    shots.append((i, new_enemy_bullet))
            last_enemy_shot_time = current_time

        return shots

        
   
