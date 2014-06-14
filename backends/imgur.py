import json

import requests
from progressbar import ProgressBar

from .common.download import downloadImage
from ._config_parser import config


BASE_URL = "https://api.imgur.com/3/gallery/search/time/{page}?q={query}"

NB_IMAGES = int(config.get('imgur', 'NB_IMAGES'))
API_KEY = config.get('imgur', 'API_KEY')


def go(query, path):
    """
    Perform a JSON request to imgur.
    API reference:
    https://api.imgur.com/
    """
    progress = ProgressBar(maxval=NB_IMAGES).start()
    page = 0
    images_done = 0
    while images_done < NB_IMAGES:
        # Perform the search request
        r = requests.get(
            BASE_URL.format(query=query, page=page),
            headers={"Authorization": "Client-ID {API_KEY}".format(API_KEY=API_KEY)},
        )
        response = json.loads(r.text)

        # Parse the results and download the images
        for image_info in response['data']:
            url = image_info['link']
            downloadImage(url, path)
            images_done += 1
            progress.update(images_done)
            if images_done >= NB_IMAGES:
                break
        page += 1
    progress.finish()

