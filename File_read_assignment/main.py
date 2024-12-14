import re #Regular expression
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

def clean_data(f_data):
    """
    :param f_data: raw data as fp.read() mostly given by raw_data(filename)
    :return: A cleaned data which as only .isalpha content.
    """
    try :
        f_data = re.findall(r'[a-zA-Z]+', f_data)
        return f_data
    except Exception as error_msg:
        print('Exception in extracting data is {} pls check data {} '.format(error_msg,f_data))
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

def palindrome(word, palin_list):
    """
    :param word: Is the word which is to checked for palindrome
    :param palin_list: Is the palin_list from fetch_palindrome function
    :return: Modified palin_list
    """
    try :
        length = len(word)
        temp = word.lower().strip()
        if length!=1:
            for cf in range(len(word) // 2 + 1):
                if temp[cf] == temp[length - 1 - cf]:
                    continue
                else:
                    break
            else:
                palin_list.append(word)
        return palin_list
    except Exception as error_msg:
        print('Exception is {} '.format(error_msg))
    finally:
        return palin_list

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_palindrome(f_data):
    """
    This function checks for type of content and thus decides whether to proceed or not.
    :param f_data: should be a list of .isalpha content.
    :local_var palin_list: collects all the palindrome.
    :return: palin_list
    """
    try :
        palin_list = []
    except Exception as error_msg:
        print('ERROR IS --> {} '.format(error_msg))
    else:
        try :
            if isinstance(f_data,list):
                for scan in f_data:
                    palin_list = palindrome(scan, palin_list)
            else:
                raise Exception('Something suspicious is included {} '.format(f_data))
        except Exception as error_msg:
            print('Error is --> {} '.format(error_msg))
        else:
            return palin_list


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def occurrence(f_data):
    """
    :param f_data: Raw data as fp.read()
    :return: Dictionary with words and their counts in raw data
    """
    try :
        f_set = list(set(f_data))
        occur_dict = {key.lower().strip():f_data.count(key) for key in f_set if key.isalpha() and len(key)!=1}
        top_counts = set(list(occur_dict.values()))
        top_counts = sorted(top_counts)
        if len(top_counts)>=5:
            top_counts.reverse()
            top_counts = top_counts[0:5]
        top_5_freq_words = {count:[word for word in occur_dict if count==occur_dict[word]] for count in top_counts}
        return occur_dict,top_5_freq_words
    except Exception as error_msg:
        print('Exception in calculating occurrence of each word is {} or pls check to provided data {}'.format(error_msg,f_data))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_emails(f_data):
   """
   :param f_data: Raw data of file i.e. fp.read()
   :return: List of emails
   """
   try:
       f_data = list(set(f_data.split('+')))
       top_level_domains = [
           "com",
           "org",
           "net",
           "edu",
           "co",
           "in"
       ]
       emails = []
       for segment in f_data:
           if '.' in segment and '@' in segment:
               if segment.split('.')[-1] in top_level_domains:
                   emails.append(segment)
       return emails
   except ValueError as error_msg:
       print('Something malicious may have been added {} pls check file data {}'.format(error_msg, f_data))
   except Exception as error_msg:
       print('Exception in fetching email is {} pls check your file data {}'.format(error_msg,f_data))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_numbers(f_data):
    """
    :param f_data: Raw data of file.
    :return: List with all the numbers in file.
    """
    try:
        f_data = list(set(re.findall(r"[0-9]+", f_data)))
        return f_data
    except ValueError as error_msg:
        print('Something malicious may have been added {} pls check file data {}'.format(error_msg,f_data))
    except Exception as error_msg:
        print("Exception in fetching numbers is {} pls check your file data {}".format(error_msg,f_data))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def vowel_set(f_data):
    """
    :param f_data: Raw data
    :return: List of vowel-initial-words.
    """
    try:
        vowels = [
            'a',
            'e',
            'i',
            'o',
            'u',
        ]
        vowels += [vol.upper() for vol in vowels]
        return [word for word in f_data if word[0] in vowels and len(word)!=1]
    except ValueError as error_msg:
        print('Something malicious may have been added {} pls check file data {}'.format(error_msg, f_data))
    except Exception as error_msg:
        print('Exception in identifying vowel-initial-words is {} pls check file data {}'.format(error_msg,f_data))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_anagrams(f_data):
    """
    :param f_data: Clean data but not with duplicates.
    :return: Dictionary with anagrams
    """
    try:
        anagram_dict = dict()
        for word in f_data:
            temp_word = word.lower()
            if len(word)!=1:
                for trav in f_data:
                    temp_trav = trav.lower()
                    if temp_trav!=temp_word and ''.join(sorted(list(temp_word)))==''.join(sorted(list(temp_trav))):
                        if word in anagram_dict:
                            anagram_dict[word].append(trav)
                        else:
                            anagram_dict[word] = [trav]
                        f_data.remove(trav)
        return anagram_dict
    except ValueError as error_msg:
        print('Something malicious may have been added {} pls check file data {}'.format(error_msg, f_data))
    except Exception as error_msg:
        print('Exception in fetching anagrams is {} pls check file data {}'.format(error_msg, f_data))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    """
    Moin code with all the data and function calls
    :return: Nothing
    """

    file_name = input('Enter the File Name - ')

    file_data = raw_data(file_name)
    print( f'\nEmails are :- {fetch_emails(file_data)}'
          f'\nNumbers are {fetch_numbers(file_data)}'
    )

    clean_content = clean_data(file_data)
    del file_data
    print(f'\nOccurrence of each word is :- {occurrence(clean_content)[0]}'
          f'\nTop 5 frequent words are :- {occurrence(clean_content)[1]}')

    file_set = list(set(clean_content))
    del clean_content
    print(
          f'Palindromes are :- {fetch_palindrome(file_set)}'
          f'\nAnagrams are :- {fetch_anagrams(file_set)}'
          f'\nVowel-Initial-Words are {vowel_set(file_set)}'
    )
    print('---------------------------------------------------------Program execution successfully------------------------------------------------------------------------------')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import cProfile #To check the profile of the code
if __name__=='__main__':
    main()
    #cProfile.run('main()')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
