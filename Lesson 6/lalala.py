def song_gen(strings=3, las=3, end=0):
    string = (('la'+'-') * las).strip('-')
    song = (string + '\n') * (strings - 1) + string + ('.' if end == 0 else '!')
    return song

if __name__ == "__main__":
    print(song_gen(strings=5, las=6, end=1))
