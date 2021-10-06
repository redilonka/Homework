import os
import json
import itertools

from homework4.utils import load_users, load_books


class Distributer:
    """
    Distributer for book list.
    """
    def __init__(self, users, books) -> None:
        self.users = users
        self.books = books
        self.roster = {}

        for user in users:
            self.roster[user.get("name")] = {
                "name":    user.get("name", ''),
                "gender":  user.get("gender", 'binary'),
                "address": user.get("address", ''),
                "age":     user.get("age", 18),
                "books": []
            }

    @staticmethod
    def serialize(book) -> dict:
        return {
            "title":  book.get("Title", ""),
            "author": book.get("Author", ""),
            "pages":  int(book.get("Pages", "0")),
            "genre":  book.get("Genre", "")
        }

    def distribute(self) -> None:
        """
        Distribute books between users.
        """
        users = itertools.cycle(self.users)

        for book in self.books:
            # get next user
            user = next(users)
            self.roster[user["name"]]["books"].append(self.serialize(book))

    def save(self) -> None:
        """
        Write a resulter list of users with books to file.
        """
        result = [user for user in self.roster.values()]

        with open(f"{os.path.dirname(__file__)}/result.json", "w") as file:
            file.write(json.dumps(result, indent=4))



if __name__ == "__main__":
    users = load_users(f"{os.path.dirname(__file__)}/users.json")
    books = load_books(f"{os.path.dirname(__file__)}/books.csv")

    dist = Distributer(users, books)
    dist.distribute()
    dist.save()
