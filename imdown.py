import json
import os
import time
import sys
from PIL import Image
from io import BytesIO
from functools import partial

import requests
from requests.exceptions import ConnectionError

# Parallel processing
try:
    from scoop import futures
    parallel_map = futures.map
except ImportError:
    parallel_map = map


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
    print(BASE_URL.format(query=query, start=start), response)
    for image_info in response['responseData']['results']:
        url = image_info['unescapedUrl']
        try:
            image_r = requests.get(url)
        except ConnectionError as e:
            print('Could not download %s' % url)
            continue

        # Remove file-system path characters from name.
        title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')

        with open(os.path.join(BASE_PATH, '%s') % url.split("/")[-1], 'wb') as fhdl:
            try:
                Image.open(BytesIO(image_r.content)).save(fhdl, 'JPEG')
            except IOError as e:
                # Throw away some gifs...blegh.
                print('Could not save {0}: {1}'.format(url, e))
                continue

def go(query, path):
    """
    Download full size images from Google image search.
    """

    BASE_PATH = os.path.join(path, query)

    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    thisRequest = partial(performRequest, query, BASE_PATH)

    # Maximum 8 pages as written in the JSON dev guide of Google Image
    results = list(parallel_map(thisRequest, range(8)))

if __name__ == '__main__':
    # Example use
    if len(sys.argv) < 2:
        print("Please specify a query")
    else:
        go(sys.argv[1], 'images')
