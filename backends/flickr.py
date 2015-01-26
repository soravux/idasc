import time

from progressbar import ProgressBar

from .flickrpy import flickr
from .common.download import downloadImage
from ._config_parser import config


NB_IMAGES = config.get('flickr', 'NB_IMAGES')


def go(keyword, path):
    """Picasa fetcher"""
    keyword = keyword.replace(' ', ',')
    print(keyword)
    photos = flickr.photos_search(
        content_type=1,
        tags=keyword,
        tag_mode='all',
        per_page=NB_IMAGES,
        page=1,
    )
    print(len(photos))
    progress = ProgressBar()
    for photo in progress(photos):
        #loc = photo.getLocation()
        #if loc:
        #    print("Photo {} has a location: {}".format(photo.title, loc))
        try:
            url = photo.getURL(size='Large', urlType='source')
        except flickr.FlickrError:
            pass
        downloadImage(url, path)
