import os


def find_files(suffix, path):
    file_list = [os.path.join(path, x) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) if
                 x.endswith(suffix)]
    dir_list = [os.path.join(path, x) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

    if len(dir_list) == 0:
        if len(file_list) > 0:
            return file_list[:]
        else:
            return []
    for directory in dir_list:
        file_list.extend(find_files(suffix, directory))

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return file_list


print(find_files("", "./")) # prints all files
print(find_files(".c", "./testdir/")) # prints all c files
print(find_files("hh", ".")) # no such file format
