# If your asking what I am doing, just an experiment
# A walking simulator
# But fullscreen :D

#Crash handling section
def crashfile(Reasonfile):
    try:
        import os
    except Exception:
        crashcon(f"\n An error occoured: {Reasonfile} \n ")
    with open("log/error.txt", "a") as my_file:
        my_file.write(f"An error occoured: {Reasonfile}")
    print(f"2")
    crashexit2 = input(f"\n Press enter to quit")
    try:
        pygame.quit()
    except Exception:
        pass
    exit()
        
def crashcon(Reason):
    print(f"\n A crittical Error occored!\n The reason: {Reason}")
    crashexit1 = input(f"\n Press enter to quit")
    try:
        pygame.quit()
    except Exception:
        pass
    exit()



# Setting up the window and player position
try:
    import os
    import sys
    import pygame
    import pygame.mixer as mixer 
except Exception:
    crashcon("Failing to import librarys. Check python interpretor.")
    crashfile(f"Failing to import librarys. Check python interpretor. Check log\\error.txt")


pygame.init()
mixer.init()
mixer.music.load("resources/audios/mainms.wav")
WHITE = (255, 255, 255)
width = 800
height = 600
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("The New Era")
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
print(f"{screen_width} {screen_height}")

playerx = screen_width // 2
playery = screen_height // 2
print(playerx, playery)


# Setting up the textures and the moving conditions
try:
    playertexture = pygame.image.load("resources/sprites/character/Sprite-0001.png")
    playertexture = pygame.transform.scale(playertexture, (128, 128)) 
    background = pygame.image.load("resources/sprites/background/Sprite-bg1.png")
    background = pygame.transform.scale(background,(screen_width, screen_height)) 
except Exception:
    crashcon("Failing to load sprites and/or audios")
    crashfile("Failing to load sprites and/or audios")

moving_right = False  
moving_left = False
moving_up = False
moving_down = False
# clock.
clock = pygame.time.Clock()

# title screen
# remove this part when you get errors thrown there
# but it still shouldn't happen
basicsetup = True
while basicsetup:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                basicsetup = False

    try:
        title1bg = pygame.image.load("resources/sprites/background/Sprite-title1.png")
        title1bg = pygame.transform.scale(title1bg,(screen_width, screen_height)) 
    except Exception:
        basicsetup = False
    screen.blit(title1bg, (0,0)) 
    pygame.display.flip()
    clock.tick(120) 

instruc = True
while instruc:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                instruc = False
    try:
        title2bg = pygame.image.load("resources/sprites/background/Sprite-title2.png")
        title2bg = pygame.transform.scale(title2bg,(screen_width, screen_height)) 
    except Exception:
        basicsetup = False
    screen.blit(title2bg, (0,0)) 
    pygame.display.flip()
    clock.tick(120) 

running = True
musicsetup = True
while running:
    if musicsetup != False:
        mixer.music.play(-1)
        musicsetup = False
    # Checking for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Condition Loop 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_a:
                moving_left = True    
            elif event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_a:
                moving_left = False 
            elif event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False
    # Movement
    if moving_right:
        playerx += 10  
    if moving_left:
        playerx -= 10
    if moving_up:
        playery -= 10
    if moving_down:
        playery += 10

    # Blitting
    screen.blit(background, (0,0)) 
    screen.blit(playertexture, (playerx, playery))

    #Refreshing
    pygame.display.flip()
    clock.tick(120) 
    
pygame.quit()
sys.exit()