# pygame template 
import math
import time
import random
import pygame
from pygame.draw import circle
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Fruit Click")
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

#TEXT FONTS AND SIZES
score_font = pygame.font.SysFont('Press Start 2P', 50)
lose_font = pygame.font.SysFont('Press Start 2P', 100)

#COORDINATES: sets of predetermined x and y coords for each fruit, y intervals of -300
watermelon_coords = [[140, 0], [220, -400], [450, -1500]]
cantaloupe_coords = [[320, -300], [570, -900], [80, -1800]]
orange_coords = [[620, -2000], [100, -4000], [400, -7000]]
kiwi_coords = [[270, -3000], [300, -6000], [500, -8000]]
bomb_coords = [[100, 0], [220, -900], [400, -1200]]
watermelon_radius = 50
cantaloupe_radius = 40
orange_radius = 25
kiwi_radius = 19
bomb_radius = 30
fruit_speed = 4
framecount = 0
hearts = 3
score = 0

# ---------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
## Pedram (SCORE COUNTER) Credit - inspired by SiggyWithACiggy from discord and Mr.Gallo ##
        # check if user clicked the mouse
        elif event.type == MOUSEBUTTONDOWN:
            # get the position of the mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            #check if the mouse click hits the watermelon
            for watermelon in watermelon_coords:
                # calculate the distance between mouse click and fruit
                watermelon_dist = math.sqrt((mouse_x - watermelon[0])**2 + (mouse_y - watermelon[1])**2)
                if watermelon_dist <= watermelon_radius:
                    score += 10
                    watermelon[1] = HEIGHT + 30 # teleports watermelon off-screen to respawn again
                    break
                    
            #check if the mouse click hits the cantaloupe
            for cantaloupe in cantaloupe_coords:
                # calculate the distance between mouse click and fruit
                cantaloupe_dist = math.sqrt((mouse_x - cantaloupe[0])**2 + (mouse_y - cantaloupe[1])**2)
                if cantaloupe_dist <= cantaloupe_radius:
                    score += 10
                    cantaloupe[1] = HEIGHT + 30 # teleports cantaloupe off-screen to respawn again
                    break 
                    
            #check if the mouse click hits the orange
            for orange in orange_coords: 
                # calculate the distance between mouse click and fruit
                orange_dist = math.sqrt((mouse_x - orange[0])**2 + (mouse_y - (orange[1]- 20))**2)
                if orange_dist <= orange_radius + 10:
                    score += 20
                    orange[1] = HEIGHT + 30 # teleports orange off-screen to respawn again
                    break 
                    
            #check if the mouse click hits the kiwi
            for kiwi in kiwi_coords: 
                # calculate the distance between mouse click and fruit
                kiwi_dist = math.sqrt((mouse_x - kiwi[0])**2 + (mouse_y - (kiwi[1] - 20))**2)
                if kiwi_dist <= kiwi_radius + 10:
                    score += 30
                    kiwi[1] = HEIGHT + 30 # teleports kiwi off-screen to respawn again
                    break 
                    
            #check if the mouse click hits the bomb
            for bomb in bomb_coords:
                # calculate the distance between mouse click and bomb
                bomb_dist = math.sqrt((mouse_x - bomb[0])**2 + (mouse_y - bomb[1])**2)
                if bomb_dist <= bomb_radius:
                    hearts -= 1
                    score = 0
                    bomb[1] = HEIGHT + 30 # teleports bomb off-screen to respawn again
                    break

    

    ## TARA (FRUIT DRAWING FUNCTIONS) ##

    def draw_watermelon(watermelon_coords):
        
        pygame.draw.circle(screen, (79,121,66), (watermelon_coords), watermelon_radius)  
        pygame.draw.circle(screen,(255,36,0),(watermelon_coords), watermelon_radius - 10)

        #loops through each x/y coordinate pair, draws seeds in relation to center of each watermelon
        for watermelon in watermelon_coords:
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +28, watermelon_coords[1] -10), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +28, watermelon_coords[1] +5), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +23, watermelon_coords[1] +20), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +12, watermelon_coords[1] +29), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -6, watermelon_coords[1] +30), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -22, watermelon_coords[1] +20), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -31, watermelon_coords[1] +6), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -31, watermelon_coords[1] -11), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -21, watermelon_coords[1] -25), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -6, watermelon_coords[1] -31), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +8, watermelon_coords[1] -30), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +22, watermelon_coords[1] -26), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -15, watermelon_coords[1] -9), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -12, watermelon_coords[1] +8), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +2, watermelon_coords[1] +14), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +14, watermelon_coords[1] +4), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] +15, watermelon_coords[1] -14), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0] -3, watermelon_coords[1] -19), watermelon_radius - 47)
            pygame.draw.circle(screen,(0,0,0),(watermelon_coords[0], watermelon_coords[1] -4), watermelon_radius - 47)

    def draw_cantaloupe(cantaloupe_coords):
        #loops through each x/y coordinate pair, draws outline and seeds in relation to center of each cantaloupe
        for cantaloupe in cantaloupe_coords:
            pygame.draw.circle(screen, (60,179,113), (cantaloupe_coords), cantaloupe_radius +3)
            pygame.draw.circle(screen, (255, 165, 0), (cantaloupe_coords), cantaloupe_radius)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords), cantaloupe_radius-37)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords[0] - 5, cantaloupe_coords[1] - 5), cantaloupe_radius-37)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords[0] + 5, cantaloupe_coords[1] - 5), cantaloupe_radius-37)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords[0] + 5, cantaloupe_coords[1] - 5), cantaloupe_radius-37)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords[0] - 5, cantaloupe_coords[1] + 5), cantaloupe_radius-37)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords[0] - 12, cantaloupe_coords[1] + 1), cantaloupe_radius-37)
            pygame.draw.circle(screen, (255,250,205), (cantaloupe_coords[0] + 12, cantaloupe_coords[1] + 1), cantaloupe_radius-37)

    def draw_orange(orange_coords):
        #loops through each x/y coordinate pair, draws outline and seeds in relation to center of each orange
        for orange in orange_coords:
            pygame.draw.circle(screen, (255, 165, 0), (orange_coords[0], orange_coords[1]), orange_radius)
            pygame.draw.rect(screen,(173,255,47),(orange_coords[0] -2,orange_coords[1]-33,3,15))
            pygame.draw.circle(screen, (173,255,47), (orange_coords[0] + 4, orange_coords[1] - 27), orange_radius-15)

    def draw_kiwi(kiwi_coords):
        #loops through each x/y coordinate pair, draws outline and seeds in relation to center of each kiwi
        for kiwi in kiwi_coords:
            pygame.draw.circle(screen, (205,133,63), (kiwi_coords[0], kiwi_coords[1]), kiwi_radius+2)
            pygame.draw.circle(screen, (173,255,47), (kiwi_coords[0], kiwi_coords[1]), kiwi_radius)
            pygame.draw.circle(screen, (255,255,255), (kiwi_coords[0], kiwi_coords[1]), kiwi_radius-10)
            pygame.draw.circle(screen, (0,0,0),(kiwi_coords[0]-4, kiwi_coords[1]-6), kiwi_radius-18)
            pygame.draw.circle(screen, (0,0,0),(kiwi_coords[0]-8, kiwi_coords[1]-2), kiwi_radius-18)
            pygame.draw.circle(screen, (0,0,0),(kiwi_coords[0]-5, kiwi_coords[1]+4), kiwi_radius-18)
            pygame.draw.circle(screen, (0,0,0),(kiwi_coords[0]+3, kiwi_coords[1]+5), kiwi_radius-18)
            pygame.draw.circle(screen, (0,0,0),(kiwi_coords[0]+7, kiwi_coords[1]+1), kiwi_radius-18)
            pygame.draw.circle(screen, (0,0,0),(kiwi_coords[0]+3, kiwi_coords[1]-6), kiwi_radius-18)
            
    def draw_bomb(bomb_coords):
        #loops through each x/y coordinate pair, draws outline and seeds in relation to center of each watermelon
        for bomb in bomb_coords:
            pygame.draw.circle(screen, (0,0,0), (bomb_coords[0], bomb_coords[1]), bomb_radius)
            pygame.draw.rect(screen,(222,184,135),(bomb_coords[0]-2,bomb_coords[1]-33,3,15))
            pygame.draw.circle(screen, (255,255,0), (bomb_coords[0], bomb_coords[1]-30), bomb_radius-23)
            
    ## Pedram (FUNCTION FOR DRAWING THE HEARTS) ##
   
    def draw_3_hearts():
        pygame.draw.circle(screen, (255, 10, 10), (WIDTH / 1.16, 28), 25)
        pygame.draw.circle(screen, (255, 10, 10), (WIDTH / 1.16 - 60, 28), 25)
        pygame.draw.circle(screen, (255, 10, 10), (WIDTH / 1.16 + 60, 28), 25)

    def draw_2_hearts():
        pygame.draw.circle(screen, (255, 10, 10), (WIDTH / 1.16, 28), 25)
        pygame.draw.circle(screen, (255, 10, 10), (WIDTH / 1.16 + 60, 28), 25)

    def draw_1_heart():
        pygame.draw.circle(screen, (255, 10, 10), (WIDTH / 1.16 + 60, 28), 25)

    #DRAWING game background
    
    screen.fill((91,39,11))

    ## CAILEIGH (DRAWING AND ANIMATION)##

    #DRAW FRUITS: loops through all fruit coordinates, draws staggered off-screen
    for watermelon in watermelon_coords:
        draw_watermelon(watermelon)
    for cantaloupe in cantaloupe_coords:
        draw_cantaloupe(cantaloupe)
    for orange in orange_coords:
        draw_orange(orange)
    for kiwi in kiwi_coords:
        draw_kiwi(kiwi)
    for bomb in bomb_coords:
        draw_bomb(bomb)

    #FALLING FRUITS: For each fruit in list, adds random int to y value for random speeds (range depends on fruit type)
    for x in range(len(cantaloupe_coords)):
        watermelon_coords[x][1] += fruit_speed 
        cantaloupe_coords[x][1] += fruit_speed + 1
        orange_coords[x][1] += fruit_speed + 1 
        kiwi_coords[x][1] += fruit_speed + 1 
        bomb_coords[x][1] +=fruit_speed +1

    #RESPAWN FRUITS: Check if fruit has left the screen, then teleport to a new spawn high above the screen
    for watermelon in watermelon_coords:
        if watermelon[1] >= HEIGHT + .5 * watermelon_radius:
            watermelon[1] -= HEIGHT + 800 #400: amount of pause space between leaving/respawn
    for cantaloupe in cantaloupe_coords:
         if cantaloupe[1] >= HEIGHT + .5 * cantaloupe_radius:
            cantaloupe[1] -= HEIGHT + 800
    for orange in orange_coords:
         if orange[1] >= HEIGHT + .5 * orange_radius:
            orange[1] -= HEIGHT + 800
    for kiwi in kiwi_coords:
         if kiwi[1] >= HEIGHT + .5 * kiwi_radius:
            kiwi[1] -= HEIGHT + 800
    for bomb in bomb_coords:
        if bomb[1] >= HEIGHT + .5 * bomb_radius:
            bomb[1] -= HEIGHT + 700

    ## Pedram (LOSING HEALTH/HEARTS IF A FRUIT IS NOT CLICKED) ##  

    for watermelon in watermelon_coords:
        if watermelon[1] == HEIGHT:
            hearts -= 1
            score = 0
            
    for cantaloupe in cantaloupe_coords:
        if cantaloupe[1] == HEIGHT:
            hearts -= 1
            score = 0
            
    for orange in orange_coords:
        if orange[1] == HEIGHT:
            hearts -= 1
            score = 0
            
    for kiwi in kiwi_coords:
        if kiwi[1] == HEIGHT:
            hearts -= 1
            score = 0
   

    ## Pedram (DRAWING THE HEARTS) ##
    
    if hearts == 3:
        draw_3_hearts() 
    elif hearts == 2:
        draw_2_hearts()
    elif hearts == 1:
        draw_1_heart()

    ## Pedram (HEARTS COUNTER IF THE SCORE IS LOWER THAN ZERO) ##
    
    if score < 0:
        hearts -= 1
        score = 0

    ## Pedram (SCORE DISPLAY/DRAWING) ##
    
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (0, 0))

    ## Pedram (GAME END MESSAGE DISPLAY/DRAWING AND GAME END) ##

    if score <= 0 and hearts <= 0: 
        lose_text = lose_font.render("YOU LOSE!!!", True, (0, 0, 0))
        screen.blit(lose_text, (100, 100))
        pygame.display.update()  # Update the display to show the message before delay
        time.sleep(10) # Delays the code/break for 10 seconds
        break 

    
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
