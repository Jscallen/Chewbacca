import requests
import pandas as pd

def get_star_wars_data(resource):
    base_url = "https://swapi.dev/api/"
    url = base_url + resource
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_starships():
    starships_data = get_star_wars_data("starships")
    return starships_data['results']

def main():
    starships = get_starships()
    df = pd.DataFrame(starships)
    print(df)

def get_star_wars_data_people(resource):
    base_url = "https://swapi.dev/api/"
    url = base_url + resource
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_people():
    people_data = get_star_wars_data_people("people")
    return people_data['results']

def main_people():
    people = get_people()
    df = pd.DataFrame(people)
    print(df)

main_people()
