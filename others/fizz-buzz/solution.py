def fizzBuzz(x):
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzBuzz(15)
fizzBuzz(30)
fizzBuzz(0)
fizzBuzz(-100)
