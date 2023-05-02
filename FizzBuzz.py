variable=int(input("Enter The Number :"))
if variable%3==0 and variable%5==0:
    print("FizzBuzz")
elif variable%3==0:
    print("Fizz")
elif variable%5==0:
    print("Buzz")
