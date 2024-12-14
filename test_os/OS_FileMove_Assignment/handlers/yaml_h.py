import yaml
from eraser.erasefile import del_file
import logging as log
from pathlib import Path

src = ''

log_y = log.getLogger(Path(__file__).name)
def yaml_handler(func):
    try:
        def opener(filename,src_dir,dest_dir):
            try:
                global src
                src = src_dir
                with open(r'{}/{}'.format(src_dir,filename)) as fp:
                    log_y.info('{} is opened'.format(filename))
                    f_data = yaml.safe_load(fp)
                    log_y.info('{} was read completely'.format(filename))
                    del_file(fp.name)
                    log_y.info('{} is deleted'.format(filename))
                    log_y.info('{} will enter in {}'.format(filename, func))
                    func(f_data,dest_dir,filename)
                return True
            except Exception as error_msg:
                log_y.critical(f'Exception {error_msg} in yaml handling of file {filename}')
            finally:
                log_y.info(f'Processing {filename} is completed successfully')
                fp.close()
                log_y.info(f'Check file close status -- {fp.closed}')

        return opener
    except Exception as error_msg:
        log_y.critical(f'Exception in accessing opener -- {error_msg}')
