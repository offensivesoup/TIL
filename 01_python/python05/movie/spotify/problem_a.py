import json
from pprint import pprint


def artist_info(artist):
    result = {}
    result['genres_ids'] = artist['genres_ids']
    result['id'] = artist['id']
    result['images'] = artist['images']
    result['name'] = artist['name']
    result['type'] = artist['type']
    # 여기에 코드를 작성합니다.
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
