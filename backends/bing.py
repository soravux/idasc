import json
import base64

import requests
from progressbar import ProgressBar

from .common.download import downloadImage
from ._config_parser import config


BASE_URL = ("https://api.datamarket.azure.com/Bing/Search/Image?$format=json&"
           "Query=%27{query}%27")

NB_IMAGES = int(config.get('bing', 'NB_IMAGES'))
ACCOUNT_KEY = config.get('bing', 'ACCOUNT_KEY')
AUTH = base64.b64encode(bytes("{ACCOUNT_KEY}:{ACCOUNT_KEY}".format(**locals()), "utf-8")).decode("utf-8")


def go(query, path):
    """
    Perform a request to Bing.
    """
    progress = ProgressBar(maxval=NB_IMAGES).start()
    images_done = 0
    URI = BASE_URL.format(query=query)
    while images_done < NB_IMAGES:
        # Perform the search request
        r = requests.get(
            URI,
            headers={"Authorization": "Basic {AUTH}".format(AUTH=AUTH)},
        )
        response = json.loads(r.text)

        # Parse the results and download the images
        for image_info in response['d']['results']:
            url = image_info['MediaUrl']
            downloadImage(url, path)
            images_done += 1
            progress.update(images_done)
            if images_done >= NB_IMAGES:
                break
        # Get the link to the next page of results.
        # format must be appended, otherwise the default xml is returned
        URI = response['d']['__next'] + "&$format=json"
    progress.finish()


if __name__ == '__main__':
    go('puppies', '.')
