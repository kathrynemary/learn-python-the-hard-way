from sys import argv

script, user = argv
prompt = '> '

print "Hi, %s, I'm the %s script." % (user, script)
print "Do you like me, %s?" % user
likes = raw_input(prompt)

print "Where is your house, %s?" % user
house = raw_input(prompt)

print """
You said you like me thiiiis much: %r
You live at %r.
""" % (likes, house)
