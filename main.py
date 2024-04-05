
def read_lines(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        return file.readlines()

def filter_lines(lines: list[str], keyword: str) -> list[str]:
    return [line for line in lines if keyword in line]

def main():
    file_name = 'data.txt'

    lines = read_lines(file_name)

    filtered_lines = filter_lines(lines, 'world')

if __name__ == '__main__':
    main()