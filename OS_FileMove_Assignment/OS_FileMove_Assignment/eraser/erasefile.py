from os import remove
import logging as log
from pathlib import Path
log_del = log.getLogger(Path(__file__).name)

def del_file(filepath):
    try:
        remove(filepath)
        log_del.info('{} is deleted'.format(filepath.split('/')[-1]))
    except Exception as error_msg:
        pass