import sys

import backends


def main(keyword, path):
    import pdb
    pdb.set_trace()

if __name__ == '__main__':
    # Example use
    if len(sys.argv) < 2:
        print("Please specify a query")
    else:
        main(sys.argv[1], 'images')
