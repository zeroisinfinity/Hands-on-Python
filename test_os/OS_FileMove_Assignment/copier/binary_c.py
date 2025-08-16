from handlers.binary_h import binary_handler
import logging as log
from pathlib import Path

log_bc = log.getLogger(Path(__file__).name)

@binary_handler
def binary_copier(text,dest_dir,filename):
    try:
        with open(r'{}/{}'.format(dest_dir,filename),'wb') as fp:
            log_bc.info('File {} is opened for writing'.format(filename.split('/')[-1]))
            fp.write(text)
            log_bc.info('File {} is written successfully'.format(filename.split('/')[-1]))
        return True
    except Exception as error_msg:
        log_bc.critical('INTERUPPTION in reading binary file {} due to {}'.format(filename,error_msg))
    finally:
        fp.close()
        log_bc.debug(f'File is safely closed now -- check file status {fp.closed}')

