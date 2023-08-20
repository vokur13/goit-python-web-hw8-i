from db.models import Quotes


def quotes_by_tags(tags: list):
    quotes = Quotes.objects(tags__name__in=tags)
    for quote in quotes:
        all_quotes_list = list()
        all_quotes_list.append(quote.quote)
        return all_quotes_list


if __name__ == "__main__":
    result = quotes_by_tags(["life", "live"])
    print(result)
