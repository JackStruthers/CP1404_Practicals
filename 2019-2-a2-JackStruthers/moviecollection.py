"""..."""


# TODO: Create your MovieCollection class in this file

from movie import Movie
import operator


class MovieCollection:
    """..."""
    def __init__(self):
        self.movies = []

    def __str__(self):
        return "{}".format(self.movies)

    def load_movies(self, file_name):
        with open(file_name, "r") as in_file:
            for line in in_file:
                line = line.strip(" ")
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
        if sort_by == "unwatched":
            return self.movies.sort(key=operator.attrgetter("is_watched", "title"))
        elif sort_by == "watched":
            return self.movies.sort(key=operator.attrgetter("is_watched", "title"), reverse=True)
        else:
            return self.movies.sort(key=operator.attrgetter(sort_by, "title"))

    def save_movies(self, file_name):
        output_file = open(file_name, "w")
        for movie in self.movies:
            if movie.is_watched:
                movie.is_watched = "w"
            else:
                movie.is_watched = "u"
            output_line = "{},{},{},{}\n".format(movie.title, movie.year, movie.category, movie.is_watched)
            output_file.write(output_line)
