def playSound(path):
    try:
        import pygame

        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=-1)  # repeat indefinitely
    except Exception as e:
        print(str(e))