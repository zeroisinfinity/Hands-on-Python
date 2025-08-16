import json
from eraser.erasefile import del_file
import logging as log
from pathlib import Path

src = ''

log_j = log.getLogger(Path(__file__).name)
def json_handler(func):
    try:
        def opener(filename,src_dir,dest_dir):
            try:
                global src

                src = src_dir
                with open(r'{}/{}'.format(src_dir,filename)) as fp:
                    log_j.info('{} is opened'.format(filename))
                    f_data = json.load(fp)
                    log_j.info('{} was read completely'.format(filename))
                    del_file(fp.name)
                    log_j.info('{} is deleted'.format(filename))
                    log_j.info('{} will enter in {}'.format(filename, func))
                    func(f_data,dest_dir,filename)
                return True
            except Exception as error_msg:
                log_j.critical(f'Exception {error_msg} in json handling of file {filename}')
            finally:
                log_j.info(f'Processing {filename} is completed successfully')
                fp.close()
                log_j.info(f'Check file close status -- {fp.closed}')

        return opener
    except Exception as error_msg:
        log_j.critical(f'Exception in accessing opener -- {error_msg}')

