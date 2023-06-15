import sys

movie_name = ""
movies = set()
while True:
    movie_name = input()
    if not movie_name:
        break
    movies.add(movie_name)

preferred_movies = {}

firstname = ""
while True:
    firstname = input()
    if not firstname:
        break
    person_movies = []
    for index in range(10):
        movie_name = input()
        if not movie_name:
            break
        person_movies.append(movie_name)
    preferred_movies[firstname] = person_movies

movie_score = {}
for firstname, person_movies in preferred_movies.items():
    for movie in person_movies:
        if movie in movie_score:
            movie_score[movie] += 1
        else:
            movie_score[movie] = 1

movies_recommended = {}
for firstname, person_movies in preferred_movies.items():
    for index, movie in enumerate(person_movies):
        other_movies = person_movies[:index] + person_movies[index+1:]
        if movie not in movies_recommended:
            movies_recommended[movie] = {}
        for other_movie in other_movies:
            if other_movie not in movies_recommended[movie]:
                movies_recommended[movie][other_movie] = 0
            movies_recommended[movie][other_movie] += 1

if len(sys.argv) > 1:
    for index in range(1, len(sys.argv)):
        firstname = sys.argv[index]
        you_should_watch = {}
        for movie in preferred_movies[firstname]:
            other_movies = movies_recommended[movie]
            for other_movie, score in other_movies.items():
                if other_movie in preferred_movies[firstname]:
                    continue
                if other_movie not in you_should_watch:
                    you_should_watch[other_movie] = 0
                you_should_watch[other_movie] += score

        for movie, score in you_should_watch.items():
            you_should_watch[movie] /= movie_score[movie]
        print(firstname, you_should_watch)