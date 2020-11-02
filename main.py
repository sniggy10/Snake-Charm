import pygame
import time
import random

pygame.init()

#creating game screen
dis_width = 800
dis_height  = 600
display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('BEWARE  OF  SNAKES !!')
background_img = pygame.image.load('images/background.jpg')
background_img = pygame.transform.scale(background_img, (dis_width,dis_height+20))

snake_color = (25,255,110)
food_color = (255,167,0)
score_color = (224,255,255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)

score_font = pygame.font.SysFont(None, 40)
instruction_font = pygame.font.SysFont(None, 40)
msg_font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()

def draw_snake(snake_list, snake_block):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_block, snake_block])

def display_score(score):
    score_msg = score_font.render("Your Score: " + str(score), True, score_color)
    display.blit(score_msg, [10, 10])

def display_lose_message(color):
    message = msg_font.render("You Lost !!", True, color)
    instruction = instruction_font.render("Press Q to quit or C to continue.",True,(0,0,255))
    display.blit(message, [dis_width/3, dis_height/3])
    display.blit(instruction,[dis_width/5,dis_height/2])

def gameLoop():  
    
    game_over = False
    game_close = False

    snake_block = 10
    snake_speed = 10
    snake_length = 1
    snake_list = []

    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0       
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(black)
            display_lose_message(red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
    
        x1 += x1_change
        y1 += y1_change
        
        display.fill(black) 
        display.blit(background_img,(0,0))

        pygame.draw.rect(display,food_color,[foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        draw_snake(snake_list,snake_block)

        display_score(snake_length-1)

        pygame.display.update()  

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()