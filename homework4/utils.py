import csv
import json


def load_users(path) -> list:
    """
    Load users list from path.
    """
    with open(path) as file:
        users = json.load(file)

    return users


def load_books(path) -> list:
    """
    Load books list from path
    """
    with open(path) as file:
        books = [book for book in csv.DictReader(file)]

    return books
