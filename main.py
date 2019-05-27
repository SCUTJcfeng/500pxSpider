# python 3.6

from bs4 import BeautifulSoup
from api import PHOTO_URL, POPULAR_URL
from common.http import HttpTool
from common.url import UrlTool
from common.base import create_folder, create_path, check_path
from common.save import SaveTool


base_dir = './pic'


def main():
    create_folder(base_dir)
    html, status_code = HttpTool.get(POPULAR_URL, retFormat='text')
    headers = UrlTool.randomHeaders()
    headers['X-CSRF-Token'] = get_csrf_token(html)
    data, status_code = HttpTool.get(PHOTO_URL, headers=headers, retFormat='json')
    for photo in data['photos']:
        image_info = photo['images'][-1]
        url = image_info['url']  # most high quality one
        name = photo['url'].split('/')[-1] + '.' + image_info['format']
        filename = create_path(base_dir, name)
        if not check_path(filename):
            download_photo(url, filename)


def download_photo(url, filename):
    r, status_code = HttpTool.get(url, headers=UrlTool.randomHeaders(), retFormat='raw')
    try:
        SaveTool.saveChunk(r, filename)
        print(f'{filename} save success')
    except:
        pass


def get_csrf_token(html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find('meta', {'name': 'csrf-token'})
    return res.attrs['content']


if __name__ == "__main__":
    main()
