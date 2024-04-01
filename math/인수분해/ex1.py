from sympy import expand, factor, Symbol

x = Symbol('x')

# expand() 수식을 (x + 1) * (x + 5) 로 전개한다.
print(expand((x + 1) * (x + 5)))

# factor() 인수 분해하는 함수로, x2 + 6x + 5를 인수 분해한다.
print(factor(x ** 2 + 6 * x + 5))