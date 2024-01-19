"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)
    idLst = []
    artist_result = []
    star_list = []
    for artist in artists_list:
        idLst.append(artist['id'])
    for id in idLst:
        artists_json = open(f"data/artists/{id}.json", encoding="utf-8")
        artists_detail = json.load(artists_json)  
        artist_result.append(artists_detail)
    for star in artist_result:
        star_dict = {}
        if 5000000 <= star['followers']['total'] < 10000000:
            star_dict['followers'] = star['followers']['total']
            star_dict['name'] = star['name']
            star_list.append(star_dict)
    return star_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
