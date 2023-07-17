def generate_series(a):
    if a <= 0:
        return "Input value must be a positive integer."

    series = [str(i) for i in range(1, 2 * a) if i % 2 != 0]
    return ", ".join(series)


if __name__ == "__main__":
    a = int(input("Enter the value of 'a': "))
    result = generate_series(a)
    print("Output:", result)
