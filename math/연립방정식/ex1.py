from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

equation1 = 3 * x + y - 2
equation2 = x - 2 * y - 3

print(solve((equation1, equation2), dict=True))