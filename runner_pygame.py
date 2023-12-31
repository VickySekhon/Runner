#import pygame library
import pygame

#Initialize pygame
pygame.init()

#Set variable for while loop (the game is active until a condition is not met)
game_active = True

#Screen elements
pygame.display.set_caption("Runner")
(length, width) = (800,400)
screen = pygame.display.set_mode((length,width))
fps = pygame.time.Clock()

#Text font
title_font = pygame.font.Font("Export/Pixeltype.ttf", 50)

#Music
music = pygame.mixer.Sound("Export/music.wav")
jump_music = pygame.mixer.Sound("Export/audio_jump.mp3")

#Visual background elements
sky = pygame.image.load("Export/Sky.png").convert()
ground = pygame.image.load("Export/ground.png").convert()
title = title_font.render("Runner",False,(64,64,64))
title_rect = title.get_rect(center = (400, 50))
credits = title_font.render("By: Vicky Sekhon",False,"Black")

#Obstacle elements
snail = pygame.image.load("Export/snail1.png").convert_alpha()
snail_rect = snail.get_rect(bottomright = (600,300))
fly = pygame.image.load("Export/Fly1.png").convert_alpha()
fly_rect = fly.get_rect(topleft = (300,170))

#Player element
player = pygame.image.load("Export/player_walk_1.png").convert_alpha()
player_rect = player.get_rect(midbottom = (100,300))

#Game dynamics
gravity = 0

#While loop (keep running until...)
loop = True
while loop:
    #Find if the user quits the game and if so then break the loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            loop = False
        
        #If we make our player jump and the player tries to escape the screen then put him back on ground level (same goes for jumping)
        if game_active:     
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    gravity = -20
                    jump_music.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    gravity = -20      
                    jump_music.play()
            
        #Once the game fails (loop breaks) if a key is pressed or the mouse then start the game back up with the initial positions of the characters below
        else:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                snail_rect.left = 800 
                fly_rect.left = 500
    
    #Background music 
    music.play(loops=5)
    music.set_volume(0.5)
    jump_music.set_volume(1.5)
    
    #While the game is active display the following elements to the screen
    if game_active:
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,300))
        screen.blit(snail,snail_rect)
        screen.blit(player,player_rect)
        screen.blit(fly,fly_rect)
       
        #Game dynamics 
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        
        #Visual elements 
        pygame.draw.rect(screen, "#c0e8ec", title_rect)
        pygame.draw.rect(screen, "#c0e8ec", title_rect, 10)
        screen.blit(title,title_rect)
        screen.blit(credits,(0,0))
        
        #Obstacle speed and display on-screen after an object leaves the screen
        fly_rect.x -= 5
        if fly_rect.right <= 0:
            fly_rect.left = 800
        snail_rect.x -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        
        #Game conditions (stop the game if...)
        if snail_rect.colliderect(player_rect) or fly_rect.colliderect(player_rect):
            game_active = False
    
    #If the game is not active (loop is broken) then fill the screen with a black (blank screen) and stop the music
    else:
        screen.fill("Black")
        music.stop()
    
    #"Print" everything above this to the screen
    pygame.display.flip()
    #^With this fps^
    fps.tick(60)