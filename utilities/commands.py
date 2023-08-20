from reed_data.quotes_by_author import quotes_by_author
from reed_data.quotes_by_tag import quotes_by_tag
from reed_data.quotes_by_tags import quotes_by_tags
from utilities import sortie

COMMANDS = {
    "name": quotes_by_author,
    "tag": quotes_by_tag,
    "tags": quotes_by_tags,
    "exit": sortie,
}
