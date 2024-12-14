from handlers.txt_h import txt_handler , src
from copier.binary_c import binary_copier
from encoder.en import encode
import logging as log
from pathlib import Path
from encoder.encodings_list import PRIOR_LIST
PRIOR_LIST = PRIOR_LIST
recur_track = 0

log_tc = log.getLogger(Path(__file__).name)
@txt_handler
def txt_copier(text,dest_dir,filename,def_encode = 'utf-8'):
    try:
        global recur_track
    except Exception:
        log_tc.error('Unexpected error in setting a global variable')
    try:
        with open(r'{}/{}'.format(dest_dir,filename),'w',encoding=def_encode) as fp:
            log_tc.info('File {} is opened for writing'.format(filename.split('/')[-1]))

            fp.write(text)
            log_tc.info('File {} is written successfully'.format(filename.split('/')[-1]))

        return True
    except UnicodeDecodeError:
        if PRIOR_LIST:
            next_code = encode(fp.name)
            PRIOR_LIST.remove(next_code)
            log_tc.warning("unicode {} doesn't match trying for {} ".format('utf-8', next_code))
            try:
                log_tc.info(
                    'Entered for recursive encode checking of {} with respect to encode {}'.format(filename, next_code))
                recur_track += 1
                txt_copier(text, dest_dir, filename, def_encode=next_code)
            except Exception as error_msg:
                log_tc.critical('Exception in {}{} recursive call for correcting encoding'.format(recur_track,
                                                                                                  'st' if
                                                                                                  str(recur_track)[
                                                                                                      -1] == '1'
                                                                                                  else 'nd' if
                                                                                                  str(recur_track)[
                                                                                                      -1] == '2'
                                                                                                  else 'rd' if
                                                                                                  str(recur_track)[
                                                                                                      -1] == '3'
                                                                                                  else 'th'))
        else:
            log_tc.warning('Completely different unicode used in {}'.format(filename))
            try:
                binary_copier(filename, src, dest_dir)
            except:
                raise Exception(UnicodeDecodeError)
    except Exception as error_msg:
        log_tc.critical('Unexpected error {} while writing txt file {}'.format(error_msg,filename))
    finally:
        fp.close()
        log_tc.debug(f'File is safely closed now -- check file status {fp.closed}')

