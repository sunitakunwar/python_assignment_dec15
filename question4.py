'''Write a function that solves the equation, y=mx+c where different values of x'es are [1, 2.3, 5.6, 7, 78].
Your function shouldn't return any values but must print the value of y for each iteration. value of y should be in
2 decimal format. (m = 45, c = 0.5)'''

def solve_for_y(x_values):
    m=45
    c=0.5
    for x in x_values:
        y=m*x+c
        print(y)
x_values=[1, 2.3, 5.6, 7, 78]
solve_for_y(x_values)