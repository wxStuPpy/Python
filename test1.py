num=10

def fun1():
    global num
    print(num)
    num = 20
    print("Inside function:",num)
fun1()
