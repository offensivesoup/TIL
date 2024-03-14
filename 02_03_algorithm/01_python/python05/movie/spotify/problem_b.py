import json
from pprint import pprint


def artist_info(artist, genres):
    genreLst = []
    for genre in genres:
        for genre_id in artist['genres_ids']:
            if genre['id'] == genre_id:
                genreLst.append(genre['name'])
    artist['genres_names'] = artist.pop('genres_ids')
    artist['genres_names'] = genreLst
                
    return artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
