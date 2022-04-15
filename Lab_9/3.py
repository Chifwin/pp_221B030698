import math
import sys
from turtle import heading, width
import pygame
from random import shuffle

class Figure:
    def __init__(self, color, coords) -> None:
        self.coords = coords
        self.color = color

    def draw(self):
        pass

    def get_color(self, index):
        new_color = list(self.color)
        for i in range(3):
            new_color[i] = math.ceil(self.color[i] * (index/256))
        return new_color

class Circle(Figure):
    def __init__(self, color, coords, radius=0) -> None:
        super().__init__(color, coords)
        if radius:
            self.center = self.coords
            self.radius = radius
        else:
            self.center = coords[0]
            self.radius = ((self.center[0] - self.coords[1][0])**2 + (self.center[1] - self.coords[1][1])**2)**0.5 if not radius else radius
    
    def draw(self, screen, ind: int):
        pygame.draw.circle(screen, self.get_color(ind), self.center, self.radius)
        
class Rectange(Figure):
    def __init__(self, color, coords) -> None:
        super().__init__(color, coords)
        x, y = self.coords[1]
        xx, yy = self.coords[0]
        self.coords = [0, 0, 0, 0]
        self.coords[0], x = min(xx, x), max(xx, x)
        self.coords[1], y = min(yy, y), max(yy, y)
        self.coords[2] = x - self.coords[0]
        self.coords[3] = y - self.coords[1]
    
    def draw(self, screen, ind: int):
        pygame.draw.rect(screen, self.get_color(ind), self.coords)

class Square(Figure):
    def __init__(self, color, coords) -> None:
        super().__init__(color, coords)
        x = 2*coords[0][0] - coords[1][0] if coords[0][0] < coords[1][0] else coords[1][0]
        y = 2*coords[0][1] - coords[1][1] if coords[0][1] < coords[1][1] else coords[1][1]
        width = 2*(coords[0][0] - x)
        height = 2*(coords[0][1] - y)
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen, ind: int):
        pygame.draw.rect(screen, self.get_color(ind), self.rect)

class Right_Triange(Figure):
    def __init__(self, color, coords) -> None:
        super().__init__(color, coords)
        self.a, self.b = self.coords
        if (self.a[0] < self.b[0]):
            self.c = (max(self.a[0], self.b[0]), min(self.a[1], self.b[1]))
        else:
            self.c = (min(self.a[0], self.b[0]), min(self.a[1], self.b[1]))

    def draw(self, screen, ind: int):
        pygame.draw.polygon(screen, self.get_color(ind), (self.a, self.b, self.c))

class Equaterial_Triange(Figure):
    def __init__(self, color, coords) -> None:
        super().__init__(color, coords)
        center, self.a = self.coords
        vec = pygame.Vector2((-self.a[0] + center[0], -self.a[1] + center[1]))
        self.b = tuple(center + vec.rotate(60))
        self.c = tuple(center + vec.rotate(-60))

    def draw(self, screen, ind: int):
        pygame.draw.polygon(screen, self.get_color(ind), (self.a, self.b, self.c))

class Rhombus(Figure):
    def __init__(self, color, coords) -> None:
        super().__init__(color, coords)
        center = coords[0]
        point = list(coords[1])
        if (center[0] < point[0]): point[0] += abs(center[0] - point[0])
        if (center[1] > point[1]): point[1] -= abs(center[1] - point[1])
        self.a = (point[0], center[1])
        self.b = (center[0], point[1])
        self.c = (2*center[0] - point[0], center[1])
        self.d = (center[0], 2*center[1] - point[1])

    def draw(self, screen, ind: int):
        pygame.draw.polygon(screen, self.get_color(ind), (self.a, self.b, self.c,self.d))

def main():
    is_dif_colors = input("Do you want to use random colors? (y/n) ")

    COLOR_NAMES = ["white", "red", "green", "blue", "orange", "purple", "silver", "pink", "yellow", "black"]
    if is_dif_colors == 'y':
        COLOR_NAMES = [x for x, y in pygame.color.THECOLORS.items() if not x[-1].isdigit()]
        shuffle(COLOR_NAMES)
        COLOR_NAMES = COLOR_NAMES[:9] + ['black']

    print("""\nHelp:
    Moving the mouse:           draw trail after it
    Left mouse button click:    trail become thicker
    Right mouse button click:   trail become thinner
    Ctrl+W or Alt+F4:           close the window
    R:                          Rectange: two mouse click define vertexes of the rectangle
    C:                          Circle: first mouse click - center of the circle, second - point on radius
    E:                          Eraser (black trail)
    S:                          Square: first mouse click - center of the square, second - vertex
    T:                          Right triangle: two mouse cliks - vertexes of the triangle
    Ctrl+E:                     Ecuaterial triangle: first mouse click - center of the circle, second - vertex of the triangle
    Ctrl+R:                     Rhombus: first mouse click - center of the circle, second - vertex of the rectangle, where is rhombus
    Ctrl+Z:                     Drop mode to line\n""")
    for i, color in enumerate(COLOR_NAMES):
        print(f"    Number {i}:                   {color}")

    COLOR_CODES = [pygame.Color(x) for x in COLOR_NAMES]
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    cur_color = 0
    line_radius = 15
    points = []
    objects = []
    mode = "line"

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():                
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                    
                if event.key == pygame.K_z and ctrl_held:
                    mode = 'line'
                if event.key == pygame.K_r:
                    mode = 'rectangle'
                if event.key == pygame.K_c:
                    mode = 'circle'
                if event.key == pygame.K_e:
                    mode = 'eraser'
                if event.key == pygame.K_s:
                    mode = 'square'
                if event.key == pygame.K_t:
                    mode = 'rtriangle'
                if event.key == pygame.K_e and ctrl_held:
                    mode = 'etriangle'
                if event.key == pygame.K_r and ctrl_held:
                    mode = 'rhombus'


                key = pygame.key.name(event.key)
                if len(key) > 2 and key[1].isdigit():
                    cur_color = int(key[1])
            
            if event.type == pygame.MOUSEBUTTONDOWN and mode != "line" and mode != "eraser":
                points.append(event.pos)
                if len(points) == 2:
                    objects.append(get_object(mode, COLOR_CODES[cur_color], points, line_radius))
                    points.clear()
            
            if event.type == pygame.MOUSEMOTION:
                if mode == "line":
                    objects.append(Circle(COLOR_CODES[cur_color], event.pos, radius=line_radius))
                elif mode == "eraser":
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, line_radius)
        
        if mode != "eraser":
            for i, obj in enumerate(objects):
                obj.draw(screen, i)
            objects = objects[-255:]

        pygame.display.flip()
        clock.tick(60)

def get_object(mode, color, points, radius):
    obj = None
    if mode == "line": obj = Circle(color, points, radius=radius)
    elif mode == "rectangle": obj = Rectange(color, points)
    elif mode == "circle": obj = Circle(color, points)
    elif mode == "eraser": obj = Circle((0, 0, 0), points, radius=radius)
    elif mode == "square": obj = Square(color, points)
    elif mode == "rtriangle": obj = Right_Triange(color, points)
    elif mode == "etriangle": obj = Equaterial_Triange(color, points)
    elif mode == "rhombus": obj = Rhombus(color, points)

    return obj

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
