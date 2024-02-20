def add_songs(*args):
    songs = {}
    for song, lyrics in args:
        if song not in songs:
            songs[song] = []
        songs[song].append(lyrics)
    result = ''
    for k, v in songs.items():
        result += f'- {k}\n'
        for el in v:
            if len(el) > 0:
                for l in el:
                    result += f'{l}\n'

    return result


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
