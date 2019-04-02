from sys import argv
from os.path import exists

scrip, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("The input file is {} bytes long".format(len(indata)))

print("Does the output file exist?{}".format(exists(to_file)))
print("Ready, hit ENTER to continue, CTRL-C to abort.")
input()


out_file = open(to_file, 'w')
out_file.write(indata)


print("Alright,all done.")

out_file.close()
in_file.close()