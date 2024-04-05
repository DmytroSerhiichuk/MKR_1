
def read_lines(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        return file.readlines()


def main():
    file_name = 'data.txt'

    lines = read_lines(file_name)


if __name__ == '__main__':
    main()