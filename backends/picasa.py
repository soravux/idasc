import os

import gdata.photos, gdata.photos.service

from common.download import downloadImage


def go(query, path):
    pws = gdata.photos.service.PhotosService()
    photos = pws.SearchCommunityPhotos(query, limit='10')
    for photo in photos.entry:
        url = photo.media.content[0].url,
        url = url[0].decode('ascii')
        #import pdb; pdb.set_trace()
        downloadImage(
            url,
            os.path.join(path, url.split("/")[-1]),
        )


if __name__ == '__main__':
    go('puppy', '')
