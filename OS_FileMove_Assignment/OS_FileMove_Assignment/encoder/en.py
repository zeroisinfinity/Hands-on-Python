from charset_normalizer import from_bytes
import logging as log
from pathlib import Path

log_en = log.getLogger(Path(__file__).name)
def encode(fp_name):
    try:
        with open(fp_name, 'rb') as fp:
            log_en.info('{} HAS ENTERED FOR TESTING OF ENCODING'.format(fp_name.split('/')[-1]))
            code = from_bytes(fp.read()).best()
        return code.encoding
    except Exception as error_msg:
        log_en.critical('Exception {} found in encode verifier func '.format(error_msg))


