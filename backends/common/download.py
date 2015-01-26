from io import BytesIO
import string
import time
import shutil
import os
import urllib
from urllib import request

from .._config_parser import config


def downloadImage(url, path):
    """
    Download image "url" in "path".
    Appends a _X before the extension if filename already exists
    (and increments X).
    Will try multiple times the download.
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    output_filename = os.path.join(
        path,
        ''.join(c for c in url.split("/")[-1] if c in valid_chars),
    )
    original_output_filename = output_filename.rsplit(".", maxsplit=1)
    counter = 1
    while os.path.isfile(output_filename):
        output_filename = "".join([
            original_output_filename[0],
            '_',
            str(counter),
            '.',
            original_output_filename[1],
        ])
        counter += 1

    for _ in range(5):
        try:
            filename, mime = request.urlretrieve(url)
            shutil.move(filename, output_filename)
        except urllib.error.HTTPError:
            # Error while downloading file.
            time.sleep(int(config.get('general', 'delay')))
        except urllib.error.URLError:
            print("Timeout Error")
            break
        except TimeoutError:
            print("Timeout Error")
            break 
        else:
            break
    else:
        print("Could not download url: ", url)
