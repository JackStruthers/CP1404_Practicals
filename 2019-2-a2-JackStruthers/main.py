"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from moviecollection import MovieCollection
from movie import Movie


FILENAME = "movies.csv"
WAYS_TO_SORT = {"Title": "title", "Year": "year", "Category": "category", "Watched": "watched",
                "Unwatched": "unwatched"}
WATCHED_BACKGROUND = (0.8, 0, 0.4, 1)
UNWATCHED_BACKGROUND = (0, 0.8, 0.8, 1)


class MoviesToWatchApp(App):
    """..."""

    status_text = StringProperty()
    sort_movies = ListProperty()

    def __init__(self, **kwargs):
        """Initiate self"""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies(FILENAME)

    def build(self):
        """Initiate Kivy"""
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file("app.kv")
        self.create_widgets()
        self.watched_unwatched_label()
        return self.root

    def create_widgets(self):
        """Create buttons for every movie in the movie file"""
        for movie in self.movie_collection.movies:
            colour = UNWATCHED_BACKGROUND

            if movie.is_watched:
                colour = WATCHED_BACKGROUND

            temp_button = Button(text="{}".format(movie), id="{}".format(movie.title), background_color=colour)
            temp_button.bind(on_release=self.have_watched)
            temp_button.movie = movie
            self.root.ids.entries_box.add_widget(temp_button)

    def watched_unwatched_label(self):
        """Is used to display how many movies have been watched and how are are still needed to be watched"""
        watched_amount = self.movie_collection.count_watched_movies()
        unwatched_amount = self.movie_collection.count_unwatched_movies()
        self.root.ids.watched_unwatched.text = "To watch: {} Watched: {}".format(unwatched_amount, watched_amount)

    def have_watched(self, instance):
        """After clicking unwatched movie it will inform the user it is now
         watched and do the opposite for a watched movie"""
        movie = instance.movie
        if not movie.is_watched:
            self.status_text = "You have watched {}".format(movie.title)
            movie.is_watched = True
        else:
            self.status_text = "You need to watch {}".format(movie.title)
            movie.is_watched = False

    def clear_widgets(self):
        """Clears all the dynamic buttons"""
        self.root.ids.entries_box.clear_widgets()

if __name__ == '__main__':
    MoviesToWatchApp().run()
