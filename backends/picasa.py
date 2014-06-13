import os

import gdata.photos, gdata.photos.service
from progressbar import ProgressBar

from .common.download import downloadImage
from ._config_parser import config


NB_IMAGES = config.get('picasa', 'NB_IMAGES')

def go(query, path):
    pws = gdata.photos.service.PhotosService()
    photos = pws.SearchCommunityPhotos(query, limit=str(NB_IMAGES))
    progress = ProgressBar()
    for photo in progress(photos.entry):
        url = photo.media.content[0].url,
        url = url[0].decode('ascii')
        downloadImage(
            url,
            path,
        )


if __name__ == '__main__':
    go('puppy', '')
