def get_file(file_name):
    if file_name is None or len(file_name) == 0:
        raise NameError('File name with path is required')

    file = open(file_name, 'r')

    return file


def isPalindrome(words):
    """After removing spaces, checks if string is a palindrome."""
    words = words.replace(' ', '').lower()
    org = list(words)
    rev = list(words)
    rev.reverse()
    return org == rev


def get_clean_text(file):
    """Removes carriage return's from the list."""
    return [line.rstrip('\n') for line in file.readlines()]


def generate_output_files(file_text_list):
    pal_file = open('palindrome.txt', 'w')
    oth_file = open('other_text.txt', 'w')
    for line in file_text_list:
        if isPalindrome(line):
            pal_file.write(f'{line}\n')
        else:
            oth_file.write(f'{line}\n')
    return
