def add(a, b):
    print("Adding {} + {}".format(a, b))
    return a + b


def subtract(a, b):
    print("Subtracting {} - {}".format(a, b))
    return a - b


def multiply(a, b):
    print("Multiplying {} * {}".format(a, b))
    return a * b


def divide(a, b):
    print("Dividing {} / {}".format(a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(int(input("age1:")), 60)

height = subtract(int(input("height1:")), subtract(100, 10))

weight = multiply(int(input("weight1:")), int(input("weight2:")))

iq = divide(float(input("iq1:")), divide(30, 1.5))

print("Age: {}, Height: {}, Weight: {}, IQ:{}".format(age, height, weight, iq))

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("The finall answer is", what)