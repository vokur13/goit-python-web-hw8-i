from models import Quotes, Authors
from db.connect_db import connect


def quotes_by_author(name: str):
    authors = Authors.objects(fullname=name)
    for author in authors:
        quotes = Quotes.objects(author=author)
        all_quotes_list = list()
        for quote in quotes:
            all_quotes_list.append(quote["quote"])
        return all_quotes_list


if __name__ == "__main__":
    result = quotes_by_author("Albert Einstein")
    print(result)
