
n = int(input())


for i in range(n):
    i_3 = i % 3
    i_5 = i % 5
    if  i_3 == 0 and i_5 == 0 :
        print(i,": FizzBuzz")
    elif i_3 == 0:
        print(i,": Fizz")
    elif i_5 == 0:
        print(i, ": Buzz")
    else:
        print(i)


