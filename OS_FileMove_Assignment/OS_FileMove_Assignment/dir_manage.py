from os.path import isdir,exists
from os import getcwd,chdir,mkdir,makedirs
from pathstring import path_string
from Filtrations import Filter_Bool as f_b , Filter_Str as f_s

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def dirs_creator(*dir_names):
    """
    :param dir_names: Variable length argument containing directories names to create in working directory by default.
    :return: None if found an exception
    """
    try:
        project_dir = getcwd()
        custom_path = input('Want to specify a certain path other than current directory [y/n] - ')
        if custom_path.lower().strip() == 'y':
            custom_path = f_b(val=True, func=exists, prm_type=str, prompt='Enter the path -- ')
        else:
            custom_path = getcwd()
        if len(dir_names) == 1:
            if custom_path == getcwd():
                mkdir(r'{}'.format(dir_names[0]))
            else:
                chdir(r'{}'.format(custom_path))
                mkdir(r'{}'.format(dir_names[0]))
                chdir(r'{}'.format(project_dir))
        else:
            if custom_path == getcwd():
                list(map(lambda inp_dir : mkdir(r'{}'.format(inp_dir)), dir_names))
            else:
                chdir(r'{}'.format(custom_path))
                list(map(lambda inp_dir: mkdir(r'{}'.format(inp_dir)), dir_names))
                chdir(r'{}'.format(project_dir))
    except FileExistsError:
        print('Directory/Directories {} already exists'.format([dup for dup in dir_names if isdir(r'{}/{}'.format(getcwd(),dup))]))
        return None
    except Exception as error_msg:
        print('Exception in creating your specified directory is {}'.format(error_msg))
        return None
    finally:
        try:
            chdir(r'{}'.format(project_dir))
        except NameError as error_msg:
            print('NameError {}'.format(error_msg))
            return None

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def nested_dirs_creator(*dir_names):
    """
    :param dir_names: Variable length argument containing nested directories names to create in working directory by default .
    :return: None if found an exception
    """
    try:
        project_dir = getcwd()
        if len(dir_names) == 1:
            dirs_creator(dir_names[0])
        else:
            custom_path = input('Want to specify a certain path other than current directory [y/n] - ')
            if custom_path.lower().strip() == 'y':
                custom_path = f_b(val=True, func=exists, prm_type=str, prompt='Enter the path -- ')
                chdir(r'{}'.format(custom_path))
                makedirs(path_string(len(dir_names)).format(*dir_names))
                chdir(r'{}'.format(project_dir))
            else:
                makedirs(path_string(len(dir_names)).format(*dir_names))
    except FileExistsError:
        print('Directory/Directories {} already exists'.format(
            [dup for dup in dir_names if isdir(r'{}/{}'.format(getcwd(), dup))]))
        return None
    except Exception as error_msg:
        print('Exception in creating your specified directory is {}'.format(error_msg))
        return None
    finally:
        try:
            project_dir = getcwd()
            chdir(r'{}'.format(project_dir))
        except NameError as error_msg:
            print('NameError {}'.format(error_msg))
            return None

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    """
    Act as driver code + menu
    :return: nothing
    """
    try:
        choice = f_s('A','B',prompt='Enter A for making multiple directories.\n'
                       'Enter B for making nested directory\n'
                       'CHOICE - ')
        while True:
            if choice.lower().strip() == 'a':
                count = int(input('Enter the number of directories to create - '))
                dirs = [input('Enter the name of your directory - ') for num in range(count)]
                dirs_creator(*dirs)
            else:
                count = int(input('Enter the number of directories to create - '))
                name = root_dir = input('Enter the ROOT directory name -- ')
                dirs = [root_dir]
                for inp in range(count-1):
                    name = input('Enter the name of your directory which will be inside the {} one - '.format(name))
                    dirs.append(name)
                nested_dirs_creator(*dirs)
            want = f_s('y','n',prompt='Want to continue? [y/n] -- ')
            if want == 'y':
                choice = f_s('A', 'B', prompt='Enter A for making multiple directories.\n'
                                              'Enter B for making nested directory\n'
                                              'CHOICE - ')
                continue
            else:
                print('THANKS FOR USING OUR PROGRAM!')
                break
    except Exception as error_msg:
        print('Exception in driver code is {}'.format(error_msg))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    #main()
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------












































