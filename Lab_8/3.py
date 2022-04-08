import sys
import pygame
from random import shuffle

def main():
    is_dif_colors = "y"#input("Do you want to use random colors? (y/n) ")

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
    Q:                          drawn change color, second pressing cancel
    R:                          two mouse click define vertexes of the rectangle
    C:                          first mouse click - center of the circle, second - point on line_radius
    E:                          become eraser (black trail)
    Ctrl+Z:                     cancel circle, eraser and rectangle\n""")
    for i, color in enumerate(COLOR_NAMES):
        print(f"    Number {i}:                   {color}")

    COLOR_CODES = [pygame.Color(x) for x in COLOR_NAMES]

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    line_radius = 15
    cur_color = 0

    is_line = True
    points = []

    is_rectange = False
    rectangle_points = []

    is_circle = False
    circle_center = []
    circle_radius = 0

    is_eraser = False
    is_change_color = False


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
                    is_line = True
                    is_circle = is_eraser = is_eraser = False
                if event.key == pygame.K_r:
                    rectangle_points = []
                    is_rectange = True
                    is_circle = is_eraser = is_line = False
                if event.key == pygame.K_c:
                    circle_center = []
                    is_circle = True
                    is_rectange = is_eraser = is_line = False
                if event.key == pygame.K_e:
                    is_eraser = True
                    is_circle = is_rectange = is_line = False
                if event.key == pygame.K_q:
                    is_change_color = not is_change_color
                    if is_change_color:
                        for i in range(len(points)):
                            points[i][1] = COLOR_CODES[cur_color]


                key = pygame.key.name(event.key)
                if len(key) > 2 and key[1].isdigit():
                    cur_color = int(key[1])
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_rectange:
                    x, y = event.pos
                    if len(rectangle_points) == 0:
                        rectangle_points = [x, y]
                    else:
                        rectangle_points[0], x = min(rectangle_points[0], x), max(rectangle_points[0], x)
                        rectangle_points[1], y = min(rectangle_points[1], y), max(rectangle_points[1], y)
                        rectangle_points.append(x - rectangle_points[0])
                        rectangle_points.append(y - rectangle_points[1])
                elif is_circle:
                    x, y = event.pos
                    if len(circle_center) == 0:
                        circle_center = [x, y]
                    else:
                        circle_radius = round(((x - circle_center[0])**2 + (y - circle_center[1])**2)**0.5)
                else:
                    if event.button == 1: # left click grows line_radius
                        line_radius = min(200, line_radius + 1)
                    elif event.button == 3: # right click shrinks line_radius
                        line_radius = max(1, line_radius - 1)
            
            if event.type == pygame.MOUSEMOTION and is_line:
                # if mouse moved, add point to list
                position = event.pos
                points.append([position, COLOR_CODES[cur_color] if not is_eraser else COLOR_CODES[-1]])
                points = points[-256:]

        #if not is_eraser:
            #screen.fill((0, 0, 0))
        
        # draw all points
        if is_line:
            for i in range(len(points)-1):
                drawLineBetween(screen, i, points[i][0], points[i + 1][0], line_radius, 
                                points[i + 1][1])
        elif is_rectange:
            points = []
            if len(rectangle_points) >= 4:
                pygame.draw.rect(screen, COLOR_CODES[cur_color], rectangle_points)
                rectangle_points = []
        elif is_circle:
            points = []
            if len(circle_center) >= 2 and circle_radius:
                pygame.draw.circle(screen, COLOR_CODES[cur_color], circle_center, circle_radius)
                circle_center = []
                circle_radius = 0

        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    new_color = list(color)
    for i in range(3):
        new_color[i] = round(color[i] * (index/256))

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, new_color, (x, y), width)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
