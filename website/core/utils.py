import requests


def downloadImage(image_link):

    r = requests.get(image_link)
    return r.text


