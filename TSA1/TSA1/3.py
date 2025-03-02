def pattern_a(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))

pattern_a(5)

def pattern_b(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(str(i) * i)
        i += 1

pattern_b(7)