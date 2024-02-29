import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Square side length L
L = 500

# Screen dimensions
screen_width = L
screen_height = L

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Random Points in a Square')

# Color definitions
background_color = (255, 255, 255)  # White
point_color = (0, 0, 0)  # Black

# Main loop flag
running = True

# Frame rate control
clock = pygame.time.Clock()

def draw():
    for i in range(len(pairs)):
        pygame.draw.circle(screen, point_color, (pairs[i][0], pairs[i][1]), 2)

# Generate 100 points
pairs = []
for _ in range(100):
    x = random.randint(0, L-1)
    y = random.randint(0, L-1)
    pairs.append( (x, y) )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
