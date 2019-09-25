# Logging levels are:
# debug, info, warning, error, critical
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from terp.classes import info


logging.basicConfig(
    format="%(module)12s:%(levelname)s %(message)s",
    datefmt='%H:%M:%S',
    level=logging.INFO
)

formatter = logging.Formatter('%(module)12s:%(levelname)s %(message)s')

log = logging.getLogger('terp')
log.setLevel(logging.INFO)

fh = RotatingFileHandler(
    os.path.join(info.USER_PATH, 'openshot-qt.log'),
    encoding="utf-8",
    maxBytes=25*1024*1024,
    backupCount=3
)

fh.setFormatter(formatter)
log.addHandler(fh)
