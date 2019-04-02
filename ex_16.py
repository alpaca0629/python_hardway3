from sys import argv
script, filename = argv
print("We're going to erase{}".format(filename))
print("if u don't want that, hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file,  Goodbye!")

print("Now I'm going to ask you for three lines ")

print("I'm going to write these to the file")

target.write("{}\n{}\n{}".format(input("line1:"), input("line2:"), input("line3:")))


print("And finally, we close it.")
target.close