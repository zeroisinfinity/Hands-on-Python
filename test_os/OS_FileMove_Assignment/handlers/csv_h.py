import csv
import logging as log
from pathlib import Path
from src_keeper import src


log_c = log.getLogger(Path(__file__).name)
def csv_handler(func):
    try:
        def opener(filename,src_dir,dest_dir,def_encode ='utf-8'):
            try:
                global src
                src = src_dir
                print(r'{}/{}'.format(src_dir,filename))
                with open(r'{}/{}'.format(src_dir,filename),encoding=def_encode) as fp:
                    log_c.info('{} is opened'.format(filename))
                    iter_obj = csv.DictReader(fp)
                    log_c.info('{} was read completely'.format(filename))
                    log_c.info('{} will enter in {}'.format(filename, func))
                    func(iter_obj, src_dir , dest_dir,filename)
                return True
            except Exception as error_msg:
                log_c.critical(f'Exception {error_msg} in csv handling of file {filename}')
            finally:
                log_c.info(f'Processing {filename} is completed successfully')
                fp.close()
                log_c.info(f'Check file close status -- {fp.closed}')

        return opener

    except Exception as error_msg:
        log_c.critical(f'Exception in accessing opener -- {error_msg}')