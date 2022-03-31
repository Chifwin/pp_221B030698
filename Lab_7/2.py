import pygame, os


pygame.init()

print("""Settings:
Play/stop:      space
Next:           right arrow
Previous:       left arrow""")

FORMATS = ["flac", 'mp3', 'ogg', 'm4a']

while True:
    directory = r"C:\Users\Oleg\Music\初音ミクシンフォニー～Miku Symphony 2020 オーケストラライブ (24-96)" #input("From which folder you want to listen music? ")
    try:
        songs = [x for x in os.listdir(directory) if not os.path.isdir(rf"{directory}\{x}") and x.split('.')[-1] in FORMATS]
    except FileNotFoundError:
        print(f"{directory} doesn't exist")
    else:
        break

cur_song = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((200, 200))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)


pygame.quit()