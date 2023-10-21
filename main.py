from colorama import Fore, Style


def transform_point(point, a, k, p, q):
    x, _ = point
    new_x = x
    new_y = a * k * (x - p) + q
    return new_x, new_y


a = int(input("Enter the value of 'a': "))
k = int(input("Enter the value of 'k': "))
p = int(input("Enter the value of 'p': "))
q = int(input("Enter the value of 'q': "))

file_path = "input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

transformed_points = []

for line in lines:
    try:
        x, y = map(int, line.strip().strip("()").split(","))
        original_point = (x, y)
        transformed_point = transform_point(original_point, a, k, p, q)
        transformed_points.append(transformed_point)
    except ValueError:
        print(f"Skipping invalid point: {line}")

for original, transformed in zip(
    [str(p) for p in transformed_points], transformed_points
):
    arrow = f"{Fore.WHITE + Style.BRIGHT} -> {Style.RESET_ALL}"
    transformed_str = f"{Fore.GREEN}{transformed}"
    print(f"{Fore.RED}{original}{arrow}{transformed_str}{Style.RESET_ALL}")
