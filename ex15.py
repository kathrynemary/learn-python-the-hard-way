from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file called %r:" % filename
print txt.read()

print "What's that file called again?"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
print "closed!"
