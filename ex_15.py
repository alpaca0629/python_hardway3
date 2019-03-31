from sys import argv

prompt = '> '

script, filename = argv
txt = open(filename)

print("Here's your file{}".format(filename))
print(txt.read())

print("Type the filename again:")
file_again = input(prompt)

txt_again = open(file_again)

print(txt_again.read())