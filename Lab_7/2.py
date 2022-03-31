import pygame, os



print("""Settings:
Play/pause:     space
Next:           right arrow
Previous:       left arrow
Stop/restart:   escape""")

FORMATS = ["flac", 'mp3', 'ogg', 'm4a']

while True:
    directory = r"C:\Users\Oleg\Music\初音ミクシンフォニー～Miku Symphony 2020 オーケストラライブ (24-96)" #input("From which folder you want to listen music? ")
    try:
        songs = [x for x in os.listdir(directory) if not os.path.isdir(rf"{directory}\{x}") and x.split('.')[-1] in FORMATS]
    except FileNotFoundError:
        print(f"{directory} doesn't exist")
    else: 
        if len(songs) > 0:
            break
        else:
            print("There aren't supported files")

cur_song = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200, 200))
done = False
is_played = False

def play():
    pygame.mixer.music.unload()
    print(f"Now playing {songs[cur_song]}")
    pygame.mixer.music.load(rf"{directory}\{songs[cur_song]}")
    pygame.mixer.music.play(-1)
    is_played = True

play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            cur_song -= 1
            if (cur_song >= 0):
                play()
            else:
                print("No previous song")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            cur_song += 1
            if (cur_song < len(songs)):
                play()
            else:
                print("No more songs")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if is_played:
                pygame.mixer.music.stop()
                is_played = False
            else:
                play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if is_played:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            is_played = not is_played

    clock.tick(60)


pygame.quit()