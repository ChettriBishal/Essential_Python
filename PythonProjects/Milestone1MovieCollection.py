# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie_details(movies):
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def list_movies(movies):
    print("MOVIES")
    for counter, movie in enumerate(movies):
        print(f"{counter}. Title: {movie['title']} | Director: {movie['director']} | Year: {movie['year']}")
    

def find_movies(movies):
    movie_key = input('Enter the title of the movie to search: ')
    all_movies = {movie['title'].lower() for movie in movies}
    if movie_key.lower() in all_movies:
        print("Movie is in the list")
    else:
        print("Movie is NOT in the list")


# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie_details(movies)
    elif selection == "l":
        list_movies(movies)
    elif selection == "f":
        find_movies(movies)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!