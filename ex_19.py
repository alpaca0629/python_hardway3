import math
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} cheeses!".format(cheese_count))
    print("you have {} boxes of crackers!".format(boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

cheese_and_crackers(input("The number of chesses:"),input("The number of boxers of crackers:"))

print("we can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("OR, we can use variables from our directly:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 * 10**2, 500/20)

print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese * 2, amount_of_crackers * 2**0.5)
