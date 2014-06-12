from io import BytesIO

import requests
from requests.exceptions import ConnectionError
from PIL import Image


def downloadImage(url, path):
    """
    Download image "url" in "path".

    TODO: other than JPEG
    TODO: if filename already exists?
    """
    try:
        image_r = requests.get(url)
    except ConnectionError as e:
        print('Could not download %s' % url)
        return

    # Remove file-system path characters from name.

    with open(path, 'wb') as fhdl:
        try:
            Image.open(BytesIO(image_r.content)).save(fhdl, 'JPEG')
        except IOError as e:
            # Throw away some gifs...blegh.
            print('Could not save {0}: {1}'.format(url, e))
