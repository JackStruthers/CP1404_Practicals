"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        watched_status = ""
        if self.is_watched:
            watched_status = "watched"
        return "{}({} from {}){}".format(self.title, self.category, self.year, watched_status)

    def is_true(self):
        self.is_watched = True

    def is_false(self):
        self.is_watched = False

