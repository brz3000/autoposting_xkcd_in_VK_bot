import os
from dotenv import load_dotenv
import requests
import random


def get_comic_book(url):
    response = requests.get(url)
    response.raise_for_status()
    comic_book = response.json()
    comment = comic_book['alt']
    image_url = comic_book['img']
    response = requests.get(image_url)
    response.raise_for_status()
    with open('image.png', 'wb') as file:
        file.write(response.content)
    return comment


def get_server_address(token, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {'v': '5.131',
              'access_token': token,
              'group_id': group_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_photo(token, group_id):
    with open('image.png', 'rb') as file:
        url = get_server_address(token, group_id)
        files = {"file1": file}
        response = requests.post(url, files=files)
    response.raise_for_status()
    photo_payload = response.json()
    server = photo_payload['server']
    photo = photo_payload['photo']
    hash_parameter = photo_payload['hash']
    return server, photo, hash_parameter


def save_comic_book(token, group_id):
    server, photo, hash_parameter = upload_photo(token, group_id)
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {'server': server,
              'photo': photo,
              'hash': hash_parameter,
              'group_id': group_id,
              'access_token': token,
              'v': '5.131'
              }
    response = requests.post(url, params=params)
    response.raise_for_status()
    save_wall_photo_payload = response.json()
    owner_id = save_wall_photo_payload['response'][0]['owner_id']
    media_id = save_wall_photo_payload['response'][0]['id']
    return f'photo{owner_id}_{media_id}'


def post_comic_book(token, group_id, comment):
    url = 'https://api.vk.com/method/wall.post'
    params = {'v': '5.131',
              'access_token': token,
              'group_id': group_id,
              'owner_id': f'-{group_id}',
              'from_group': 0,
              'attachments': save_comic_book(token, group_id),
              'message': comment}
    response = requests.post(url, params=params)
    response.raise_for_status()


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN_ID']
    group_id = os.environ['VK_GROUP_ID']
    random_number = random.randrange(1, 2808, 1)
    url = f'https://xkcd.com/{random_number}/info.0.json'
    post_comic_book(token, group_id, get_comic_book(url))
    try:
        os.remove('image.png')
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    main()
