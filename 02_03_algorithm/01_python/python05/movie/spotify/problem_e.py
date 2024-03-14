import json
from pprint import pprint

def dec_artists(artists):
    idLst = []
    artist_result = []
    star_list = []
    for artist in artists:
        idLst.append(artist['id'])
    for id in idLst:
        artists_json = open(f"data/artists/{id}.json", encoding="utf-8")
        artists_detail = json.load(artists_json)  
        artist_result.append(artists_detail)
    for star in artist_result:
        star_dict = {}
        if star['followers']['total'] >= 10000000:
            star_dict['name'] = star['name']
            star_dict['uri-id'] = star['uri']
            star_list.append(star_dict)
    return star_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint(dec_artists(artists_list))
