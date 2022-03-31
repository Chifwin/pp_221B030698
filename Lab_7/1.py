import pygame
from datetime import datetime


def blit_rotate(screen, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    #print(rotated_image.get_rect())
    new_rect = rotated_image.get_rect(center = image.get_rect(bottomright = topleft).center)
    #new_rect = rotated_image.get_rect(center = image.get_rect(bottomright = bottomright).center)
    #print(new_rect)
    screen.blit(rotated_image, new_rect)

pygame.init()
screen_size = width, height = (500, 500)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
done = False

mickey_body = pygame.transform.scale(
    pygame.image.load('Lab_7\\images\\Mickey_body.png'), screen_size)
mickey_left_hand = pygame.transform.rotate(
    pygame.image.load('Lab_7\\images\\Mickey_left_hand.png'), 60)
mickey_right_hand = pygame.transform.rotate(
    pygame.image.load('Lab_7\\images\\Mickey_right_hand.png'), -45)

start = datetime.now()
mickey_left_hand = pygame.transform.rotate(mickey_left_hand, start.minute*6)
mickey_right_hand = pygame.transform.rotate(mickey_right_hand, start.second*6)

print(mickey_left_hand.get_rect())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(mickey_body, (0, 0))

    blit_rotate(screen, mickey_right_hand, (0, 0), datetime.now().second*6)
    pygame.display.flip()
    clock.tick(60)