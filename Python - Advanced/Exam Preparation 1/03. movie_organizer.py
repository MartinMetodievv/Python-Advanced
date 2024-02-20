def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)
    sorted_movies = sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for k, v in sorted_movies:
        result += f'{k} - {len(v)}\n'
        for mov in sorted(v):
            result += f'* {mov}\n'
    return result


print(movie_organizer(

    ("The Godfather", "Drama"),

    ("The Hangover", "Comedy"),

    ("The Shawshank Redemption",

     "Drama"),

    ("The Pursuit of Happiness",

     "Drama"),

    ("The Hangover Part II", "Comedy")))
