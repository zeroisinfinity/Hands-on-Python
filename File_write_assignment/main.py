import re
from argparse import FileType
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def handler(func):
    """
    :param func: function which will carry the file_name data.
    :return: opener function which contains the file opening logic.
    """
    try :
        def opener(incoming_file):
            """
            :param incoming_file: File is to be opened in read mode and tested for functionalities.
            :return: file data.
            """
            try:
                with open(incoming_file) as file_ptr:
                    f_content = file_ptr.read()
                    result = func(f_content)
            except FileNotFoundError as error_msg2:
                print('File {} is not found {} '.format(incoming_file, error_msg2))
            except ValueError as error_msg2:
                print('Please enter a valid filename {} and check if extension is "txt" or not error is {} '.format(
                    incoming_file, error_msg2))
            except Exception as error_msg2:
                print('Error was - {} '.format(error_msg2))
            else:
                print(f'Process {func} executed successfully!')
            finally:
                file_ptr.close()
                print('Check file close status {} '.format(file_ptr.closed))
                return result
        return opener
    except Exception as error_msg:
        print('Exception in file handler decorator is {} '.format(error_msg))
        return None

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@handler
def raw_data(f_data):
    """
    :param f_data: Is the file content aka simply fp.read().
                   It's wrapped in the handler function so it picks a data
                   and after file is closed in finally block
                   of handler.
    :return: Simply returns f_data and nothing else.
    """
    try:
        return f_data
    except Exception as error_msg:
        print('Exception is {} '.format(error_msg))
        return None

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def occurrence(f_data):
    """
    :param f_data:
    :return:
    """
    try :
        f_set = list(set(re.findall(r'[a-zA-Z]+',f_data)))
        occur_dict = {key.lower().strip():f_data.count(key) for key in f_set if key.isalpha() and len(key)!=1}
        return occur_dict
    except Exception as error_msg:
        print('Exception in calculating occurrence of each word is {} or pls check to provided data {}'.format(error_msg,f_data))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_emails(f_data):
   """
    :param f_data: Raw data of file i.e. fp.read()
    :return: List of emails
   """
   try:
       f_set = list(set(re.findall(r'[a-zA-Z0-9.@]+',f_data)))
       top_level_domains = [
           "com",
           "org",
           "net",
           "edu",
           "co",
           "in"
       ]
       emails = []
       for segment in f_set:
           if '.' in segment and '@' in segment:
                   if segment.split('.')[-1] in top_level_domains:
                       emails.append(segment)
       return emails
   except ValueError as error_msg:
       print('Something malicious may have been added {} pls check file data {}'.format(error_msg, f_data))
   except Exception as error_msg:
       print('Exception in fetching email is {} pls check your file data {}'.format(error_msg, f_data))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_numbers(f_data):
    """
    :param f_data: Raw data of file.
    :return: List with all the numbers in file.
    """
    try:
        f_data = re.findall(r"[0-9+]+", f_data)
        list(set(f_data))
        valid_num = []
        invalid_num = []
        for num in f_data:
            if num[0] == '+':
                if num[1:3] == '91':
                    if int(num[3]) > 5:
                        if len(num) == 13:
                            valid_num.append(num)
                        else:
                            invalid_num.append(num)
                    else:
                        invalid_num.append(num)
                else:
                    invalid_num.append(num)
            else:
                if int(num[0]) > 5:
                    if len(num) == 10:
                        valid_num.append(num)
                    else:
                        invalid_num.append(num)
                else:
                    invalid_num.append(num)
        return valid_num,invalid_num
    except ValueError as error_msg:
        print('Something malicious may have been added {} pls check file data {}'.format(error_msg,f_data))
    except Exception as error_msg:
        print("Exception in fetching numbers is {} pls check your file data {}".format(error_msg,f_data))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def file_writer(file_name,f_data):
    try:
        with open(file_name, 'w') as file_ptr:
            file_ptr.write(f'{f_data}')
    except FileType:
        print(f"There's a mistake in file's extension/type i.e. {file_name.split('.')[-1]} pls kindly check")
    except Exception as error_msg:
        print(f'Exception in writing a file named {file_name} with data {f_data} is {error_msg}')
    finally:
        file_ptr.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    """
    Moin code with all the data and function calls
    :return: Nothing
    """
    try:
        file_name = input('Enter the file from which the data is to be fetched :- ')
        f_data = raw_data(file_name)
        files = ['emails.txt', 'valid_mobile_numbers.txt', 'invalid_mobile_numbers.txt', 'wordcount.txt']
        result_tuple = (fetch_emails(f_data), fetch_numbers(f_data)[0], fetch_numbers(f_data)[1], occurrence(f_data))
        list(map(lambda fp, inp: file_writer(fp, inp), files, result_tuple))
        print('---------------------------------------------------------Program execution successfully------------------------------------------------------------------------------')
    except Exception as error_msg:
        print(f'Exception is :- {error_msg}')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import cProfile #To check the profile of the code
if __name__=='__main__':
    main()
    #cProfile.run('main()')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
