import json
from urllib.request import urlopen

from ioiprint import CONTESTANT_DATA_ADDRESS_URL,WEBSERVICE_URL


def get_contestant_data(ip):
    url_address = CONTESTANT_DATA_ADDRESS_URL.format(ip=ip)
    data = json.loads(urlopen(url_address).read().decode('utf-8'))

    return {
        'contestant_id': data['login'],
        'contestant_name': data['name'] + ' ' + data['surname'],
        'zone': data['seat'][:1],
        'desk_id': data['seat'][1:],
        'desk_image_url': 'http://' + WEBSERVICE_URL + '/images/' +data['seat'][:1]+'.png'
    }
