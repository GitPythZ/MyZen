numbers = list(range(0, 10))
fib_num = []
a, b = 0, 1
for i in numbers:
    if i <= 1:
        fib_num.append(i)
    else:
        while i >= b:
            a, b = b, a+b
            fib_num.append(a + b)
print(fib_num)


