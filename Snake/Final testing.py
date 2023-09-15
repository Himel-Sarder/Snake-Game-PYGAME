import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the fonts
font_style = pygame.font.SysFont("bazooka", 30, 0, 1)
font_style2 = pygame.font.SysFont("ebrima", 50, 0, 1)

# Define the function to display the score
def display_score(score):
    score_text = font_style.render("Score: " + str(score), 1, "white")
    window.blit(score_text, [0, 0])

# Define function to display game over
def display_game_over():
    game_over_text = font_style2.render("GAME OVER", 5, "white")
    window.blit(game_over_text, (100, 225))
    pygame.display.flip()

# Set up the snake
snake_block_size = 20
snake_speed = 10
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

# Load the eat sound
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("Snake/Metarials/Eating.mp3")  # Replace with your sound file

# Load the game over sound
game_over_sound = pygame.mixer.Sound("Snake/Metarials/GameOver.wav")  # Replace with your game over sound file

# Load the background music
pygame.mixer.music.load('Snake/Metarials/music_music.mp3')  # Replace with your music file
pygame.mixer.music.play(-1)  # Play the background music

# Define the function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(window, "black", [segment[0], segment[1], snake_block_size, snake_block_size])
# Initialize the menu state
menu_state = "start"

# Load the background image
background_image = pygame.image.load("Snake/Metarials/background.png")

# Load the menu image
menu_image = pygame.image.load("Snake/Metarials/menu_image.png")

# Load the credit image
#credit_image = pygame.image.load("Snake/Metarials/nice.png")

# Define the main menu
def main_menu():
    global menu_state

    menu_font = pygame.font.SysFont("Courier New", 70, 1, 1)
    menu_font2 = pygame.font.SysFont("Times New Roman", 35, 1, 1)
    title_text = menu_font.render("Noob Snake", 1, "black")
    start_text = menu_font2.render("Start", 1, "black")
    credit_text = menu_font2.render("Credit", 1, "black")
    exit_text = menu_font2.render("Exit", 1, "black")

    while menu_state == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if window_width / 2 - 100 <= mouse[0] <= window_width / 2 + 100 and 200 <= mouse[1] <= 200 + 50:
                    pygame.mixer.music.stop()  # Stop the background music when the game starts
                    menu_state = "game"
                    start_game()
                elif window_width / 2 - 100 <= mouse[0] <= window_width / 2 + 100 and 300 <= mouse[1] <= 300 + 50:
                    menu_state = "credit"
                elif window_width / 2 - 100 <= mouse[0] <= window_width / 2 + 100 and 400 <= mouse[1] <= 400 + 50:
                    pygame.quit()
                    quit()

        window.fill("coral")
        mouse = pygame.mouse.get_pos()
        
        # Display the menu image
        window.blit(menu_image, (0, 0))

        # Display Title
        title_width = title_text.get_width()
        window.blit(title_text, (window_width / 2 - title_width / 2, 50))

        # Centered Buttons
        button_width = 200
        button_height = 50

        start_x = window_width / 2 - button_width / 2
        start_y = 200
        credit_x = window_width / 2 - button_width / 2
        credit_y = 300
        exit_x = window_width / 2 - button_width / 2
        exit_y = 400

        # Stylish Start Button
        if start_x <= mouse[0] <= start_x + button_width and start_y <= mouse[1] <= start_y + button_height:
            pygame.draw.rect(window, "green", [start_x, start_y, button_width, button_height])
        else:
            pygame.draw.rect(window, "lightgreen", [start_x, start_y, button_width, button_height])
        
        # Stylish Credit Button
        if credit_x <= mouse[0] <= credit_x + button_width and credit_y <= mouse[1] <= credit_y + button_height:
            pygame.draw.rect(window, "blue", [credit_x, credit_y, button_width, button_height])
        else:
            pygame.draw.rect(window, "lightblue", [credit_x, credit_y, button_width, button_height])
        
        # Stylish Exit Button
        if exit_x <= mouse[0] <= exit_x + button_width and exit_y <= mouse[1] <= exit_y + button_height:
            pygame.draw.rect(window, "red", [exit_x, exit_y, button_width, button_height])
        else:
            pygame.draw.rect(window, "pink", [exit_x, exit_y, button_width, button_height])

        # Stylish Button Text
        window.blit(start_text, (start_x + 60, start_y + 5))
        window.blit(credit_text, (credit_x + 50, credit_y + 5))
        window.blit(exit_text, (exit_x + 60, exit_y + 5))
        
        pygame.display.update()

    if menu_state == "credit":
        # Display credit message and back button
        credit_font = pygame.font.SysFont("pixer", 30, 0, 1)
        credit_text1 = credit_font.render("Game Credit:", 1, "black")
        credit_text2 = credit_font.render("**Game Title: **Noob Snake", 1, "black")
        credit_text3 = credit_font.render("**Developer: **Himel Sarder", 1, "black")
        credit_text4 = credit_font.render("**Production:** BK Production", 1, "black")
        credit_text5 = credit_font.render("Thank you for playing Noob Snake!", 1, "black")
        back_text = credit_font.render("Back To Main Menu", 1, "black")

        window.fill("pink")
        # Display the credit image
        #window.blit(credit_image, (0, 0))

        window.blit(credit_text1, (40, 200))
        window.blit(credit_text2, (40, 235))
        window.blit(credit_text3, (40, 260))
        window.blit(credit_text4, (40, 285))
        window.blit(credit_text5, (40, 320))

        # Stylish Back Button
        pygame.draw.rect(window, "lightgreen", [100, 400, 200, 50])
        pygame.draw.rect(window, "green", [100, 400, 200, 50])
        
        # Stylish Button Text
        window.blit(back_text, (100, 410))
        pygame.display.update()
        
        while menu_state == "credit":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 100 <= mouse[0] <= 100 + 200 and 400 <= mouse[1] <= 400 + 50:
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
            eat_sound.play()  # Play the eat sound

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
            game_over_sound.play()  # Play the game over sound
            pygame.time.delay(1000)
            menu_state = "start"
            pygame.mixer.music.play(-1)  # Play the background music again
            return

        # Set the game speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)
        pygame.time.delay(30)

        # Check for collision with the snake's body
        for block in snake_list[:-1]:
            if block == snake_head:
                display_game_over()
                game_over_sound.play()  # Play the game over sound
                pygame.time.delay(1000)
                menu_state = "start"
                pygame.mixer.music.play(-1)  # Play the background music again
                return

        # Draw the game objects
        window.blit(background_image, (0, 0))
        pygame.draw.circle(window, "red", (food_x + food_block_size // 2, food_y + food_block_size // 2), food_block_size // 2)
        draw_snake(snake_block_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.flip()

    menu_state = "start"  # Go back to the main menu when the game is over

# Play the background music before the main menu loop
pygame.mixer.music.play(-1)

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu_state == "start":
        main_menu()

pygame.quit()
