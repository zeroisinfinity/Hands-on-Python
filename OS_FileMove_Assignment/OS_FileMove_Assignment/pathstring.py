def path_string(dirs):
    """
    :param dirs: No.of dirs to create
    :return: A string containing whole path string which can be formatted to create a nested directory
    :return: None if Exception found.
    """
    try:
        p_str = r'{}/'
        dirs -= 1
        while dirs:
            p_str += r'{}'
            dirs -= 1
            if dirs:
                p_str += "/"
        return p_str
    except ValueError as value_msg:
        print('Pls enter the correct value of {}'.format(dirs))
        return None
    except Exception as error_msg:
        print('Exception in creating your custom path string is {}'.format(error_msg))
        return None

