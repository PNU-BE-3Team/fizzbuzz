# 피즈버즈 값 확인하기

#성민님 마무리 부탁드려요~!~!~!

for i in range(50):
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

