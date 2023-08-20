from db.models import Quotes


def quotes_by_tag(tag: str):
    quotes = Quotes.objects(tags__name=tag)
    for quote in quotes:
        all_quotes_list = list()
        all_quotes_list.append(quote.quote)
        return all_quotes_list


if __name__ == "__main__":
    result = quotes_by_tag("life")
    print(result)
