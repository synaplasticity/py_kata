def get_file(file_name):
    if file_name is None or len(file_name) == 0:
        raise NameError('File name with path is required')

    file = open(file_name, 'r')

    return file.read()


def isPalindrome(words):
    words = words.replace(' ', '').lower()
    org = list(words)
    rev = list(words)
    rev.reverse()
    return org == rev

def get_text_from_file(file):
    return
