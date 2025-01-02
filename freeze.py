import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from pallets import app
from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()