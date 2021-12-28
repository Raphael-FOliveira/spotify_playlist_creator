from spotify_authorizer import spotify, user_id
from scraper import scrape_songs_and_artists


def find_songs(title_artist_zip):
    uri_list = []
    for title in title_artist_zip:
        search_result = spotify.search(q=f"{title[0]} {title[1]}")
        try:
            song_uri = search_result["tracks"]["items"][0]["uri"]
            uri_list.append(song_uri)
            print(song_uri)
        except IndexError:
            pass
    return uri_list


def create_new_playlist_and_add_songs(user_id, date):
    new_playlist = spotify.user_playlist_create(user_id, date)
    uri_list = find_songs(scrape_songs_and_artists(date))
    new_list_id = spotify.user_playlists(user_id)["items"][0]["id"]
    spotify.user_playlist_add_tracks(user=user_id, playlist_id=new_list_id, tracks=uri_list)
    return new_playlist


create_new_playlist_and_add_songs(user_id, input("date(yyyy-mm-dd): "))
