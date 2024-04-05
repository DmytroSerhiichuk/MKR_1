
def read_lines(file_name: str) -> list[str]:
    '''
    Reads lines from file

    Params:
    - file_name: the name of the file from which the data is read

    Returns:
    - list[str]: read lines
    '''
    with open(file_name, 'r') as file:
        return file.readlines()

def filter_lines(lines: list[str], keyword: str) -> list[str]:
    '''
    Filters lines by keyword

    Params:
    - lines: lines that will be filtered
    - keyword

    Returns:
    - list[str]: filtered lines 
    '''
    return [line for line in lines if keyword in line]

def save_lines(lines: list[str], output_file_name: str):
    '''
    Save lines to the file

    Params:
    - lines: lines that will be saved
    - output_file_name: the path to the file to which the lines will be written
    '''
    with open(output_file_name, 'w') as file:
        for line in lines:
            file.write(line)

def main():
    file_name = 'data.txt'

    lines = read_lines(file_name)

    filtered_lines = filter_lines(lines, 'world')

    save_lines(filtered_lines, 'filtered.txt')

if __name__ == '__main__':
    main()