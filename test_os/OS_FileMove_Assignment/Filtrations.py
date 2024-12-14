import logging as log
import pathlib

log_filter = log.getLogger(pathlib.Path(__file__).name)
def Filter_Str(*val,prompt = 'Enter the required value - '):
    try:
        inp = input('{}'.format(prompt))
        while inp.lower().strip() not in [gen.lower().strip() for gen in val]:
            log_filter.info('Has entered WHILE LOOP for string check for values {}'.format(val))
            print('Pls enter values which are mentioned in {}'.format(val))
            inp = input('{}'.format(prompt))
        inp.lower().strip()
        return inp
    except Exception as error_msg:
        log_filter.critical('Exception occurred in filter functions {}'.format(error_msg))

def Filter_Int(*val,prompt  = 'Enter the required value - '):
    try:
        inp = int(input('{}'.format(prompt)))
        while inp not in val:
            log_filter.info('Has entered WHILE LOOP for integer check for values {}'.format(val))

            print('Pls enter values which are mentioned in {}'.format(val))
            inp = int(input('{}'.format(prompt)))
        return inp
    except Exception as error_msg:
        log_filter.critical('Exception occurred in filter functions {}'.format(error_msg))

def Filter_Float(*val,prompt  = 'Enter the required value - '):
    try:
        inp = float(input('{}'.format(prompt)))
        while inp not in val:
            log_filter.info('Has entered WHILE LOOP for float check for values {}'.format(val))

            print('Pls enter values which are mentioned in {}'.format(val))
            inp = float(input('{}'.format(prompt)))
        return inp
    except Exception as error_msg:
        log_filter.critical('Exception occurred in filter functions {}'.format(error_msg))

def Filter_Bool(val,func,prm_type,f_concat = '',r_concat = '',prompt  = 'Enter the required value - '):
    try:
        inp = f_concat + prm_type(input('{}'.format(prompt))) + r_concat
        if val:
            while not func(inp):
                log_filter.info('Has entered WHILE LOOP for bool(==True) check for values {}'.format(val))

                print('Pls enter values which are {}'.format(val))
                inp = f_concat + prm_type(input('{}'.format(prompt))) + r_concat
        else:
            while func(inp):
                log_filter.info('Has entered WHILE LOOP for bool(==False) check for values {}'.format(val))

                print('Pls enter values which are {}'.format(val))
                inp = f_concat + prm_type(input('{}'.format(prompt))) + r_concat
        return inp
    except Exception as error_msg:
        log_filter.critical('Exception occurred in filter functions {}'.format(error_msg))


