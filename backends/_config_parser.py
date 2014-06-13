import configparser


# Setup configuration parser
config = configparser.SafeConfigParser({
    'NB_IMAGES': 100,
    'delay': 1,
})
config.optionxform=str # Keep case
config.read("config.ini")
