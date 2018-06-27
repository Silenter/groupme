from groupy.client import Client
import wikipedia
import inflection
import inflect
import random
from dotenv import load_dotenv
from os import getenv


def random_message():
    rand_page = wikipedia.random()
    # want a bottom level category
    page = wikipedia.page(rand_page)
    categories = page.categories
    filtered_categories = []

    for cat in categories:
        if ('rticle' not in cat and
                'wiki' not in cat and
                'Wiki' not in cat and
                'date' not in cat and
                'source' not in cat and
                'stub' not in cat):
            filtered_categories.append(cat)

    plural_category = random.choice(filtered_categories)
    singular_category = ""
    inflector = inflect.engine()
    for word in plural_category.split(" "):
        singular_word = inflector.singular_noun(word)
        if singular_word:
            singular_category = " ".join([singular_category, singular_word])
        else:
            singular_category = " ".join([singular_category, word])
    singular_category = inflection.titleize(singular_category).strip()
    return "Today's {} of the Day is {} {}".format(singular_category, rand_page, page.url)


load_dotenv()

# handle Disambiguation error
message = random_message()
while message is False:
    message = random_message()

print(message)

post = input('Post this message? ')
if post in ['y','yes']:
    groupme = Client.from_token(getenv('GROUPME_TOKEN'))
    dingus_parade = [group for group in groupme.groups.list() if group.id=='19442193'][0]
    dingus_parade.post(message)
    print("Posted")
