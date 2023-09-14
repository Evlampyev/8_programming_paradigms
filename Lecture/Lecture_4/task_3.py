# Ленивые вычисления в Python

def lazy_function():
    i = 0
    while True:
        yield i
        i += 1


f = lazy_function()

print(next(f))  # 0
print(next(f))  # 1
print(next(f))  # 2
