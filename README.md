Image DataSet Creator
=====================

This project aggregates every image it can find based on a keyword search among
multiple data sources such as google images, picasa, flickr, etc.

Installation
------------

    git clone https://github.com/soravux/idasc.git
    cd idasc
    cp config.ini.dist config.ini
    nano config.ini

Getting keys
------------

Bing: http://www.bing.com/dev/en-us/dev-center
imgur: https://imgur.com/account/settings/apps
flickr: https://www.flickr.com/services/apps/create/

Usage
-----

    python imdasc.py [keyword]
    python imdasc.py --help
