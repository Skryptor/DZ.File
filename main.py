def read_files(*file_names):
    file_contents = {}
    for file_name in file_names:
        with open(file_name, encoding='utf-8') as file:
            file_contents[file_name] = file.read().splitlines()
    return file_contents


def print_sorted_files(file_contents):
    sorted_files = sorted(file_contents.items(), key=lambda item: len(item[1]))

    for file_name, lines in sorted_files:
        print(f"{file_name}")
        print(len(lines))
        for line in lines:
            print(line)

file_contents = read_files('1.txt', '2.txt')

print_sorted_files(file_contents)






