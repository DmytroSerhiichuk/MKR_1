import pytest
from main import read_lines
from main import filter_lines
from main import save_lines

def test_read_lines(prepered_file):
    expected = ['one two three\n',
                 'four five six\n',
                 'two second eleven\n',
                 'red blue green\n',
                 'pink white two\n',
                 'last end stop\n']
    assert read_lines(prepered_file) == expected


