from sys import argv
script, input_file = argv


def print_all(file_input):
    print(file_input.read())
    print("\n")


def rewind(file_input):
    file_input.seek(0)


def print_a_line(line_count, input_file):
    print(line_count, input_file.readline())


current_file = open(input_file)

print_all(current_file)

print("Now let's rewind, kind of like a type.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
