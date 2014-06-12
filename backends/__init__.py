# Imports every module in this directory
import os
import glob
import importlib
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules if not os.path.basename(f).startswith('_')]

for module in __all__:
    importlib.import_module(".{module}".format(**locals()), 'backends')
    #__import__(".{}".format(module), locals(), globals())
