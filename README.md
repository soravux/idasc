Image DataSet Creator
=====================

This project aggregates every image it can find based on a keyword search among
multiple data sources such as google images, picasa, flickr, etc.

Installation
------------

Please ensure that Python 3 is installed before proceeding. We highly
recommend using a virtual environment (which can be installed using 
`pip install virtualenv`).

    git clone https://github.com/soravux/idasc.git
    cd idasc
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp config.ini.dist config.ini
    nano config.ini

Getting keys
------------

Bing
~~~~
http://www.bing.com/dev/en-us/dev-center

imgur
~~~~~
https://imgur.com/account/settings/apps

flickr
~~~~~~
https://www.flickr.com/services/apps/create/

Usage
-----

    python idasc.py [keyword]
    python idasc.py --help
