def func(n):
    if n == 0:
        return 0
    else:
        return n + func(n-1)

if __name__ == "__main__":
    print(func(10))