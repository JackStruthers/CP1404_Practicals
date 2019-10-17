"""
Name: Jack Struthers
Date: 17/10/2019
Brief Project Description: An app that lets you mark movies as watched or not and add new movies to the list
GitHub URL: https://github.com/cp1404-students/2019-2-a2-JackStruthers.git
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
        return "{} ({} from {}) {}".format(self.title, self.category, self.year, watched_status)

    def has_been_watched(self):
        """This function is used to say that a movie that is watched has a true status for is_watched"""
        self.is_watched = True

    def has_not_watched(self):
        """This function is used to say that a movie that is not watched has a false status for is_watched"""
        self.is_watched = False
