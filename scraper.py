from bs4 import BeautifulSoup
import requests

def scrape_songs_and_artists(date):
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    soup = BeautifulSoup(response.text, "html.parser")

    titles = [(title.text[1:-1]) for title in soup.select("div ul li ul li h3")]
    artists = [(artist.text[1:-1]) for artist in soup.select("div ul li ul li span") if len(artist.text) > 4]
    return zip(titles, artists)
