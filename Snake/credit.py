import pygame
import random

pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the fonts
font_style = pygame.font.SysFont("helvetica", 30, 0, 1)
font_style2 = pygame.font.SysFont("helvetica", 50, 0, 1)

# Define the function to display the score
def display_score(score):
    score_text = font_style.render("Score: " + str(score), 1, "black")
    window.blit(score_text, [0, 0])

# Define function to display game over
def display_game_over():
    game_over_text = font_style2.render("GAME OVER", 1, "black")
    window.blit(game_over_text, (150, 225))
    pygame.display.flip()

# Set up the snake
snake_block_size = 20
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = round((window_width / 2) / snake_block_size) * snake_block_size
snake_y = round((window_height / 2) / snake_block_size) * snake_block_size
snake_x_change = 0
snake_y_change = 0

# Set up the food
food_block_size = 20
food_x = round(random.randrange(0, window_width - food_block_size) / snake_block_size) * snake_block_size
food_y = round(random.randrange(0, window_height - food_block_size) / snake_block_size) * snake_block_size

# Define the function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, "black", [x[0], x[1], snake_block_size, snake_block_size])

# Initialize the menu state
menu_state = "start"

# Define the main menu
def main_menu():
    global menu_state
    menu_font = pygame.font.SysFont("helvetica", 50, 0, 1)
    start_text = menu_font.render("Start", 1, "black")
    credit_text = menu_font.render("Credit", 1, "black")
    exit_text = menu_font.render("Exit", 1, "black")

    while menu_state == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 100 <= mouse[0] <= 100 + 200 and 150 <= mouse[1] <= 150 + 50:
                    menu_state = "game"
                    start_game()
                elif 100 <= mouse[0] <= 100 + 200 and 250 <= mouse[1] <= 250 + 50:
                    menu_state = "credit"
                elif 100 <= mouse[0] <= 100 + 200 and 350 <= mouse[1] <= 350 + 50:
                    pygame.quit()
                    quit()

        window.fill("orange")
        mouse = pygame.mouse.get_pos()
        if 100 <= mouse[0] <= 100 + 200 and 150 <= mouse[1] <= 150 + 50:
            pygame.draw.rect(window, "green", [100, 150, 200, 50])
        else:
            pygame.draw.rect(window, "lightgreen", [100, 150, 200, 50])
        if 100 <= mouse[0] <= 100 + 200 and 250 <= mouse[1] <= 250 + 50:
            pygame.draw.rect(window, "green", [100, 250, 200, 50])
        else:
            pygame.draw.rect(window, "lightgreen", [100, 250, 200, 50])
        if 100 <= mouse[0] <= 100 + 200 and 350 <= mouse[1] <= 350 + 50:
            pygame.draw.rect(window, "green", [100, 350, 200, 50])
        else:
            pygame.draw.rect(window, "lightgreen", [100, 350, 200, 50])

        window.blit(start_text, (100, 150))
        window.blit(credit_text, (100, 250))
        window.blit(exit_text, (100, 350))
        pygame.display.update()

    if menu_state == "credit":
        # Display credit message
        credit_font = pygame.font.SysFont("helvetica", 30, 0, 1)
        credit_text = credit_font.render("All credit goes to Himel Sarder", 1, "black")
        window.fill("orange")
        window.blit(credit_text, (50, 200))
        pygame.display.update()
        while menu_state == "credit":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_state = "start"

# Define the game logic
def start_game():
    global menu_state
    snake_x = round((window_width / 2) / snake_block_size) * snake_block_size
    snake_y = round((window_height / 2) / snake_block_size) * snake_block_size
    snake_x_change = 0
    snake_y_change = 0
    snake_list.clear()
    snake_length = 1

    # Reset the food position
    food_x = round(random.randrange(0, window_width - food_block_size) / snake_block_size) * snake_block_size
    food_y = round(random.randrange(0, window_height - food_block_size) / snake_block_size) * snake_block_size

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Rest of the game logic (snake movement, collision, etc.) goes here

        # Get the user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_x_change != snake_block_size:
            snake_x_change = -snake_block_size
            snake_y_change = 0
        elif keys[pygame.K_RIGHT] and snake_x_change != -snake_block_size:
            snake_x_change = snake_block_size
            snake_y_change = 0
        elif keys[pygame.K_UP] and snake_y_change != snake_block_size:
            snake_y_change = -snake_block_size
            snake_x_change = 0
        elif keys[pygame.K_DOWN] and snake_y_change != -snake_block_size:
            snake_y_change = snake_block_size
            snake_x_change = 0

        # Move the snake
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Check for collision with the food
        if snake_x == food_x and snake_y == food_y:

            # Generate a new position for the food
            food_on_snake = True
            while food_on_snake:
                food_x = round(random.randrange(0, window_width - food_block_size) / snake_block_size) * snake_block_size
                food_y = round(random.randrange(0, window_height - food_block_size) / snake_block_size) * snake_block_size
                food_on_snake = False
                for block in snake_list:
                    if block[0] == food_x and block[1] == food_y:
                        food_on_snake = True
                        break

            snake_length += 1

        # Update the snake list
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with the walls
        if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
            display_game_over()
            pygame.time.delay(1000)
            menu_state = "start"
            return

        # Set the game speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)
        pygame.time.delay(30)

        # Check for collision with the snake's body
        for block in snake_list[:-1]:
            if block == snake_head:
                display_game_over()
                pygame.time.delay(1000)
                menu_state = "start"
                return

        # Draw the game objects
        window.fill("orange")
        pygame.draw.rect(window, "red", [food_x, food_y, food_block_size, food_block_size])
        draw_snake(snake_block_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.flip()

    menu_state = "start"  # Go back to the main menu when the game is over

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu_state == "start":
        main_menu()

pygame.quit()
