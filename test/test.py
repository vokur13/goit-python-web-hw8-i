from reed_data.quotes_by_author import quotes_by_author
from reed_data.quotes_by_tag import quotes_by_tag
from reed_data.quotes_by_tags import quotes_by_tags
from db.connect_db import connect

operations = {"name": quotes_by_author, "tag": quotes_by_tag, "tags": quotes_by_tags}

if __name__ == "__main__":
    # print(quotes_by_author)
    print(operations["name"] == quotes_by_author)
    # operations["name"]("Steve Martin")
