from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """

    my_dict = defaultdict(lambda: 'Unknown')
    my_dict['Alan'] = 'Manchester'
    return my_dict


def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """

    # remove the first entry
    arg_od.pop(next(iter(arg_od)))

    # remove the last entry
    arg_od.pop(next(reversed(arg_od)))

    # move the entry with key name 'Bob' to the end of 'arg_od'
    arg_od.move_to_end('Bob')

    # move the entry with key name 'Dan' to the start of 'arg_od'
    arg_od.move_to_end('Dan', last=False)


# solution from the course
def task2_course(arg_od: OrderedDict):
    arg_od.popitem()  # remove the last element
    arg_od.popitem(False)  # remove the first element
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)


def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """

    Player = namedtuple('Player', ['name', 'club'])
    player_obj = Player(name, club)

    return player_obj


def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """

    arg_deque.pop()
    first_element = arg_deque.popleft()
    arg_deque.append(first_element)
    arg_deque.appendleft('Zack')
