import os
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

@pytest.mark.parametrize('lines, keyword, result', [
    ([
        'word key blue\n',
        'red green white\n',
        'rat word text\n',
        'hello world end\n'
    ],
    'word',
    [
        'word key blue\n',
        'rat word text\n'
    ]),
    ([
        'one two three\n',
        'four five six\n',
        'seven one nine\n',
        'ten eleven\n'
    ],
    'one',
    [
        'one two three\n',
        'seven one nine\n',
    ])
])
def test_filter_lines(lines, keyword, result):
    assert filter_lines(lines, keyword) == result

@pytest.mark.parametrize('lines, output', [
    (
        [
            'hello world test\n',
            'red blue test green\n',
            'end test finall\n'
        ],
        'test_filtered.txt'
    )
])
def test_save_lines(lines, output):
    save_lines(lines, output)

    assert os.path.isfile(output)

    with open(output, 'r') as file:
        assert file.readlines() == lines