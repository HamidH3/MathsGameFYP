# import pygame
# import sys

# # Initialize pygame
# pygame.init()

# # Set the dimensions of the window
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# # Set the title of the window
# pygame.display.set_caption('Simple Pygame with Pygbag')

# # Define the color red
# red = (255, 0, 0)

# # Initial position of the rectangle
# rect_x = screen_width // 2
# rect_y = screen_height // 2
# rect_width = 50
# rect_height = 50
# speed = 5

# # Main game loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Get the keys pressed
#     keys = pygame.key.get_pressed()

#     # Move the rectangle based on arrow keys
#     if keys[pygame.K_LEFT]:
#         rect_x -= speed
#     if keys[pygame.K_RIGHT]:
#         rect_x += speed
#     if keys[pygame.K_UP]:
#         rect_y -= speed
#     if keys[pygame.K_DOWN]:
#         rect_y += speed

#     # Fill the screen with a blue color
#     screen.fill((0, 0, 255))

#     # Draw the red rectangle
#     pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

#     # Update the display
#     pygame.display.update()


import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Simple Pygame with Pygbag')

# Define colors
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Rectangle properties
rect_x = screen_width // 2
rect_y = screen_height // 2
rect_width = 50
rect_height = 50
speed = 5

# Circle properties
circle_radius = 20
circle_x = random.randint(circle_radius, screen_width - circle_radius)
circle_y = random.randint(circle_radius, screen_height - circle_radius)

# Global score variable
score = 0

def check_collision():
    """Checks if the rectangle touches the circle and updates score."""
    global score, circle_x, circle_y
    
    # Check collision (AABB method)
    if (
        rect_x < circle_x + circle_radius and
        rect_x + rect_width > circle_x - circle_radius and
        rect_y < circle_y + circle_radius and
        rect_y + rect_height > circle_y - circle_radius
    ):
        score += 1  # Increase score
        print(f"Score: {score}")  # Debugging (remove if needed)
        
        # Move the circle to a new random position
        circle_x = random.randint(circle_radius, screen_width - circle_radius)
        circle_y = random.randint(circle_radius, screen_height - circle_radius)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the rectangle based on arrow keys
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Check for collision with the circle
    check_collision()

    # Fill the screen with blue
    screen.fill(blue)

    # Draw the red rectangle
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

    # Draw the green circle
    pygame.draw.circle(screen, green, (circle_x, circle_y), circle_radius)

    # Update the display
    pygame.display.update()
