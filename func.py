def playSound(path):
    try:
        import pygame

        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=-1)
    except Exception as e:
        pass

def logs(description, Type):
    import datetime

    try:
        error_file = open("Logs.txt", "a")
    except:
        error_file = open("Logs.txt", "w")

    if Type == "Warning":
        error_file.write(
            str(datetime.datetime.now())
            + " | "
            + "_DEV Warning: "
            + str(description)
            + "\n"
        )
    else:
        error_file.write(
            str(datetime.datetime.now())
            + " | "
            + "_DEV ERROR: "
            + str(description)
            + "\n"
        )