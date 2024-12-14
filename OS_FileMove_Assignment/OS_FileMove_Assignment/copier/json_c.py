import json

from handlers.json_h import json_handler , src
from copier.binary_c import binary_copier
import logging as log
from pathlib import Path
from encoder.encodings_list import PRIOR_LIST
from encoder.en import encode
PRIOR_LIST = PRIOR_LIST
recur_track = 0

log_jc = log.getLogger(Path(__file__).name)
@json_handler
def json_copier(json_data, dest_dir, filename, def_endcode ='utf-8'):
    try:
        global recur_track
    except Exception:
        log_jc.error('Unexpected error in setting a global variable')
    try:
        with open(r'{}/{}'.format(dest_dir,filename),'w', encoding=def_endcode) as fp:
            log_jc.info('File {} is opened for writing'.format(filename.split('/')[-1]))

            json.dump(json_data,fp,indent=4)
            log_jc.info('File {} is written successfully'.format(filename.split('/')[-1]))

        return True
    except UnicodeDecodeError:
        if PRIOR_LIST:
            next_code = encode(fp.name)
            PRIOR_LIST.remove(next_code)
            log_jc.warning("unicode {} doesn't match trying for {} ".format('utf-8', next_code))
            try:
                log_jc.info(
                    'Entered for recursive encode checking of {} with respect to encode {}'.format(filename, next_code))
                recur_track += 1
                json_copier(json_data, dest_dir, filename, encode=next_code)
            except Exception as error_msg:
                log_jc.critical('Exception in {}{} recursive call for correcting encoding'.format(recur_track,
                                                                                                  'st' if str(recur_track)[-1] == '1'
                                                                                                   else 'nd' if str(recur_track)[-1] == '2'
                                                                                                  else 'rd' if str(recur_track)[-1] == '3'
                                                                                                  else 'th'))
        else:
            log_jc.warning('Completely different unicode used in {}'.format(filename))
            try:
                binary_copier(filename, src, dest_dir)
            except:
                raise Exception(UnicodeDecodeError)
    except Exception as error_msg:
            log_jc.critical('Exception occurred in opening json file {}'.format(filename))
    finally:
        fp.close()
        log_jc.debug(f'File is safely closed now -- check file status {fp.closed}')



