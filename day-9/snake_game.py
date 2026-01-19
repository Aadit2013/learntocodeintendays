import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Game settings
width = 600
height = 400
snake_block = 10
snake_speed = 15

# Create the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsansms', 35)

# Function to display the score
def your_score(score):
    value = score_font.render('Score: ' + str(score), True, black)
    screen.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Function for the game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = int(width / 2)
    y1 = int(height / 2)

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = int(round(random.randrange(0, width - snake_block) / 10.0) * 10.0)
    foody = int(round(random.randrange(0, height - snake_block) / 10.0) * 10.0)

    while not game_over:
        while game_close:
            screen.fill(white)
            message = font_style.render('You Lost! Press C-Play Again or Q-Quit', True, red)
            screen.blit(message, [width / 6, height / 3])
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        # Reset the game
                        x1 = int(width / 2)
                        y1 = int(height / 2)
                        x1_change = 0
                        y1_change = 0
                        snake_List = []
                        Length_of_snake = 1
                        foodx = int(round(random.randrange(0, width - snake_block) / 10.0) * 10.0)
                        foody = int(round(random.randrange(0, height - snake_block) / 10.0) * 10.0)
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, black, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randrange(0, width - snake_block) / 10.0) * 10.0)
            foody = int(round(random.randrange(0, height - snake_block) / 10.0) * 10.0)
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
if __name__ == '__main__':
    gameLoop()