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
def print_movie(movie):
    print(f"Title: {movie['title']} | Director: {movie['director']} | Year: {movie['year']}")
def list_movies(movies):
    print("MOVIES")
    for counter, movie in enumerate(movies):
        print(counter, end = ' ')
        print_movie(movie)
        
    

def find_movies(movies):
    movie_key = input('Enter the title of the movie to search: ')
    all_movies = {movie['title'].lower() for movie in movies}
    if movie_key.lower() in all_movies:
        print("Movie Found!!!")
        for movie in movies:
            if movie['title'].lower() == movie_key.lower():
                print_movie(movie)
    else:
        print("Movie is NOT in the list")



# Remember first class functions ? 
operations = {
    'a': add_movie_details,
    'l': list_movies,
    'f': find_movies
}

# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection in operations:
        operations[selection](movies)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!