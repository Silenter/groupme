from groupy.client import Client
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
shakes = open('corpora/shakespeare.txt','r')
groupme = Client.from_token(getenv('GROUPME_TOKEN'))
dingus_parade = [group for group in groupme.groups.list() if group.id=='19442193'][0]

for line in shakes:
    if line != "\n":
        dingus_parade.post(line)
        sleep(3)
