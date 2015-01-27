import json
import sys

import requests
from progressbar import ProgressBar

from .common.download import downloadImage
from ._config_parser import config


API_KEY = config.get('google', 'API_KEY')
NB_IMAGES = int(config.get('google', 'NB_IMAGES'))
cx = config.get('google', 'cx')

ROOT_URL = "https://www.googleapis.com/customsearch/v1?"
BASE_URL = (ROOT_URL + "cx={cx}&q={query}&searchType=image&key={API_KEY}&start={start}")


def performRequest(query, BASE_PATH, start):
    """
    Perform a JSON request to google images.
    API reference:
    http://developers.google.com/apis-explorer/
    """
    global img_done
    r = requests.get(BASE_URL.format(query=query, cx=cx, API_KEY=API_KEY, start=start))
    response = json.loads(r.text)

    if not 'items' in response.keys():
        raise ValueError('Could not find field "items" in:\n{}'.format(response))

    for image_info in response['items']:
        url = image_info['link']
        downloadImage(url, BASE_PATH)
        img_done += 1
        progress.update(img_done)

    return response['queries']['nextPage'][0]['count']

def go(query, path):
    """
    Download full size images from Google image search.
    """
    global progress, img_done
    progress = ProgressBar(maxval=NB_IMAGES).start()
    img_done = 0
    while img_done < NB_IMAGES:
        performRequest(query, path, img_done + 1)
    progress.finish()


if __name__ == '__main__':
    # Example use
    if len(sys.argv) < 2:
        print("Please specify a query")
    else:
        go(sys.argv[1], 'images')
