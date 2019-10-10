"""
Jack Struthers
Programming 2 Assignment 2
"""


class Movie:
    """This class will be used to keep the collection of movies, print them appropriately and determine
    if the movie is watched"""
    def __init__(self, title="", year=0, category="", is_watched=False):
        """This will initiate the class with the required movie details"""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """This class will print movies in the required format"""
        watched_status = ""
        if self.is_watched:
            watched_status = "watched"
        return "{}({} from {}){}".format(self.title, self.category, self.year, watched_status)

    def is_true(self):
        """This function is used to say that a movie that is watched has a true status for is_watched"""
        self.is_watched = True

    def is_false(self):
        """This function is used to say that a movie that is not watched has a false status for is_watched"""
        self.is_watched = False

