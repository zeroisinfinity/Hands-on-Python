from eraser.erasefile import del_file
import logging as log
from pathlib import Path

log_b = log.getLogger(Path(__file__).name)
def binary_handler(func):
    try:
        def opener(filename,src_dir,dest_dir):
            try:
                with open(r'{}/{}'.format(src_dir,filename),'rb') as fp:
                    log_b.info('{} is opened'.format(filename))
                    f_data = fp.read()
                    log_b.info('{} was read completely'.format(filename))
                    del_file(fp.name)
                    log_b.info('{} is deleted'.format(filename))
                    log_b.info('{} will enter in {}'.format(filename, func))
                    func(f_data, dest_dir,filename)
                return True
            except Exception as error_msg:
                log_b.critical(f'Exception {error_msg} in binary handling of file {filename}')
            finally:
                log_b.info(f'Processing {filename} is completed successfully')
                fp.close()
                log_b.info(f'Check file close status -- {fp.closed}')
        return opener
    except Exception as error_msg:
        log_b.critical(f'Exception in accessing opener -- {error_msg}')



