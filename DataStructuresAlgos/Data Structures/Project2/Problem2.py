import os


def find_files(suffix, path):
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

    if os.path.isfile(path) and path.endswith(suffix):
        return path

    files = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path) and item.endswith(suffix):
            files.append(full_path)
        elif os.path.isdir(full_path):
            results = find_files(suffix, full_path)
            files += results

    return files


if __name__ == "__main__":
    print(
        find_files(
            ".c",
            r"C:\Users\matth\OneDrive\Learning\Udacity\DataStructuresAlgos\DataStructures\Project2\testdir",
        )
    )
    # Expected output: List of all files in path ending in .c
    print(
        find_files(
            "",
            r"C:\Users\matth\OneDrive\Learning\Udacity\DataStructuresAlgos\DataStructures\Project2\testdir",
        )
    )
    # Expected output: List of all files in path
    print(
        find_files(
            "abcdef",
            r"C:\Users\matth\OneDrive\Learning\Udacity\DataStructuresAlgos\DataStructures\Project2\testdir",
        )
    )
    # Expected output: Empty list
