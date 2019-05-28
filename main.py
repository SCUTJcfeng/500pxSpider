# python 3.6

from bs4 import BeautifulSoup
from urllib.parse import unquote
from requests.exceptions import ReadTimeout
from api import PHOTO_URL, POPULAR_URL, FEATURE_LIST, CATEGORY_LIST
from common.http import HttpPool, HttpTool
from common.url import UrlTool
from common.base import create_folder, create_path, check_path
from common.save import SaveTool


base_dir = './pic'
start_page = 1
total_page = 1
pool = HttpPool(10)


def main():
    pool.start()
    create_folder(base_dir)
    html, status_code = HttpTool.get(POPULAR_URL, retFormat='text')
    headers = UrlTool.randomHeaders()
    headers['X-CSRF-Token'] = get_csrf_token(html)
    for feature in FEATURE_LIST:
        for category in CATEGORY_LIST:
            for i in range(start_page, total_page + 1):
                url = PHOTO_URL.format(feature, category, str(i))
                pool.http_get(url, callback=get_photo_url, headers=headers, retFormat='json')
    input()


def get_photo_url(req, res, status_code):
    if status_code == 200:
        for photo in res['photos']:
            image_info = photo['images'][-1]
            url = image_info['url']  # most high quality one
            name = photo['url'].split('/')[-1] + '.' + image_info['format']
            filename = create_path(base_dir, unquote(name))
            if not check_path(filename):
                pool.http_get(url, callback=save_photo, headers=UrlTool.randomHeaders(), retFormat='raw', local_data={'filename': filename})


def save_photo(req, res, status_code):
    try:
        url, callback, params, headers, retFormat, timeout, allow_redirects, local_data = req
        filename = local_data['filename']
        SaveTool.saveChunk(res, filename)
        print(f'{filename} save success')
        print(f'unfinished task {pool.count}')
    except ReadTimeout:
        pass


def get_csrf_token(html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find('meta', {'name': 'csrf-token'})
    return res.attrs['content']


if __name__ == "__main__":
    main()
