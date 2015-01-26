import sys
import os
import argparse
import traceback
from os.path import join

import backends
import similar


def main(keyword, path):
    path = join(path, keyword)
    if not os.path.exists(path):
        os.makedirs(path)

    if not args.quiet:
        print('Downloading images with keyword "{keyword}" into "{path}"'
              ''.format(**locals())
        )

    # Download phase
    for module_name in backends.__all__:
        if args.backends != 'all' and module_name not in args.backends:
            continue
        if not args.quiet:
            print("Downloading from {module_name}".format(**locals()))
        module = getattr(backends, module_name)
        try:
            module.go(keyword, path)
        except Exception as e:
            print("Module {module_name} had exception:\n".format(**locals()))
            print(traceback.format_exc())
            print("Continuing with next backend...")

    # Cleanup phase
    if not args.no_cleanup:
        similar.cleanupPhase(args, path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Image DataSet Creator.",
    )
    parser.add_argument("keyword", help="Keyword to search")
    parser.add_argument("-q", "--quiet",
                        help="Decreases output verbosity",
                        action="store_true")
    parser.add_argument("--backends",
                        nargs='+',
                        default='all',
                        help="Backends to use")
    parser.add_argument("--no_cleanup",
                        help="Disables the cleanp phase",
                        action="store_true")
    args = parser.parse_args()

    main(args.keyword, 'images')
