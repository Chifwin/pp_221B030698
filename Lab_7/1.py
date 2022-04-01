from matplotlib import scale
import pygame
from datetime import datetime


def rotate(screen, surface, angle, bias, radii):
    """Rotate the surface around center of image displaysed by radii vector

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        bias (tuple, list, pygame.math.Vector2): Displaysement
        radii (pygame.math.Vector2): Vector to pivot point from center of image
    """
    rotated_image = pygame.transform.rotate(surface, -angle)  # Rotate the image.
    rotated_radii = radii.rotate(angle)  # Rotate the radii vector.
    # Add the radii vector to the bias point to shift the rect.
    rect = rotated_image.get_rect(center=bias+rotated_radii)
    screen.blit(rotated_image, rect)


pygame.init()
screen_size = width, height = (500, 500)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
done = False

mickey_body = pygame.image.load('Lab_7\\images\\Mickey_body.png')
mickey_left_hand = pygame.image.load('Lab_7\\images\\Mickey_left_hand.png')
mickey_right_hand = pygame.image.load('Lab_7\\images\\Mickey_right_hand.png')

start = datetime.now()

MICKEY_LEFT_HAND_OFFSET = pygame.math.Vector2(0, -73)
MICKEY_RIGHT_HAND_OFFSET = pygame.math.Vector2(0, -65)
BIAS = (250, 250)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(mickey_body, (0, 0))

    rotate(screen, mickey_right_hand, datetime.now().second*6, BIAS, MICKEY_RIGHT_HAND_OFFSET)
    rotate(screen, mickey_left_hand, datetime.now().minute*6, BIAS, MICKEY_LEFT_HAND_OFFSET)
    pygame.display.set_caption(f'Minutes: {datetime.now().minute}, seconds: {datetime.now().second}')
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
