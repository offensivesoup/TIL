import json
from pprint import pprint


def artist_info(artists, genres):
    result = []
    for artist in artists:
        genreLst = []
        new_artist = {}
        for genre in genres:
            for genre_id in artist['genres_ids']:
                if genre['id'] == genre_id:
                    genreLst.append(genre['name'])
        artist['genres_names'] = artist.pop('genres_ids')
        artist['genres_names'] = genreLst
    for info in artists:
        new_artist['genres_names'] = info['genres_names']
        new_artist['id'] = info['id']
        new_artist['images'] = info['images']
        new_artist['name'] = info['name']
        new_artist['type'] = info['type']
        result.append(new_artist)
    return result
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
