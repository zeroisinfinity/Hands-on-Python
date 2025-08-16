import pickle
from handlers.pickle_h import pickle_handler
import logging as log
from pathlib import Path

log_pc = log.getLogger(Path(__file__).name)

@pickle_handler
def pickle_copier(binary_data , dest_dir ,filename):
    try:
        with open(r'{}/{}'.format(dest_dir,filename),'wb') as fp:
            log_pc.info('File {} is opened for writing'.format(filename.split('/')[-1]))

            pickle.dump(binary_data,fp)
            log_pc.info('File {} is written successfully'.format(filename.split('/')[-1]))

        return True
    except Exception as e:
        print(e)
    finally:
        fp.close()
        log_pc.debug(f'File is safely closed now -- check file status {fp.closed}')


