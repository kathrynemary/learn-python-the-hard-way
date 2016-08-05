def add(a, b):
    print "Adding %d to %d" % (a,b)
    return a + b

def subtract(a,b):
    print "Subtracting %d from %d" % (b,a)
    return a - b

def multiply(a,b):
    print "Multiplying %d and %d" % (a,b)
    return a - b

def divide(a,b):
    print "Dividing %d into %d" % (a,b)
    return a / b

print "Let's do some math w/ just fxns!"

age = add(30,6)
height = subtract(75,4)
weight = divide(290,2)
iq = multiply(90,2)

print "Age: %d\nHeight: %d\nWeight: %d\nIQ: %d" % (age, height, weight, iq)

print "Here's a puzzle:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"
