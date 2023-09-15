import pygame

pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the snake
snake_block_size = 20
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0

# Define the function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(window, "black", [block[0],block[1], snake_block_size, snake_block_size])

# Start the game loop   
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

    # Move the snake
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Update the snake list
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Set the game speed
    clock = pygame.time.Clock()
    clock.tick(snake_speed)
    
    # Draw the game objects
    window.fill("white")
    draw_snake(snake_block_size, snake_list)
    pygame.display.flip()

    # Get the user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x_change = -snake_block_size
        snake_y_change = 0
    elif keys[pygame.K_RIGHT]:
        snake_x_change = snake_block_size
        snake_y_change = 0
    elif keys[pygame.K_UP]:
        snake_y_change = -snake_block_size
        snake_x_change = 0
    elif keys[pygame.K_DOWN]:
        snake_y_change = snake_block_size
        snake_x_change = 0


pygame.quit()