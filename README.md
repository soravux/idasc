Image DataSet Creator
=====================

This project aggregates every image it can find based on a keyword search among
multiple data sources such as google images, bing images, picasa, flickr, etc.

Features
--------

* Can create datasets for research purposes in matter of minutes
* Easy to add backends
* Automatically prune duplicates (currently being developed)


Installation
------------

    git clone https://github.com/soravux/idasc.git
    cd idasc
    cp config.ini.dist config.ini
    nano config.ini


Usage
-----

    python imdasc.py [keyword]
    python imdasc.py --help


Adding a backend
~~~~~~~~~~~~~~~~

Just create a new python module in the `backends` directory containing a
`go(keyword, path)` function. This function will receive the keyword entered
by the user and the path where it should download its images. Most backends are
similar and thus could be copied over another similar backend and modified. 

