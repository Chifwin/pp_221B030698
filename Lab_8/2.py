from pickle import FALSE
import random, sys, time

import pygame


# Defining some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Screen set up
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
SCREEN_CENTER = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
screen = pygame.display.set_mode(SCREEN_SIZE)

# Fonts
FONT = pygame.font.Font(None, 150)
FONT_SMALL = pygame.font.Font(None, 30)


class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 1
        self.dy = 0
        self.is_add = False
        self.speed = 5
        self.is_living = True
        self.level = 0
        self.score = 0

    def draw(self):
        if not self.is_living: return
        for element in self.elements:
            pygame.draw.circle(screen, RED, element, self.radius)

    def add_to_snake(self):
        if not self.is_living: return 
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.level_up()

    def move(self):
        if not self.is_living: return 
        if self.is_add:
            self.add_to_snake()
            self.is_add = False

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx * self.speed
        self.elements[0][1] += self.dy * self.speed

    def is_fit(self, width, height):
        x, y, r = *self.elements[0], self.radius
        return not (x - r < 0 or y - r < 0 or x + r > width or y + r > height)

    def level_up(self):
        self.level += 1
        self.speed += 1


class Food:
    SIZE = 5

    def __init__(self):
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)

    def gen(self, *snakes):
        while True:
            self.x = random.randint(50, SCREEN_WIDTH - 50)
            self.y = random.randint(50, SCREEN_HEIGHT - 50)
            flag = True
            for snake in snakes:
                if self.is_intersect(snake):
                    flag = False
                    break
            if flag:
                break

    def is_intersect(self, snake):
        for x, y in snake.elements:
            if (abs(x - self.x) < Food.SIZE + snake.radius) and (abs(y - self.y) < Food.SIZE + snake.radius):
                return True
        return False

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, Food.SIZE*2, Food.SIZE*2))
    
    def get_center(self):
        return (self.x + Food.SIZE, self.y + Food.SIZE)

def game_over(screen, scores, levels):
    """
    Function for game over title
    """
    # Game over titles
    GAME_OVER = FONT.render("Game over", True, BLACK)
    scores_label = FONT_SMALL.render(f"Scores: first player {scores[0]}, second player {scores[1]}", True, BLACK)
    levels_label = FONT_SMALL.render(f"Levels: first player {levels[0]}, second player {levels[1]}", True, BLACK)
    screen.fill(RED)
    screen.blit(GAME_OVER, GAME_OVER.get_rect(center = SCREEN_CENTER))
    screen.blit(scores_label, scores_label.get_rect(center = (SCREEN_CENTER[0], SCREEN_CENTER[1]+65)))
    screen.blit(levels_label, levels_label.get_rect(center = (SCREEN_CENTER[0], SCREEN_CENTER[1]+100)))
    pygame.display.flip()
    time.sleep(2)

# Game objects
snake1 = Snake(100, 100)
snake2 = Snake(150, 100)
food = Food()

# Set up FPS
FPS = 30
clock = pygame.time.Clock()

while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if snake1.is_living:
                if event.key == pygame.K_RIGHT and not snake1.dx:
                    snake1.dx = 1
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and not snake1.dx:
                    snake1.dx = -1
                    snake1.dy = 0
                if event.key == pygame.K_UP and not snake1.dy:
                    snake1.dx = 0
                    snake1.dy = -1
                if event.key == pygame.K_DOWN and not snake1.dy:
                    snake1.dx = 0
                    snake1.dy = 1
            if snake2.is_living:
                if event.key == pygame.K_d and not snake2.dx:
                    snake2.dx = 1
                    snake2.dy = 0
                if event.key == pygame.K_a and not snake2.dx:
                    snake2.dx = -1
                    snake2.dy = 0
                if event.key == pygame.K_w and not snake2.dy:
                    snake2.dx = 0
                    snake2.dy = -1
                if event.key == pygame.K_s and not snake2.dy:
                    snake2.dx = 0
                    snake2.dy = 1

    # Snakes' moving
    snake1.move()
    snake2.move()
    
    # Handling event that snake leaved game arena
    if not snake1.is_fit(*SCREEN_SIZE): snake1.is_living = False
    if not snake2.is_fit(*SCREEN_SIZE): snake2.is_living = False

    # Game over if all snakes are dead
    if not snake1.is_living and not snake2.is_living:
        game_over(screen, (snake1.score, snake2. score), (snake1.level, snake2.level))
        break

    # Handling event that one of snakes eated food
    if food.is_intersect(snake1):
        snake1.is_add = True
        food.gen(snake1, snake2)
    if food.is_intersect(snake2):
        snake2.is_add = True
        food.gen(snake1, snake2)

    # Drawing frame
    screen.fill(WHITE)
    snake1.draw()
    snake2.draw()
    food.draw()

    # Updating frame
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()