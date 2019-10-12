"""..."""


# TODO: Create your MovieCollection class in this file

from movie import Movie
import operator


class MovieCollection:
    """..."""
    def __init__(self):
        self.movies = []

    def load_movies(self, file_name):
        with open(file_name, "r") as in_file:
            for line in in_file:
                line = line.strip("\n")
                line = line.split(",")
                movie = Movie(line[0], int(line[1]), line[2], line[3])

                if movie.is_watched == "u":
                    movie.has_not_watched()
                else:
                    movie.has_been_watched()

                self.movies.append(movie)

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort(self, sort_by):
        if sort_by == "year":
            return self.movies.sort(key=operator.attrgetter("year", "title"))
        elif sort_by == "title":
            return self.movies.sort(key=operator.attrgetter("title"))
        elif sort_by == "category":
            return self.movies.sort(key=operator.attrgetter("category", "title"))
        elif sort_by == "unwatched":
            return self.movies.sort(key=operator.attrgetter("is_watched", "title"))
        elif sort_by == "watched":
            return self.movies.sort(key=operator.attrgetter("is_watched", "title"), reverse=True)
