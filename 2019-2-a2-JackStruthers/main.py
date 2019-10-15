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


class MoviesToWatchApp(App):
    """..."""

    current_sort = StringProperty()
    sort_movies = ListProperty()

    def __init__(self, **kwargs):
        """Initiate self"""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies(FILENAME)

    def build(self):
        """Build self for kiviy"""
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file("app.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons for every movie in the movie file"""
        for movie in self.movie_collection.movies:
            watched_string = ""
            if movie.is_watched:
                watched_string = "watched"
            temp_button = Button(text="{} ({} from {}) {}".format(movie.title, movie.category, movie.year,
                                                                  watched_string), id="{}".format(movie.title))
            # temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)


if __name__ == '__main__':
    MoviesToWatchApp().run()
