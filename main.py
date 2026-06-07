import pygame, os


def main():
    print("""
Welcome to the clmp (command line music player)
Here is a list of commands""")
    commands()
    print("To see this list again, use 'Commands'")
    pygame.mixer.init()

    song_paths = os.listdir("songs")
    song_paths.sort()
    song_names = [s.replace(".ogg", "") for s in song_paths]

    current_song = ""

    while True:
        command = input(">>> ").lower()
        args = command.split(" ", 1)
        args.append(
            None
        )  # Workaround for IndexError thrown if args[1] == '--help' if user passes only 1 arg

        match args[0]:
            case "play":
                if args[1] == None:
                    print("'Play --help' for help")
                elif args[1] == "--help":
                    help_play()
                else:
                    lowercase_names = [s.lower() for s in song_names]
                    if args[1].rstrip(".ogg") not in lowercase_names:
                        print("Second argument should be song name or song not found")
                    else:
                        file_path = os.path.join("songs", args[1] + ".ogg")
                        current_song = file_path
                        pygame.mixer.music.load(file_path)
                        pygame.mixer.music.play()

            case "list":
                if args[1] == None:
                    print("'List --help' for help")
                if args[1] == "--help":
                    help_list()
                else:
                    show_list(song_names)

            case "pause":
                if args[1] == None:
                    pygame.mixer.music.pause()
                elif args[1] == "--help":
                    help_pause()

            case "resume":
                if args[1] == None:
                    pygame.mixer.music.unpause()
                elif args[1] == "--help":
                    help_resume()

            case "stop":
                if args[1] == None:
                    pygame.mixer.music.unload()
                elif args[1] == "--help":
                    help_stop()

            case "skip":
                if args[1] == None:
                    sound = pygame.mixer.Sound(current_song)
                    pygame.mixer.music.set_pos(sound.get_length())
                elif args[1] == "--help":
                    help_skip()

            case "queue":
                if args[1] == None:
                    print("'Queue --help' for help")
                elif args[1] == "--help":
                    help_queue()
                else:
                    lowercase_names = [s.lower() for s in song_names]
                    if args[1].rstrip(".ogg") not in lowercase_names:
                        print("Second argument should be song name or song not found")
                    else:
                        file_path = os.path.join("songs", args[1] + ".ogg")
                        pygame.mixer.music.queue(file_path)

            case "volume":
                if args[1] == None:
                    print("'Volume --help' for help")
                elif args[1] == "--help":
                    help_volume()
                elif args[1] == "--status":
                    print(f"Volume is at {pygame.mixer.music.get_volume()}")
                elif 0 > int(args[1]) > 100:
                    print("Volume must be between 0 and 100")
                elif 0 <= int(args[1]) <= 100:
                    pygame.mixer.music.set_volume(int(args[1]) / 100)

            case "commands":
                commands()


def help_play():
    print("""
Play is used to play a song. The syntax is 'Play [song title]'. Using the play command while a song is already playing will
cause the CLMP to skip the currently playing song and begin whichever song you requested. In order to queue a song, use the
'Queue' command. Use 'Queue --help' for more info on Queue
""")


def help_list():
    print("""
List is used to list all the songs in the songs directory. It lists items 10 at a time as to not hijack your terminal window in song names.
Use 'Q' to stop listing, or press any other key to continue listing the next 10 songs.
""")


def help_pause():
    print("""
Pause is used to pause the current song. Pausing a song will not unload the song from the player, meaning a simple 'Resume' command will
continue playing your music. For more info on the 'Resume' command enter the command 'Resume --help'.
""")


def help_resume():
    print("""
Resume is used to unpause a currently paused track. For more info on pausing, use 'Pause --help'.
""")


def help_stop():
    print("""
Stop is used to completely unload a song from the CLMP. This will stop playing any music, and using 'Resume' will not work
""")


def help_skip():
    print("""
Skip is used to skip a song. If there is no song in queue the command will act similarly to the 'Stop' command
""")


def help_queue():
    print("""
Queue is used to set a song to play at the end of the current song. Due to limitations of pygame, only one song can be queued at a time.
Attempting to queue a song while another song is queued will result in the new queued song overwriting the previous queued song.
The song playing will remain unaffected.
""")


def help_volume():
    print("""
Volume is used to set the volume of playback. By using volume --status you can get the current volume. Due to how pygame works, the
percentage you see may be slightly off from the volume you set. The syntax for this command is 'Volume [1-100]'.
""")


def show_list(song_names):
    for i in range(len(song_names)):
        if i > 1 and i % 10 == 0:
            print("Enter any key other than 'Q' as a command to continue listing")
            if input(">>> ").lower() == "q":
                break
        print(song_names[i])


def commands():
    print("""
Play
List
Pause
Resume
Stop
Skip
Queue
Commands""")


if __name__ == "__main__":
    main()
