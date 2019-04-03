def print_two(*args):
    arg1, arg2, arg3 = args
    print("arg1:{},arg2:{},arg3:{}".format(arg1, arg2, arg3))

def print_two_again(arg1, arg2):
    print("arg1:{}, arg2:{}".format(arg1, arg2))

def print_one(arg1):
    print("arg1:{}".format(arg1))

def print_none():
    print("I got nothin'.")


print_two(input("1:"), input("2:"), input("3:"))
print_two_again("shell","may")
print_one("first")
print_none()