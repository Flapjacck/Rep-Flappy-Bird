#Spencer Kelly
#Mrs. Mattina
#ICS3U1
#2021-11-1

#importing moduels - day 1 
import pygame
import random

# Initialising the modules in pygame - day 1
pygame.init()

#setting up a frame limit - day 3
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((500, 750))  # Setting the display - day 1

# background - day 1
BACKGROUND_IMAGE = pygame.image.load('background.jpg')

#  BIRD - day 1
BIRD_IMAGE = pygame.image.load('bird1.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

# OBSTACLES - day 2
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)
OBSTACE_X_CHANGE = -4
obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_y = height + 150
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(obstacle_x, bottom_y, OBSTACLE_WIDTH, bottom_height))

# COLLISION DETECTION - day 3
def collision_detection (obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False

# SCORE - day 4
score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    SCREEN.blit(display, (10, 10))

#loading in sound effects - day 4 and 5
flap_sound = pygame.mixer.Sound('Flap.wav')
death_sound = pygame.mixer.Sound('Death.wav')
point_sound = pygame.mixer.Sound("Score.mp3")

# START SCREEN - day 4 and 5
startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    # displays: "press space bar to start)
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(display, (20, 200))
    pygame.display.update()

# GAME OVER SCREEN - day 5
# This list will hold all of the scores
score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():
    # check for the maximum score
    maximum = max(score_list)
    #  "game over"
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(display1, (50, 300))
    # shows your current score and your max score
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
    #  If your new score is the same as the maximum then u reached a new high score
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (255, 255, 0))
        SCREEN.blit(display3, (80, 100))

    pygame.display.update()

#running for the while loop - day 1
running = True
# waiting is going to refer to our end or start screen - day 4
waiting = True
# set collision to false in the beginning so that we only see the start screen in the beginning - day 4
collision = False

#while loop to run the game - day 1
while running:

    #filling screen - day 1
    SCREEN.fill((0, 0, 0))

    #setting max fps to 60 to make the game smooth - day 3
    clock.tick(60)

    # display the background image - day 1
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    # we will be sent into this while loop at the beginning and ending of each game - day 4 and 5
    while waiting:
        if collision:
            # If collision is True (from the second time onwards) we will see both the end screen and the start screen - day 5
            game_over()
            start()
        else:
            # This refers to the first time the player is starting the game - day 5
            start()

        #starting the game if space is pressed - day 5
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #  If we press the space bar we will exit out of the waiting while loop and start to play the game
                    # we will also reset some of the variables such as the score and the bird's Y position and the obstacle's starting position
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                    #  to exit out of the while loop
                    waiting = False

            if event.type == pygame.QUIT:
                # in case we exit out make both running and waiting false
                waiting = False
                running = False

    #using events for ingame actions and quitting - day 1
    for event in pygame.event.get():
        #quitting the game - day 1
        if event.type == pygame.QUIT:
            # If you press exit you exit out of the while loop and pygame quits
            running = False

        #if statements for key presses - day 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #  if you press spacebar you will move up
                bird_y_change = -6
                flap_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # when u release space bar you will move down automatically
                bird_y_change = 3

    # moving the bird vertically - day 1 
    bird_y += bird_y_change
    # setting boundaries for the birds movement - day 2
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571

    # Moving the obstacle - day 2
    obstacle_x += OBSTACE_X_CHANGE

    #making the game progressivly harder - day 4
    if score == 10:
        OBSTACE_X_CHANGE += -0.03
    if score == 20:
        OBSTACE_X_CHANGE += -0.02
    if score == 30:
        OBSTACE_X_CHANGE += -0.01
    if score == 40:
        OBSTACE_X_CHANGE += -0.005

    # COLLISION - day 3
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 150)

    #restarting the game if there is a collision - day 4
    if collision:
        # if a collision does occur we are gonna add that score to our list of scores and make waiting True
        score_list.append(score)
        waiting = True
        OBSTACE_X_CHANGE = -4
        death_sound.play()

    # generating new obstacles - day 2
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1
        point_sound.play()

    # displaying the obstacle - day 2
    display_obstacle(OBSTACLE_HEIGHT)

    # displaying the bird - day 2
    display_bird(bird_x, bird_y)

    # display the score - day 3
    score_display(score)

    # Update the display after each iteration of the while loop - day 1
    pygame.display.update()

# Quit the program - day 1
pygame.quit()