import os
import glob
import importlib
import traceback


# Imports every module in this directory
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules if not os.path.basename(f).startswith('_')]

for module in __all__:
    try:
        importlib.import_module(".{module}".format(**locals()), 'backends')
    except Exception as e:
        print("Could not load the {module} module. Traceback:".format(**locals()))
        print(traceback.format_exc())
        print("Continuing with next module...")

