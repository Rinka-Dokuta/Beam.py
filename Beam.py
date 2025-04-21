import pygame
import math

# Constants
FPS = 60
SCREEN_W = 800
SCREEN_H = 800

# Keys
KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3
KEY_SPACE = 4

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Sinusoidal Shooter")
clock = pygame.time.Clock()

# Load image
pic = pygame.image.load("spaceship.png").convert_alpha()

# Position of player
xPos = 50
yPos = 400
angle = 0

#Beam 1
BeamX = xPos
BeamY = yPos

isShooting = False

#Beam 2
Beam2X = xPos
Beam2Y = yPos


isShooting = False

# Game state
key = [False, False, False, False, False]
running = True

while running: #GAME LOOP##################################################
    
    #input section-----------------------------------
    clock.tick(FPS)
    
    #event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyboard input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key[KEY_UP] = True
            elif event.key == pygame.K_DOWN:
                key[KEY_DOWN] = True
            elif event.key == pygame.K_LEFT:
                key[KEY_LEFT] = True
            elif event.key == pygame.K_RIGHT:
                key[KEY_RIGHT] = True
            elif event.key == pygame.K_SPACE:
                key[KEY_SPACE] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key[KEY_UP] = False
            elif event.key == pygame.K_DOWN:
                key[KEY_DOWN] = False
            elif event.key == pygame.K_LEFT:
                key[KEY_LEFT] = False
            elif event.key == pygame.K_RIGHT:
                key[KEY_RIGHT] = False
            elif event.key == pygame.K_SPACE:
                key[KEY_SPACE] = False
            elif event.key == pygame.K_ESCAPE:
                running = False

    #physics section---------------------------------------
    
    angle += 0.1
    if BeamX > SCREEN_W:
        BeamX = xPos
        angle = 0

    angle += 0.2
    if Beam2X > SCREEN_W:
        Beam2X = xPos
        angle = 0

    if not isShooting:
        if key[KEY_UP]:
            yPos -= 4
        if key[KEY_DOWN]:
            yPos += 4
        if key[KEY_LEFT]:
            xPos -= 4
        if key[KEY_RIGHT]:
            xPos += 4

    if key[KEY_SPACE]:
        #HERES THE MOST IMPORTANT PART!--------------
        A = 20
        B = 10 
        C = 0
        D = yPos
        
        BeamX += 5 #handles how fast the beam moves to the right
        BeamY = A* math.sin(B*(angle-C)) + D #handles the shape of the beam

        
        A2 = 70
        B2 = 5
        C2 = 0
        D2 = yPos


        Beam2X += 5 #handles how fast the beam moves to the right
        Beam2Y = A2* math.sin(B2*(angle-C2)) + D2 #handles the shape of the beam

        #------------------------------------------
        isShooting = True
    else:
        isShooting = False
        BeamX = xPos + 25
        Beam2X = xPos + 25
        angle = 0
       

    # Render Section-----------------------------------------------------------------------
    #screen.fill((255, 255, 255)) #commented out so we see the path of the beam
    
    if not isShooting:
        screen.fill((255, 255, 255))  # Clear screen

    if isShooting:
        pygame.draw.circle(screen, (250, 0, 0), (int(BeamX), int(BeamY)), 5) #draw beam
        pygame.draw.circle(screen, (250, 120, 20), (int(Beam2X), int(Beam2Y)), 5)
    screen.blit(pic, (xPos, yPos)) #draw spaceship
    
    pygame.display.flip()

    
#end game loop#########################
pygame.quit()
