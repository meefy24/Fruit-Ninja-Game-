"""
Hi, Mr. Gallo!
Our group work process wasn't very seperate, most of our contributions were bouncing ideas off each other and editing each other's code. Because of this, almost every section of our code is a collection of each member's ideas and executions. Since neither of us can take credit for the entire game...the following sections of code were mostly concieved or contributed to by me!
"""

#Coordinate lists: the following lists store 3 sublists for the various x/y values of each fruit/obj spawns. The y values are negative and staggered at different heights off-screen to space out the spawn times for each fruit.
watermelon_coords = [[140, 0], [220, -400], [450, -1500]]
cantaloupe_coords = [[320, -300], [570, -900], [80, -1800]]
orange_coords = [[620, -2000], [100, -4000], [400, -7000]]
kiwi_coords = [[270, -3000], [300, -6000], [500, -8000]]
bomb_coords = [[100, 0], [220, -900], [400, -1200]]

 #DRAW FRUITS: loops through all fruit coordinates, draws each at designated place off-screen
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

    #FALLING FRUITS: For each fruit/obj in list, isolates y value and adds varying values for different speeds falling downwards
    for x in range(len(cantaloupe_coords)):
        watermelon_coords[x][1] += fruit_speed 
        cantaloupe_coords[x][1] += fruit_speed + 1
        orange_coords[x][1] += fruit_speed + 1 
        kiwi_coords[x][1] += fruit_speed + 1 
        bomb_coords[x][1] +=fruit_speed +1

    #RESPAWN FRUITS: Check if each obj's y value has exceeded screen height, then teleports to a new spawn high above the screen
    for watermelon in watermelon_coords:
        if watermelon[1] >= HEIGHT + .5 * watermelon_radius:
            watermelon[1] -= HEIGHT + 800 #amount of pause space between leaving/respawn
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
