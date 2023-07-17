def generate_series(a):
    if a <= 0:
        return "Input value must be a positive integer."

    series = []
    number = 1

    while len(series) < a:
        series.append(str(number))
        number += 2

    return ", ".join(series)


if __name__ == "__main__":
    a = int(input("Enter the value of 'a': "))
    result = generate_series(a)
    print("Output:", result)
