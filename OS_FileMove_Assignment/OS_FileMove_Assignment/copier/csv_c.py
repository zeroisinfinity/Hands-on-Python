import csv
from eraser.erasefile import del_file
from encoder.en import encode
from copier.binary_c import binary_copier
from encoder.encodings_list import PRIOR_LIST
from handlers.csv_h import csv_handler , src
import logging as log
from pathlib import Path

log_cc = log.getLogger(Path(__file__).name)
recur_track = 0
uni_iter = 0
print(src)

@csv_handler
def csv_copier(csv_data, src_dir , dest_dir, filename):
    try:
        global recur_track
        print(r'{}/{}'.format(dest_dir,filename))
        with open(r'{}/{}'.format(dest_dir,filename),'w', encoding='utf-8') as fp:
            header , *rest = csv_data
            log_cc.info('csv data is ready')
            w_obj = csv.DictWriter(fp,fieldnames=list(header.keys()))
            w_obj.writeheader()
            log_cc.info('Header {} is written'.format(list(header.keys())))
            w_obj.writerow(header)
            w_obj.writerows(rest)
            log_cc.info('All rows in csv {} is written'.format(filename.split('/')[-1]))
            del_file(r'{}/{}'.format(src_dir,filename))
            log_cc.info('{} is deleted'.format(filename))
        return True
    except UnicodeDecodeError:
        global uni_iter
        while uni_iter < len(PRIOR_LIST):
            if not recur_track:
                next_code  = encode(r'{}/{}'.format(dest_dir,filename))
                if next_code in PRIOR_LIST:
                    PRIOR_LIST.remove(next_code)
                    PRIOR_LIST.insert(next_code,0)
                    uni_iter = 1
                else:
                    uni_iter = 0
            else:
                next_code = PRIOR_LIST[uni_iter]
            log_cc.warning("unicode {} doesn't match trying for {} ".format('utf-8', next_code))
            try:
                log_cc.info('Entered for recursive encode checking of {} with respect to encode {}'.format(filename, next_code))
                recur_track += 1
                uni_iter+=1
                if csv_copier(filename,src_dir,dest_dir,next_code):
                    break
            except Exception as error_msg:
                log_cc.critical('Exception {} in {}{} recursive call for correcting encoding'.format(error_msg,recur_track,
                                                                                                  'st' if str(recur_track)[-1] == '1'
                                                                                                    else 'nd' if str(recur_track)[-1] == '2'
                                                                                                    else 'rd' if str(recur_track)[-1] == '3'
                                                                                                    else 'th'))

        else:
            log_cc.warning('Completely different unicode used in {}'.format(filename))
            try:
                binary_copier(filename,src,dest_dir)
            except:
                raise Exception(UnicodeDecodeError)
    except Exception as error_msg:
        log.critical('Exception occurred in opening csv file {} is {}'.format(filename,error_msg))
    finally:
        fp.close()
        log_cc.debug(f'File is safely closed now -- check file status {fp.closed}')

