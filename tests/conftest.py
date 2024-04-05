import pytest

@pytest.fixture
def prepered_file():
    path = 'test_data.txt'
    with open(path, 'w') as file:
        lines = ['one two three\n',
                 'four five six\n',
                 'two second eleven\n',
                 'red blue green\n',
                 'pink white two\n',
                 'last end stop\n']
        file.writelines(lines)
    return path