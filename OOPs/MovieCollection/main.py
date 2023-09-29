from movies_module import Movies, Movie

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "


# You may want to create a function for this code
def take_input(my_movies):
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    new_movie = Movie(title, director, year)
    return new_movie


def user_menu(my_movies):
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            new_movie = take_input(my_movies)
            my_movies.add_movie(new_movie)
        elif selection == "l":
            my_movies.list_movie()
        elif selection == "f":
            my_movies.find_movie()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


my_movies = Movies()
new_movie = Movie("Snowden", "Somebody Else", 2014)
my_movies.movie_list.append(new_movie)

# print(len(my_movies))

user_menu(my_movies)
print(repr(my_movies))
