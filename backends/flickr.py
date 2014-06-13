import time

from progressbar import ProgressBar

from .flickrpy import flickr
from .common.download import downloadImage
from ._config_parser import config


NB_IMAGES = config.get('flickr', 'NB_IMAGES')


def go(keyword, path):
    """Picasa fetcher"""
    photos = flickr.photos_search(
        tags=keyword,
        #tag_mode='all',
        per_page=NB_IMAGES,
    )
    progress = ProgressBar()
    for photo in progress(photos):
        #loc = photo.getLocation()
        #if loc:
        #    print("Photo {} has a location: {}".format(photo.title, loc))
        url = photo.getURL(size='Large', urlType='source')
        downloadImage(url, path)
