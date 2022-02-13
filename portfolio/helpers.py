import requests
import string
import random
from .settings import BASE_DIR
import os


def get_random_text():
    '''
    https://www.boredapi.com/documentation
    '''

    types = ["education", "recreational", "busywork"]
    type = random.choice(types)

    if type:
        url = "http://www.boredapi.com/api/activity/"+f"?{type}"
    else:
        url = "http://www.boredapi.com/api/activity/"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()["activity"]


def random_advise():
    import requests

    url = "https://api.adviceslip.com/advice"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()["slip"]["advice"]


def random_affirmation():
    url = "https://www.affirmations.dev/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()["affirmation"]


def random_pixart(size=6, chars=string.ascii_uppercase + string.digits):
    size = random.randint(5,20)
    string = ''.join(random.choice(chars) for _ in range(size))

    url = f"https://avatars.dicebear.com/api/personas/{string}.svg"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    path = os.path.join(BASE_DIR, 'static', 'favicon.svg')
    open(path, 'wb').write(response.content)

    path = os.path.join(BASE_DIR, 'portfolio', 'static', 'favicon.svg')
    open(path, 'wb').write(response.content)

    return True

