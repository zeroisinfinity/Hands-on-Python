import pickle
from eraser.erasefile import del_file
import logging as log
from pathlib import Path

log_p = log.getLogger(Path(__file__).name)
def pickle_handler(func):
    try:
        def opener(filename,src_dir,dest_dir):
            try:
                with open(r'{}/{}'.format(src_dir,filename),'rb') as fp:
                    log_p.info('{} is opened'.format(filename))
                    f_data = pickle.load(fp)
                    log_p.info('{} was read completely'.format(filename))
                    del_file(fp.name)
                    log_p.info('{} is deleted'.format(filename))
                    log_p.info('{} will enter in {}'.format(filename, func))
                    func(f_data,dest_dir,filename)
                return True
            except Exception as error_msg:
                    log_p.critical(f'Exception {error_msg} in pickle handling of file {filename}')
            finally:
                log_p.info(f'Procossing {filename} is completed successfully')
                fp.close()
                log_p.info(f'Check file close status -- {fp.closed}')

        return opener
    except Exception as error_msg:
        log_p.critical(f'Exception in accessing opener -- {error_msg}')
