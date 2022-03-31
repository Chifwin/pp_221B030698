import pygame


pygame.init()
screen_size = width, height = (500, 500)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
done = False

coords = [250, 250]
radius = 25

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            coords[1] -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            coords[1] += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            coords[0] -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            coords[0] += 20
    
    coords[1] = max(radius, min(coords[1], height - radius))
    coords[0] = max(radius, min(coords[0], width - radius))
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), coords, radius)
    pygame.display.flip()
    clock.tick(60)
