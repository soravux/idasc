import os
from os.path import isfile, join
from subprocess import Popen, PIPE, CalledProcessError, check_output
from itertools import combinations
from multiprocessing import Pool, Lock
from functools  import partial

from progressbar import ProgressBar


def findAndDeleteSimilars(im1, im2, path):
    """Compares all images in path for identical files and removes them."""

    if not isfile(join(path, im1)) or not isfile(join(path, im2)) or im1 == im2:
        return

    # With resize (Slow!)
    #out, err = Popen("convert '{}' '{}' -resize '400x300!' MIFF:- | "
    #        "compare -metric AE -fuzz '10%' - null:".format(
    out, err = Popen("compare -metric AE -fuzz '10%' '{}' '{}' null:".format(
                join(path, im1),
                join(path, im2),
            ),
        shell=True, stdout=PIPE, stderr=PIPE
    ).communicate()

    try:
        error = int(err)
    except ValueError:
        #if not args.quiet:
        #    print("Could not find the similiarity between {im1} and {im2}".format(**locals()))
        return

    if error < 20:
        if not args.quiet:
            print("Deleting file {im2}, duplicate of {im1}".format(**locals()))
        try:
            os.remove(join(path, im2))
        except FileNotFoundError:
            pass


def updatePB(val):
    global nb_done
    lock.acquire()

    nb_done += 1
    progress.update(nb_done)

    lock.release()


def cleanupPhase(rcvargs, path):
    global args
    args = rcvargs

    if not args.quiet:
        print("Erasing identical images...")
    
    # Check if ImageMagick is in path
    try:
        output = check_output(["compare"])
    except CalledProcessError as e:
        if e.returncode == 127:
            print("Error: Could not find ImageMagic. Will not search identical images.")
            return

    pool = Pool()
    imgs = sorted(os.listdir(path))
    img_pairs = list(combinations(imgs, 2))
    func = partial(findAndDeleteSimilars, path=path)

    global progress, lock, nb_done
    lock = Lock()
    progress = ProgressBar(maxval=len(img_pairs)).start()
    nb_done = 0
    tasks = []

    for pair in img_pairs:
        tasks.append(pool.apply_async(func, pair, callback=updatePB))
    
    for task in tasks:
        task.get()
    progress.finish()
