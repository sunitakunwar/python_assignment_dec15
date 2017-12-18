#Write a function that simply returns ("Hello", 45, 23.3). Now, call this function and unpack the returned values and print it.
def f():
    return ["Hello", 45, 23.3]

result = list(f())

print(result)