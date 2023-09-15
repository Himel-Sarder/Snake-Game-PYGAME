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
        pygame.draw.rect(window, "black", [block[0], block[1], snake_block_size, snake_block_size])

# Start the game loop   
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

    # Update the snake list
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    # Set the game speed
    clock = pygame.time.Clock()
    clock.tick(snake_speed)
    
    # Draw the game objects
    window.fill("white")
    draw_snake(snake_block_size, snake_list)
    pygame.display.flip()

pygame.quit()