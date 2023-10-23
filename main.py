from typing_extensions import Tuple, Type
import matplotlib.pyplot as plt
from colorama import Fore, Style
import os


def save_transformed_points_plot(original_points, transformed_points):
    original_x, original_y = zip(*original_points)
    transformed_x, transformed_y = zip(*transformed_points)

    plt.figure(figsize=(8, 4))
    plt.scatter(original_x, original_y, c='red', label='Original Points')
    plt.scatter(transformed_x, transformed_y, c='green', label='Transformed Points')
    # plt.plot(original_x, original_y, 'r--', label='Original')
    # plt.plot(transformed_x, transformed_y, 'g--', label='Transformed')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Original and Transformed Points with Connecting Lines')
    plt.legend()
    plt.grid(True)

    output_image_path = os.path.join("transformed_points.png")
    plt.savefig(output_image_path)


def transform_point(point: tuple[int, int], a, k, p, q):
    x = point[0]
    y = point[1]
    new_x = x
    new_y = a * (k * (x - p)) + q
    return new_x, new_y


a = int(input("Enter the value of 'a': "))
k = int(input("Enter the value of 'k': "))
p = int(input("Enter the value of 'p': "))
q = int(input("Enter the value of 'q': "))

with open("input.txt", "r") as f:
    lines = f.readlines()

transformed_points = []
original_points = []

for line in lines:
    try:
        x, y = map(int, line.strip().strip("()").split(","))
        original_point = (x, y)
        transformed_point = transform_point(original_point, a, k, p, q)
        original_points.append(original_point)
        transformed_points.append(transformed_point)
    except ValueError:
        print(f"Skipping invalid point: {line}")

for original, transformed in zip(
    [str(p) for p in original_points], transformed_points
):
    arrow = f"{Fore.WHITE + Style.BRIGHT} -> {Style.RESET_ALL}"
    transformed_str = f"{Fore.GREEN}{transformed}"
    print(f"{Fore.RED}{original}{arrow}{transformed_str}{Style.RESET_ALL}")

save_transformed_points_plot(original_points, transformed_points)
