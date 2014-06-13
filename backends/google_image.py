import json
import os
import time
import sys
from functools import partial

import requests
from progressbar import ProgressBar

from .common.download import downloadImage


# TODO: This API is deprecated and limited to 8 pages.
# Use customsearch API instead
BASE_URL = ("https://ajax.googleapis.com/ajax/services/search/images"
            "?v=1.0&q={query}&start={start}")


def performRequest(query, BASE_PATH, start):
    """
    Perform a JSON request to google images.
    API reference:
    https://developers.google.com/image-search/v1/jsondevguide
    """
    r = requests.get(BASE_URL.format(query=query, start=start))
    response = json.loads(r.text)
    for image_info in response['responseData']['results']:
        url = image_info['unescapedUrl']
        downloadImage(url, BASE_PATH)

def go(query, path):
    """
    Download full size images from Google image search.
    """
    thisRequest = partial(performRequest, query, path)

    # Maximum 8 pages as written in the JSON dev guide of Google Image
    progress = ProgressBar()
    for i in progress(range(8)):
        thisRequest(i)

if __name__ == '__main__':
    # Example use
    if len(sys.argv) < 2:
        print("Please specify a query")
    else:
        go(sys.argv[1], 'images')
