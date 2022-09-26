def makeIfNotExist(directory):
    '''
    Checks if directory exists and creates new directory
    Parameters:
    -------------------
    directory: str
        Output folder path as per log curve present
    Returns:
    -------------------
    directory: str, directory of output path created
    '''
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return directory
