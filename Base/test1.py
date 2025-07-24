num=10

def fun1():
    global num
    print(num)
    num = 20
    print("Inside function:",num)
fun1()

def main():
    return input('Enter a number: ')

while True:
    try:
        x = int(main())
        if x == 10:
            break;
    except ValueError:
        print("Oops, that was no valid number.  Try again...")