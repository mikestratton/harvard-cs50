def main():
    n = int(input("What's x? "))
    m = int(input("What's y? "))
    print(f"{n} to the power of {m} is", raise_to_power_of(n, m))


def square(x):
    return x * x


def raise_to_power_of(n, m):
    return pow(n, m)


if __name__ == "__main__":
    main()
