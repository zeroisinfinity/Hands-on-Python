from eraser.erasefile import del_file
import logging as log
from pathlib import Path

src = ''

log_t = log.getLogger(Path(__file__).name)
def txt_handler(func):
    try:
        def opener(filename,src_dir,dest_dir):
            try:
                global src
                src = src_dir
                with open(r'{}/{}'.format(src_dir,filename)) as fp:
                    log_t.info('{} is opened'.format(filename))
                    f_data = fp.read()
                    log_t.info('{} was read completely'.format(filename))
                    del_file(fp.name)
                    log_t.info('{} is deleted'.format(filename))
                    log_t.info('{} will enter in {}'.format(filename,func))
                    func(f_data, dest_dir,filename)
                return True
            except Exception as error_msg:
                log_t.critical(f'Exception {error_msg} in text handling of file {filename}')
            finally:
                log_t.info(f'Processing {filename} is completed successfully')
                fp.close()
                log_t.info(f'Check file close status -- {fp.closed}')

        return opener
    except Exception as error_msg:
        log_t.critical(f'Exception in accessing opener -- {error_msg}')



