from colorama import Fore, Style

def read_coordinates_from_file():
        with open("input.txt", 'r') as file:
            lines = file.readlines()
        return [tuple(map(float, line.strip().strip("()").split(","))) for line in lines]

def stretch_compress(points, factor):
    return [(x * factor, y * factor) for x, y in points]

def translate(points, dx, dy):
    return [(x + dx, y + dy) for x, y in points]

def reflect_x_axis(points):
    return [(-x, y) for x, y in points]

def reflect_y_axis(points):
    return [(x, -y) for x, y in points]

def print_coordinates_with_arrows(original, transformed):
    for o, t in zip(original, transformed):
        print(f"{Fore.RED}{o}{Style.RESET_ALL}{Fore.WHITE + Style.BRIGHT} -> {Style.RESET_ALL}{Fore.GREEN}{t}{Style.RESET_ALL}")

def main():
    original_points = read_coordinates_from_file()

    if not original_points:
        return

    factor = float(input("Enter the stretch/compress factor (default: 1.0): ") or 1.0)
    dx = float(input("Enter the translation in the x-direction (default: 0.0): ") or 0.0)
    dy = float(input("Enter the translation in the y-direction (default: 0.0): ") or 0.0)
    ref = input("Reflect in X or Y or None (default: None): ")
    
    points = original_points
    
        
    if ref.lower() == "x":
        points = reflect_x_axis(points)

    elif ref.lower() == "y":
        points = reflect_y_axis(points)

    points = stretch_compress(points, factor)
    points = translate(points, dx, dy)

    print("\nTransformed Points:")
    print_coordinates_with_arrows(original_points, points)

if __name__ == "__main__":
    main()

