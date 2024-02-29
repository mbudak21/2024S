import pygame
import random
import sys

def initialize_pygame(L):
    """Initializes Pygame and returns the screen and clock."""
    pygame.init()
    screen = pygame.display.set_mode((L, L))
    pygame.display.set_caption('Random Points in a Square')
    return screen, pygame.time.Clock()

def generate_points(L, num_points=100):
    """Generates a list of random (x, y) points within the square."""
    return [(random.randint(0, L-1), random.randint(0, L-1)) for _ in range(num_points)]

def draw_points(screen, points, point_color):
    """Draws points on the screen."""
    for x, y in points:
        pygame.draw.circle(screen, point_color, (x, y), 2)

def main():
    # Configuration
    L = 500  # Square side length
    background_color = (255, 255, 255)  # White
    point_color = (0, 0, 0)  # Black
    num_points = 100  # Number of points to generate
    coll_radius = 5  # Collision radius

    # Initialize Pygame
    screen, clock = initialize_pygame(L)

    # Generate points
    points = generate_points(L, num_points)

    # Sort points by x
    x_sorted = sorted(points, key=lambda point: point[0])

    # Sort points by y
    y_sorted = sorted(points, key=lambda point: point[1])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        screen.fill(background_color)

        # Draw points
        draw_points(screen, points, point_color)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
