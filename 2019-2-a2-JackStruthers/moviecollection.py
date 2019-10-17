"""
Name: Jack Struthers
Date: 17/10/2019
Brief Project Description: An app that lets you mark movies as watched or not and add new movies to the list
GitHub URL: https://github.com/cp1404-students/2019-2-a2-JackStruthers.git
"""


from movie import Movie
import operator


class MovieCollection:
    """This class handles most of the functions involving manipulating the data """
    def __init__(self):
        self.movies = []

    def __str__(self):
        return "{}".format(self.movies)

    def load_movies(self, file_name):
        """This function loads the movie a given file and puts it in the format that Movie uses"""
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
        """This function will a movie to the movie collection list"""
        self.movies.append(movie)

    def sort(self, sort_by):
        """This will let the user sort the data in a prefered way"""
        if sort_by == "watched":
            return self.movies.sort(key=operator.attrgetter("is_watched", "title"), reverse=True)
        else:
            return self.movies.sort(key=operator.attrgetter(sort_by, "title"))

    def save_movies(self, file_name):
        """This will save the data to file"""
        output_file = open(file_name, "w")
        for movie in self.movies:  # changes the true or false to a u or w so that it matches the format of the file
            if movie.is_watched:
                movie.is_watched = "w"
            else:
                movie.is_watched = "u"
            output_line = "{},{},{},{}\n".format(movie.title, movie.year, movie.category, movie.is_watched)
            output_file.write(output_line)

    def count_unwatched_movies(self):
        """This function counts how many movies are yet to be watched"""
        unwatched_counter = 0
        for movie in self.movies:
            if not movie.is_watched:
                unwatched_counter += 1
        return "{}".format(unwatched_counter)

    def count_watched_movies(self):
        """This function counts how many movies have been watched"""
        watched_counter = 0
        for movie in self.movies:
            if movie.is_watched:
                watched_counter += 1
        return "{}".format(watched_counter)

    def number_of_movies(self):
        """This function counts how many movies are in the current list of movies"""
        number_of_movies = 0
        for movie in self.movies:
            number_of_movies += 1
        return number_of_movies
