import random

movies_list = [{'name': 'the dark night', 'year': 2008, 'rating': '9'},
               {'name': 'the Godfather', 'year': 1972, 'rating': '9.2'},
               {'name': '12 angry men', 'year': 1957, 'rating': '9'},
               {'name': 'rush', 'year': 2013, 'rating': '8'},
               ]


class Movies():
    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    @property
    def rank(self):
        """
        'S':lt8.5
        'A':lt8
        'B':lt7
        'C':lt6
        'd':st6
        """
        rating_num = float(self.rating)
        if rating_num >= 8.5:
            return 'S'
        elif rating_num >= 8:
            return 'A'
        elif rating_num >= 7:
            return 'B'
        elif rating_num >= 6:
            return 'C'
        else:
            return 'D'


# sort movies list
def get_movies_list_sorted(movies, sorted_type):
    """
    :param movies: object
    :param sorted_type: name,year,rating,random
    :return:
    """
    if sorted_type == 'name':
        sorted_movies = sorted(movies, key=lambda movies: movies.name.lower())
    elif sorted_type == 'year':
        sorted_movies = sorted(movies, key=lambda movies: movies.year, reverse=True)
    elif sorted_type == 'rating':
        sorted_movies = sorted(movies, key=lambda movies: float(movies.rating), reverse=True)
    elif sorted_type == 'random':
        sorted_movies = sorted(movies, key=lambda movies: random.random())
    else:
        raise RuntimeError(f'Unknown sorting type: {sorted_type}')
    return sorted_movies


def main():
    all_sorting_types = ('name', 'year', 'rating', 'random')
    sort_input = input('Please input sorting type')
    if sort_input not in all_sorting_types:
        print(f'Sorry, {sort_input} is not a valid sorting type, please choose from {all_sorting_types}')
        return

    # initial movies data
    movie_items = []
    for m in movies_list:
        movie_items.append(Movies(**m))

    sorted_movies = get_movies_list_sorted(movie_items, sort_input)
    for movie in sorted_movies:
        print(f'-[{movie.rank}] {movie.name}({movie.year}) | rating: {movie.rating}')


if __name__ == '__main__':
    main()
