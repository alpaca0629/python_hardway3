print("Let's pratice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")


five = 10 - 2 + 3 - 6
print("This should be five:{}".format(five))


def secret_formula(started):
    jelly_bean = started * 500
    jars = jelly_bean / 1000
    crates = jars / 100
    return jelly_bean, jars, crates


start_point = 1000
beans, jars, crates = secret_formula(start_point)

print(f"With a starting point of: {start_point}")

print("We'd have {} beans, {} jars, and {} \
crates.".format(beans, jars, crates))

start_point /= 10

print("We can also do that this way:")
formuala = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formuala))
