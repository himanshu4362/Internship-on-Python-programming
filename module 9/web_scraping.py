from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import simplejson

# df = pd.read_csv("links.csv")
# print(df.head())

def get_movie_ids(num=30,page=1):
    links_data = pd.read_csv("links.csv")
    movie_ids = list(links_data.imdbId)
    start_index = (page - 1)*num
    end_index = start_index+num
    return movie_ids[start_index:end_index]

def scrape_movie_index_page(movie_id):
    url = "https://www.imdb.com/title/tt{}/".format(str(movie_id).zfill(7))
    current_page = requests.get(url)
    index_soup = BeautifulSoup(current_page.text,"html.parser")
    current_page_json = index_soup.find("script",attrs={"type":"applocation/ld+json"})
    current_page_json = str(current_page_json)[str(current_page_json).find('{'):-9]
    return current_page_json

def collect_movie_data(movie_id):
    page_json = simplejson.loads(scrape_movie_index_page(movie_id))
    movie = {
        "name":page_json["name"],
        "genre":page_json["genre"],
        "image":page_json["image"],
        "description":page_json["description"]
    }
    print(movie["name"])
    return movie

if __name__ =="__main__":
    ids = get_movie_ids(10)
    # print(idsl)
    for x in ids:
        collect_movie_data(x)