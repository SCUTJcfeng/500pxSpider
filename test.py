# python 3.6

import time
from api import PHOTO_URL, POPULAR_URL
from common.http import HttpTool
from common.url import UrlTool
from common.base import create_folder
from main import get_csrf_token, get_photo_url, save_photo, pool, base_dir, start_page, total_page


def test():
    FEATURE_LIST = ['popular']
    CATEGORY_LIST = ['Celebrities']
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
    while pool.count > 0:
        time.sleep(5)
    print('test finish')


if __name__ == "__main__":
    test()
