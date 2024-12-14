import yaml
from handlers.yaml_h import yaml_handler , src
from copier.binary_c import binary_copier
from encoder.en import encode
import logging as log
from pathlib import Path
from encoder.encodings_list import PRIOR_LIST
PRIOR_LIST = PRIOR_LIST
log_yc = log.getLogger(Path(__file__).name)

@yaml_handler
def yaml_copier(yaml_data, dest_dir, filename):
    try:
        global recur_track
        recur_track = 0
    except Exception:
        log_yc.error('Unexpected error in setting a global variable')
    try:
        with open(r'{}/{}'.format(dest_dir,filename),'w') as fp:
            log_yc.info('File {} is opened for writing'.format(filename.split('/')[-1]))

            yaml.dump(yaml_data, fp)
            log_yc.info('File {} is written successfully'.format(filename.split('/')[-1]))

        return True
    except UnicodeDecodeError:
        if PRIOR_LIST:
            next_code = encode(fp.name)
            PRIOR_LIST.remove(next_code)
            log_yc.warning("unicode {} doesn't match trying for {} ".format('utf-8', next_code))
            try:
                log_yc.info(
                    'Entered for recursive encode checking of {} with respect to encode {}'.format(filename, next_code))
                recur_track += 1
                yaml_copier(yaml_data, dest_dir, filename, encode=next_code)
            except Exception as error_msg:
                log_yc.critical('Exception in {}{} recursive call for correcting encoding'.format(recur_track,
                                                                                                  'st' if str(recur_track)[-1] == '1'
                                                                                                   else 'nd' if str(recur_track)[-1] == '2'
                                                                                                  else 'rd' if str(recur_track)[-1] == '3'
                                                                                                  else 'th'))
        else:
            log_yc.warning('Completely different unicode used in {}'.format(filename))
            try:
                binary_copier(filename, src, dest_dir)
            except:
                raise Exception(UnicodeDecodeError)
    except Exception as error_msg:
        log_yc.critical('Exception occurred in opening yaml file {}'.format(filename))
    finally:
        fp.close()
        log_yc.debug(f'File is safely closed now -- check file status {fp.closed}')

