def cheese_n_crackers(cheese_amt, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_amt
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's so many!"
    print "Grab some wine!\n"

print "We can just hand the function some numbers:"
cheese_n_crackers(20,30)

print "Or, we can use variables from our script:"
amount_o_cheese = 10
amount_o_crackers = 400

cheese_n_crackers(amount_o_cheese, amount_o_crackers)

print "We can also do math:"
cheese_n_crackers(10+2, 5 * 8)

print "We can also combine variables w/ math!"
cheese_n_crackers(amount_o_cheese + 100, amount_o_crackers / 3)
