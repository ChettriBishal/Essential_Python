class Movie:
    '''
    Used to create a single movie instance
    '''

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __repr__(self) -> str:
        return f'Movie: {self.title}, {self.director}, {self.year}'


class Movies:
    '''
    Movies to encapsulate movie details
    '''

    def __init__(self):
        self.movie_list = []

    def __len__(self):
        return len(self.movie_list)

    def __getitem__(self, i):
        return self.movie_list[i]

    def __repr__(self):
        return f'Movies {self.movie_list}'

    def add_movie(self, movie):
        self.movie_list.append(movie)
        print(f"Movie with the title {movie.title} added!")

    def list_movie(self):
        print("Movies in the list")
        for movie in self.movie_list:
            print(f'Title: {movie.title}')
            print(f'Director: {movie.director}')
            print(f'Release Year: {movie.year}')
            print('\n')

    def find_movie(self):
        f_title = input('Enter the title of the movie to find: ')
        for movie in self.movie_list:
            # print(f'{f_title} compared with {movie.title.lower()}')
            if movie.title.lower() == f_title.lower():
                print(f'{f_title.title()} found in the list!')
                break
        else:
            print(f'{f_title.title()} is NOT in the list')
