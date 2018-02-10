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
    assert len(file_text) > 0


def test_is_palindrome():
    assert isPalindrome("Taco Cat")


def test_is_not_palindrome():
    assert not isPalindrome("Test this")


def test_load_text_from_file():
    assert len(get_text_from_file(get_file('py-pal.txt'))) > 0
