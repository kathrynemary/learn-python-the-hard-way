from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Are you ready, kids?\nHit RETURN to continue, or Ctrl-C to exit."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "All righty, that's that!"

out_file.close()
in_file.close()
