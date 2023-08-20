from db.models import Authors, Quotes, Tag
import json
from datetime import datetime
from connect_db import connect

authors = "../json_data/authors.json"
quotes = "../json_data/quotes.json"

if __name__ == "__main__":
    with open(authors, "r") as fa:
        data = json.load(fa)

        for item in data:
            born_date_str = item["born_date"]
            born_date = datetime.strptime(born_date_str, "%B %d, %Y")
            author = Authors(
                fullname=item["fullname"],
                born_date=born_date,
                born_location=item["born_location"],
                description=item["description"],
            ).save()

    with open(quotes, "r") as fq:
        quotes = json.load(fq)

        for quote in quotes:
            authors = Authors.objects(fullname=quote["author"])
            for author in authors:
                if quote["author"] == author["fullname"]:
                    tags = []
                    for item in quote["tags"]:
                        tags.append(Tag(name=item))
                    Quotes(tags=tags, author=author, quote=quote["quote"]).save()
