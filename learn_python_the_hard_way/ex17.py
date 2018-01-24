from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print("the input file is", len(indata), "long")
print("does the output file exists?", exists(to_file))
print("ready? hit return to continue or CTRL-C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("All right, Done!!!")

out_file.close()



