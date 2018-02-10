from palindrome.palindrome import *
import pytest


def test_get_file_no_file_name():
    with pytest.raises(NameError):
        get_file(None)


def test_get_file_empty_file_name():
    with pytest.raises(NameError):
        get_file('')


def test_get_file_bad_dir():
    with pytest.raises(FileNotFoundError):
        get_file('dir/py-pal.txt')


def test_get_valid_file():
    file_text = get_file('py-pal.txt')
    assert len(file_text.read()) > 0


def test_is_palindrome():
    assert isPalindrome("Taco Cat")


def test_is_not_palindrome():
    assert not isPalindrome("Test this")


def test_loaded_text_has_no_carraige_returns():
    text_list = get_clean_text(get_file('py-pal.txt'))
    assert not text_list[2].endswith('\n')

def test_palindrome_file():
    text_list = get_clean_text(get_file('py-pal.txt'))
    generate_output_files(text_list)
    pal_file = open('palindrome.txt', 'r')
    assert len(pal_file.readlines()) == 2


def test_non_plaindrome_file():
    text_list = get_clean_text(get_file('py-pal.txt'))
    generate_output_files(text_list)
    oth_file = open('other_text.txt', 'r')
    assert len(oth_file.readline()) > 0
