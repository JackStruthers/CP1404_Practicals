"""
Name: Jack Struthers
Date: 17/10/2019
Brief Project Description: An app that lets you mark movies as watched or not and add new movies to the list
GitHub URL: https://github.com/cp1404-students/2019-2-a2-JackStruthers.git
"""
import operator
from movie import Movie
from moviecollection import MovieCollection


# Opens and closes the initial read file and displays the menu
def main():
    """..."""
    print("Movies To Watch 1.0 - by Jack Struthers")

    movie_details = MovieCollection()
    movie_details.load_movies("movies.csv")

    for movie in movie_details.movies:
        print(movie)

    print("{} movies loaded from file".format(movie_details.number_of_movies()))

    menu = "Menu: \n" \
           "L - List Movies \n" \
           "A - Add new movie \n" \
           "W - Watch a movie \n" \
           "Q - Quit"
    print(menu)

    menu_option = option_selection()

    while menu_option != "Q":
        if menu_option == "L":
            movie_details = sort_list_by_year(movie_details)
            print_ordered_movie_list(movie_details)
        elif menu_option == "A":
            add_new_movie(movie_details)
        else:
            movie_details = watch_movie(movie_details)

        print(menu)
        menu_option = option_selection()

    movie_details.save_movies("movies.csv")
    print("{} movies saved to movies.csv\nHave a nice day :)".format(movie_details.number_of_movies()))


# Prints the initial movie list and appends to a mast list
# def print_movie_file(list_of_movies, movie_file):
#     for line in movie_file:
#         movie_details = str(line).strip("\n")
#         list_of_movies.append(movie_details)


# Error checks user menu selection
def option_selection():
    menu_option = input(">>>").upper()
    while menu_option != "L" and menu_option != "A" and menu_option != "W" and menu_option != "Q":
        print("Invalid menu choice")
        menu_option = input(">>>").upper()
    return menu_option


# Splits main list into a list of lists
# def split_movie_list(list_of_movies):
#     movie_details = []
#     for line in list_of_movies:
#         line = str(line).split(',')
#         line[1] = int(line[1])
#         movie_details.append(line)
#
#     return movie_details


# Sorts movies in order of year
def sort_list_by_year(movie_details):
    movie_details.sort("year")
    return movie_details


# Prints an ordered version of the movie list
def print_ordered_movie_list(movie_details):
    unwatched_movies = movie_details.count_unwatched_movies()
    watched_movies = movie_details.count_watched_movies()
    for i, movie in enumerate(movie_details.movies):
        if not movie.is_watched:
            print("{}. * {:<35} - {:>4} ({})".format(i, movie.title, movie.year, movie.category))
        else:
            print("{}.   {:<35} - {:>4} ({})".format(i, movie.title, movie.year, movie.category))

    print("{} movies watched, {} movies still to watch".format(watched_movies, unwatched_movies))


# Adds new movies to the list of movie details
def add_new_movie(movie_details):
    # new_movies = []
    title = check_title_and_genre("Title: ")
    # new_movies.append(title)

    year = check_number_input()
    # new_movies.append(year)

    category = check_title_and_genre("Category: ")
    # new_movies.append(category)

    # new_movies.append("u")

    new_movies = Movie(title, year, category, False)

    movie_details.add_movie(new_movies)

    print("{} ({} from {}) added to movie list".format(str(new_movies.title),
                                                       str(new_movies.category), str(new_movies.year)))


# Ensures the title and category for the movie are not blank
def check_title_and_genre(classification):
    detail = input(classification)
    while detail == "":
        print("Input can not be blank")
        detail = input(classification)
    return detail


# Ensures a valid year is inputted
def check_number_input():
    year = 0
    valid_year = False
    while not valid_year:
        try:
            year = int(input("Year: "))
            if year < 0:
                print("Number must be >= 0")
            else:
                valid_year = True
        except ValueError:
            print("Invalid input; enter a valid number")

    return year


# Sets a movie as watched and checks if all the movies have been watched
def watch_movie(movie_details):
    watched_counter = movie_details.count_watched_movies()

    # for i in range(len(movie_details)):
    #     if movie_details[i][-1] == "w":
    #         watched_counter += 1

    if watched_counter == movie_details.number_of_movies():
        print("No more movies to watch!")
    else:
        print("Enter the number of a movie to mark as watched")
        movie_option = check_movie_option(movie_details)

        movie = None

        for i, movie in enumerate(movie_details.movies):
            movie = movie
            if i == movie_option:
                break

        if movie.is_watched:
            print("You have already watched {}".format(movie.title))
        else:
            movie.is_watched = True
            print("{} from {} watched".format(movie.title, movie.year))

    return movie_details


# Checks that a movie option is valid
def check_movie_option(movie_details):
    movie_to_watch = 0
    number_of_movies = movie_details.number_of_movies()
    valid_movie = False
    while not valid_movie:
        try:
            movie_to_watch = int(input(">>> "))
            if movie_to_watch < 0:
                print("Number must be >= 0")
            elif movie_to_watch > number_of_movies:
                print("Invalid movie number")
            else:
                valid_movie = True
        except ValueError:
            print("Invalid input; enter a valid number")

    return movie_to_watch


# Writes the new list of movies to the file
def write_movies_to_file(movie_details):
    update_movie_list = open("movies.csv", "w")
    for movie in movie_details:
        update_movie_list.write("{},{},{},{}\n".format(*movie))

    update_movie_list.close()


main()
