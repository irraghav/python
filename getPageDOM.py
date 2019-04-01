from lxml import html
import requests

def getRequests(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree