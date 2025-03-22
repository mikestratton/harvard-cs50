def main():
    o = input("What operator do you want to use? ")
    print(f"{x} {o} {y} is:", calculation(x, y, o))

def float_input(prompt:str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

x = float_input("What's x? ")
y = float_input("What's y? ")


def calculation(n, m, o):
    if o == "+":
        return n + m
    elif o == "-":
        return n - m
    elif o == "*":
        return n * m
    elif o == "/":
        return n / m
    else:
        return "uses an invalid operator. You must enter a valid operator, such as + - * /"


if __name__ == "__main__":
    main()
