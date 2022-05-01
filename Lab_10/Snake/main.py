from configparser import ConfigParser
import psycopg2

from datetime import datetime
import random, sys, time
import pygame
import win32gui, win32con


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Error")
    return db


def execute(command, need_to_commit=False):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if type(command) == str:
            cur.execute(command)
            if need_to_commit: conn.commit()
        else:
            for c in command:
                cur.execute(c)
                if need_to_commit: conn.commit()

        result = cur.fetchall()
    except Exception as e:
        pass
        #print(e)
    else:
        return result
    finally:
        if conn is not None:
            cur.close()
            conn.close()


def create_user(name: str):
    player_data = execute(f"SELECT * FROM users WHERE username='{name}'")
    if not player_data:
        score_id = execute(f"INSERT INTO user_score(max_score, level) VALUES(0, 0) RETURNING score_id", need_to_commit=True)[0][0]
        ret = execute(f"INSERT INTO users(username, is_living, score_id) VALUES('{name}', TRUE, {score_id}) RETURNING *",
                               need_to_commit=True)
        res = {"name" : name, "score_id" : score_id, "level" : 0, 'score' : 0}
        print(f"New player created: {name}")
    else:
        cur_res = execute(f"SELECT level,max_score FROM user_score WHERE score_id = {player_data[0][3]}")[0]
        execute(f"UPDATE users SET is_living = True WHERE username='{name}'")
        res = {"name" : name, "score_id" : player_data[0][3], "level" : cur_res[0], 'score' : cur_res[1]}
        if not player_data[0][2]:
            res["level"] = 0
        print(f"Current level of {name}: {res['level']}, max score: {cur_res[1]}")
    return res


def window_to_active(name:str):
    hwnd = win32gui.FindWindow(None,name)
    print(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
    win32gui.SetForegroundWindow(hwnd)

player1 = input("First player: ")
player1_data = create_user(player1)
player2 = input("Second player: ")
player2_data = create_user(player2)


# Initializing
pygame.init()

# Defining some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Screen set up
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
SCREEN_CENTER = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
WINDOW_NAME = 'Snake'
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_NAME)

# Fonts
FONT = pygame.font.Font(None, 150)
FONT_SMALL = pygame.font.Font(None, 30)


class Snake:
    def __init__(self, x, y, level=0):
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 1
        self.dy = 0
        self.is_add = False
        self.speed = 5 + level
        self.is_living = True
        self.level = level
        self.score = 0

    def draw(self):
        """
        Draw snake
        """
        if not self.is_living: return
        for element in self.elements:
            pygame.draw.circle(screen, RED, element, self.radius)

    def add_score(self, x):
        """
        Increase score of the snake by x 
        """
        self.score += x

    def add_to_snake(self):
        """
        Increase length of the snake
        """
        if not self.is_living: return 
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.level_up()

    def move(self):
        """
        Move snake
        """
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
        """
        Check does snake fit in the screen"""
        x, y, r = *self.elements[0], self.radius
        return not (x - r < 0 or y - r < 0 or x + r > width or y + r > height)

    def level_up(self):
        self.level += 1
        self.speed += 1


class Food:
    SIZE = 5
    COLORS = [RED, GREEN, BLUE]
    LIVING_TIME = 5

    def __init__(self):
        self.gen()

    def gen(self, *snakes):
        """
        Generate new food
        """
        self.time = datetime.now()
        self.weight = random.randint(1, 3)
        self.color = Food.COLORS[self.weight - 1]
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
        """
        Check is food intersect with snake
        """
        for x, y in snake.elements:
            if (abs(x - self.x) < Food.SIZE + snake.radius) and (abs(y - self.y) < Food.SIZE + snake.radius):
                return True
        return False

    def update(self):
        """
        Regenerate food is necessary and draw it
        """
        if (datetime.now() - self.time).seconds >= Food.LIVING_TIME:
            self.gen()
        pygame.draw.rect(screen, self.color, (self.x, self.y, Food.SIZE*2, Food.SIZE*2))

    def get_center(self):
        """
        Return center of the food
        """
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
    saving_data(snake1, player1_data)
    saving_data(snake2, player2_data)
    time.sleep(2)

def saving_data(snake:Snake, player_data:map):
    score = max(player_data['score'], snake.score)
    prev_score_id = player_data['score_id']
    player_data['score_id'] = execute(f"INSERT INTO user_score(max_score, level) VALUES({score}, {snake.level}) RETURNING score_id", need_to_commit=True)[0][0]
    execute(f"UPDATE users SET score_id={player_data['score_id']} WHERE username='{player_data['name']}'", need_to_commit=True)
    execute(f"DELETE FROM user_score WHERE score_id='{prev_score_id}'", need_to_commit=True)
    if not snake.is_living:
        execute(f"UPDATE users SET is_living = False WHERE username='{player_data['name']}'", need_to_commit=True)

def pause(screen:pygame.Surface):
    PAUSE = FONT.render("PAUSE", True, BLACK)
    screen.blit(PAUSE, PAUSE.get_rect(center=SCREEN_CENTER))
    pygame.display.flip()
    saving_data(snake1, player1_data)
    saving_data(snake2, player2_data)
    
# Set up FPS
FPS = 30
clock = pygame.time.Clock()

# Variable to implement pause
is_paused = False

# Game objects
snake1 = Snake(100, 100, player1_data['level'])
snake2 = Snake(150, 100, player2_data['level'])
food = Food()

#window_to_active(WINDOW_NAME)

while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Process movings of snakes
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
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_KP_ENTER:
                is_paused = not is_paused
                if is_paused:
                    pause(screen)

    if not is_paused:
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
            snake1.add_score(food.weight)
            food.gen(snake1, snake2)
        elif food.is_intersect(snake2):
            snake2.is_add = True
            snake2.add_score(food.weight)
            food.gen(snake1, snake2)

        # Drawing frame
        screen.fill(WHITE)
        snake1.draw()
        snake2.draw()
        food.update()

        # Updating frame
        pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
