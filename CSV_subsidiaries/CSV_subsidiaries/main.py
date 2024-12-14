import csv

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def handler(func):
    """
    :param func: function which will carry the file_name data.
    :return: opener function which contains the file opening logic.
    """
    try :
        def opener(csv_file):
            """
            :param csv_file: File is to be opened in read mode and tested for functionalities.
            :return: file data.
            """
            try:
                result = None
                with open(csv_file) as file_ptr:
                    csv_content = csv.DictReader(file_ptr)
                    result = func(csv_content)
            except FileNotFoundError as error_msg2:
                print('File {} is not found {} '.format(csv_file, error_msg2))
            except ValueError as error_msg2:
                print('Please enter a valid filename {} and check if extension is "csv" or not error is {} '.format(
                    csv_file, error_msg2))
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
def sub_sort(iter_obj):
    """
    :param iter_obj: The iterator containing a list of dictionaries
    :return: Three segregated lists of subsidiaries BHFL,BDL,BD respectively
    """
    try:
        BHFL, BDL, BD = [], [], []
        for dictionary in iter_obj:
            if dictionary['sub'].upper().strip() == 'BHFL':
                BHFL.append(dictionary)
            elif dictionary['sub'].upper().strip() == 'BD':
                BD.append(dictionary)
            elif dictionary['sub'].upper().strip() == 'BDL':
                BDL.append(dictionary)
        return BHFL, BD, BDL
    except Exception as error_msg:
        print('Exception in segregating subsidiaries is {} pls check your data {}'.format(error_msg,[datum for datum in iter_obj]))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def customer_file_write(sub, dict_lines):
    """
    :param sub: These are subsidiaries with respect to them csv files will be made
    :param dict_lines: A single dictionary
    :return: None
    """
    try:
        with open(f'customer_{sub}.csv', 'a', newline='') as fp:
            w_obj = csv.DictWriter(fp, fieldnames=['cust_id', 'cust_name','sub'])
            w_obj.writeheader()
            w_obj.writerows(dict_lines)
    except Exception as error_msg:
        print('Exception in opening and reading/writing csv file is {} pls check your data {} '.format(error_msg,dict_lines))
    finally:
        fp.close()
        print('Check file close status :- {}'.format(fp.closed))
        return None

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    """
    :return: None
    """
    try:
        source_file = input('Enter the file name :- ')+'.csv'
        sub = ('BHFL', 'BD', 'BDL')
        list(map(lambda sub_cat, lines: customer_file_write(sub_cat, lines), sub, sub_sort(source_file)))
    except Exception as error_msg:
        try:
            print('Exception in DRIVER CODE is :- {} pls check your SOURCE FILE {}'.format(error_msg,source_file))
        except Exception as error_msg:
            print("Exception is {} might be source file's name has a typo".format(error_msg))
            return None


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()



