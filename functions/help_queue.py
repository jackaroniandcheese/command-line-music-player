def help_queue():
    print("""
Queue is used to set a song to play at the end of the current song. Due to limitations of pygame, only one song can be queued at a time.
Attempting to queue a song while another song is queued will result in the new queued song overwriting the previous queued song.
The song playing will remain unaffected.
""")
