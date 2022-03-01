import atexit

from .components import *
from .runs import *
from .sample_components import *
from .samples import *
from .species import *
from .utils import *
from .ssh_pymongo import *

atexit.register(close_all_connections)
