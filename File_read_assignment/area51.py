"""This is just the testing area

f_data = set([7,5,4,8,7,8,8,8,4,7])
for i in list(f_data):
    for j in list(f_data):
        if i in f_data:
            f_data.remove(j)
    print(f_data)

f_data0 = ['silent','listen','update','dateup']
def fetch_anagrams(f_data):
    try:
        anagram_list = dict()
        for word in f_data:
            temp_word = word.lower()

            if len(word)!=1:

                for trav in f_data:
                    print(trav)

                    temp_trav = trav.lower()
                    if temp_trav!=temp_word and ''.join(sorted(list(temp_word)))==''.join(sorted(list(temp_trav))):
                        if word in anagram_list:
                            anagram_list[word].append(trav)
                        else:
                            anagram_list[word] = []
                            anagram_list[word].append(trav)

                        f_data.remove(trav)
        return anagram_list
    except ValueError as error_msg:
        print('Something malicious may have been added {} pls check file data {}'.format(error_msg, f_data))
    except Exception as error_msg:
        print('Exception in fetching anagrams is {} pls check file data {}'.format(error_msg, f_data))
print(fetch_anagrams(f_data0))

"""
print([9,7,3,3,3,54,5][0:3].reverse())
"""It was a attempt to remove even all escape characters and avoid them getting mixed with real file content 
   specially it'll be useful when we convert .ipynb file into txt and search for palindrome.
   Function doesn't work properly for now."""

r''''@handler
def fetch_palindrome_smartly(f_data):
    try :
        palin_list_eff = []
        escape_characters = [
        r"\\",
        r"\n",
        r"\t",
        r"\'",
        r"\"",
        r"\r",
        r"\b",
        r"\f",
        r"\a",
        r"\v",
        r"\0",
        r"\x20",
        r"\041",
        r"\u00A9",
        r"\U0001F600"
        ]

        short_list = list(set([x for x in f_data if not x.isalpha()]))
        short_list += list(set([y for y in f_data if y in escape_characters]))
        result = re.split(r'[{}]+'.format(''.join(short_list) + ''.join(escape_characters)), f_data)
        print(result)
    except Exception as error_msg:
        print('Exception in 1st try IS --> {} '.format(error_msg))
    else:
        try :
            print(result)
            if isinstance(result, list):
                for scan in result:
                    if scan.lower().strip()[::-1] == scan.lower().strip() and len(scan)!=1 and scan.isalpha():
                            palin_list_eff.append(scan)
            else:
                raise Exception('Something suspicious is included in file data {} '.format(result))
        except Exception as error_msg:
            print('Exception in 2nd try is --> {} '.format(error_msg))
        else:
            return palin_list_eff'''










































