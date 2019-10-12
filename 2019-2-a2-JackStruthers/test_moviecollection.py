"""(Incomplete) Tests for MovieCollection class."""
from moviecollection import MovieCollection
from movie import Movie


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("\nTest loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    for line in movie_collection.movies:
        print(line)

    # Test adding a new Movie with values
    print("\nTest adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    for line in movie_collection.movies:
        print(line)

    # Test sorting movies
    print("\nTest sorting - year:")
    movie_collection.sort("year")
    for line in movie_collection.movies:
        print(line)

    print("\nTest sorting - title:")
    movie_collection.sort("title")
    for line in movie_collection.movies:
        print(line)

    print("\nTest sorting - category:")
    movie_collection.sort("category")
    for line in movie_collection.movies:
        print(line)

    print("\nTest sorting - unwatched:")
    movie_collection.sort("unwatched")
    for line in movie_collection.movies:
        print(line)

    print("\nTest sorting - watched:")
    movie_collection.sort("watched")
    for line in movie_collection.movies:
        print(line, "\n")

    print(movie_collection.number_to_watch())

    # TODO: Add more sorting tests

    # TODO: Test saving movies (check CSV file manually to see results)

    # TODO: Add more tests, as appropriate, for each method


run_tests()
