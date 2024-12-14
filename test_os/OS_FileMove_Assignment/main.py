from os import listdir, getcwd
from os.path import exists , basename
from valids.valid_ext import *
import copier.csv_c , copier.txt_c , copier.json_c , copier.yaml_c , copier.pickle_c , copier.binary_c
from Filtrations import Filter_Bool as f_b , Filter_Str as f_s
import logging as log

log.basicConfig(filename='server.log',
                filemode='w',
                format='%(levelname)s : %(name)s : %(asctime)s.%(msecs)03d :%(message)s',
                datefmt='%d-%a:%m-%b:%Y'
                       ' %H:%M:%S',
                level=log.INFO)
logger = log.getLogger(basename(__file__))

def file_segregate(src_dir, ext):
    try:
        specific_files = [fp for fp in listdir(src_dir) if fp.endswith(ext)]
        logger.info('Files with extension {} are extracted successfully.'.format(ext))
        return specific_files
    except Exception as error_msg:
        logger.warning('EXCEPTION {} raised'.format(error_msg))
        return None

def main():
    try:
        while True:
            logger.info('--------------------------------------------------------Started the driver code----------------------------------------------------------------------------')
            working = f_s('y', 'n', prompt='Source directory is in working directory [y/n] -- ')
            logger.info(
                'Source directory is in working directory? {}{}'.format(working, 'es' if working == 'y' else 'o'))
            if working == 'y':
                src_dir = f_b(val=True, func=exists, f_concat=getcwd() + '/', prm_type=str,
                              prompt='Enter the source directory -- ')
                logger.info('Source directory is {}'.format(src_dir))
            else:
                src_dir = f_b(val=True, func=exists, prm_type=str, prompt='Enter the source directory entire path -- ')
                logger.info('Source directory is {}'.format(src_dir))

            working = f_s('y', 'n', prompt='Destination directory is in working directory [y/n] -- ')
            logger.info(
                'Destination directory is in working directory? {}{}'.format(working, 'es' if working == 'y' else 'o'))
            if working == 'y':
                dest_dir = f_b(val=True, func=exists, f_concat=getcwd() + '/', prm_type=str,
                               prompt='Enter the destination directory -- ')
                logger.info('Destination directory is {}'.format(dest_dir))

            else:
                dest_dir = f_b(val=True, func=exists, prm_type=str,
                               prompt='Enter the destination directory entire path -- ')
                logger.info('Destination directory is {}'.format(dest_dir))

            extension = f_s(*(list(CSV.keys()) + list(PICKLE.keys()) + list(JSON.keys()) + list(TXT.keys()) + list(YAML.keys()) + list(BINARY.keys())), prompt='Enter the file extension -- ')
            logger.info('Extension requested by user is -- {}'.format(extension))
            records = file_segregate(src_dir, extension)
            logger.info('Records are extracted {}'.format(records))

            if extension in TXT:
                list(map(lambda proc: logger.info('File {} is in destination'.format(proc)) if copier.txt_c.txt_copier(proc, src_dir,dest_dir) == True else logger.info('File {} was left half read'.format(proc)), records))
                logger.info('{} Files moving is SUCCESSFUL'.format(records))

            elif extension in CSV:
                list(map(lambda proc: logger.info('File {} is in destination'.format(proc)) if copier.csv_c.csv_copier(proc, src_dir , dest_dir) == True else logger.info('File {} was left half read'.format(proc)), records))
                logger.info('{} Files moving is SUCCESSFUL'.format(records))

            elif extension in JSON:
                list(map(lambda proc: logger.info('File {} is in destination'.format(proc)) if copier.json_c.json_copier(proc, src_dir,dest_dir)== True else logger.info('File {} was left half read'.format(proc)), records))
                logger.info('{} Files moving is SUCCESSFUL'.format(records))

            elif extension in YAML:
                list(map(lambda proc: logger.info('File {} is in destination'.format(proc)) if copier.yaml_c.yaml_copier(proc, src_dir, dest_dir)== True else logger.info('File {} was left half read'.format(proc)), records))
                logger.info('{} Files moving is SUCCESSFUL'.format(records))

            elif extension in PICKLE:
                list(map(lambda proc: logger.info('File {} is in destination'.format(proc)) if copier.pickle_c.pickle_copier(proc,src_dir,dest_dir)== True else logger.info('File {} was left half read'.format(proc)), records))
                logger.info('{} Files moving is SUCCESSFUL'.format(records))

            else:
                list(map(lambda proc: logger.info('File {} is in destination'.format(proc)) if copier.binary_c.binary_copier(proc,src_dir,dest_dir)== True else logger.info('File {} was left half read'.format(proc)), records))
                logger.info('{} Files moving is SUCCESSFUL'.format(records))
            continued = f_s('y', 'n', prompt='Want to continue ? [y/n] -- ')
            if continued != 'y':
                break

    except Exception as error_msg:
        logger.critical('CRITICAL exception in driver code is {}'.format(error_msg))

if __name__ == '__main__':
    main()
