
def read_lines(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        return file.readlines()

def filter_lines(lines: list[str], keyword: str) -> list[str]:
    return [line for line in lines if keyword in line]

def save_lines(lines: list[str], output_file_name: str):
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