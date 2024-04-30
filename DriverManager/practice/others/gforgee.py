class test:
    @staticmethod
    def square(x):
        test.result = x * x

    # object 1 for class


t1 = test()

# object 2 for class
t2 = test()
t1.square(2)

# printing result for square(2)
print (t1.result)
t2.square(3)

# printing result for square(3)
print (t2.result)

# printing the last value of result as we declared the method static
print(t1.result)