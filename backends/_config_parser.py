import configparser


# Setup configuration parser
config = configparser.SafeConfigParser({
    'NB_IMAGES': 100,
    'delay': 1,
})
config.optionxform=str # Keep case
config.read("config.ini")

try:
    delay = int(config.get('general', 'delay'))
except:
    raise Exception("Please insert a delay in the section 'general' of your "
                    "config.ini")
