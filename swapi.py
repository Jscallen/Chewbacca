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
def get_planets():
    planets_data = get_star_wars_data("planets")
    return planets_data['results']
def main_planets():
    planets = get_planets()
    df = pd.DataFrame(planets)
    print(df)
