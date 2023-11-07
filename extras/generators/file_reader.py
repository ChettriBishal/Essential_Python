from typing import NamedTuple


class DataPoint(NamedTuple):
    x: float
    y: float
    z: float


def my_data_reader(file):
    for row in file:
        cols = row.rstrip().split(',')
        cols = [float(c) for c in cols]
        yield DataPoint._make(cols)


def example_reader():
    with open("my_data.txt", "r") as file:
        for row in my_data_reader(file):
            print(row)


example_reader()