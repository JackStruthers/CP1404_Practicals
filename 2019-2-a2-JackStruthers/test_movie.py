"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    print(initial_movie)

    initial_movies = [Movie("Thor: Ragnarok", 2017, "Comedy", True), Movie("Avengers Endgame", 2019, "action", "u")]

    for movie in initial_movies:
        if movie.is_watched == "u":
            movie.is_false()
        else:
            movie.is_true()
        print(movie)


run_tests()
