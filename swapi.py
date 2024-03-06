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

def get_star_wars_data_vehicles(resource):
def get_star_wars_data_people(resource):
    base_url = "https://swapi.dev/api/"
    url = base_url + resource
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_vehicles():
    vehicles_data = get_star_wars_data_vehicles("vehicles")
    return vehicles_data['results']

def main_vehicles():
    vehicles = get_vehicles()
    df = pd.DataFrame(vehicles)
    print(df)

def get_people():
    people_data = get_star_wars_data_people("people")
    return people_data['results']

def main_people():
    people = get_people()
    df = pd.DataFrame(people)
    print(df)

def get_star_wars_data_vehicles(resource):
    base_url = "https://swapi.dev/api/"
    url = base_url + resource
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_vehicles():
    vehicles_data = get_star_wars_data_vehicles("vehicles")
    return vehicles_data['results']

def main_vehicles():
    vehicles = get_vehicles()
    df = pd.DataFrame(vehicles)
    print(df)

def get_star_wars_data(resource):
    base_url = "https://swapi.dev/api/"
    url = base_url + resource
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_planets():
    planets_data = get_star_wars_data("planets")
    return planets_data['results']

def main_planets():
    planets = get_planets()
    df = pd.DataFrame(planets)
    print(df)
