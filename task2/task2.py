#!/usr/bin/env python3
import sys

def parse_ellipse_params(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        if len(lines) < 2:
            raise ValueError("Файл должен содержать хотя бы 2 строки с данными.")

        # Центр эллипса
        try:
            x_c, y_c = map(float, lines[0].split())
        except:
            raise ValueError("Ошибка в первой строке")

        # Радиусы
        try:
            rx, ry = map(float, lines[1].split())
        except:
            raise ValueError("Ошибка во второй строке")

        if rx <= 0 or ry <= 0:
            raise ValueError("Радиусы должны быть положительными.")

        return x_c, y_c, rx, ry

    except FileNotFoundError:
        print(f"Ошибка: файл не найден.")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

def parse_points(filename):
    points = []
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    x, y = map(float, line.split())
                    points.append((x, y))
                except:
                    raise ValueError(f"Ошибка в строке {i}: ожидалось 2 числа (x y).")

        if not (1 <= len(points) <= 100):
            raise ValueError("Количество точек должно быть от 1 до 100.")

        return points

    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка при чтении файла точек: {e}")
        sys.exit(1)

def check_point_in_ellipse(x, y, x_c, y_c, rx, ry, eps=1e-10):
    dx = x - x_c
    dy = y - y_c
    val = (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry)

    if abs(val - 1.0) < eps:
        return 0
    return 1 if val < 1.0 else 2

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    ellipse_file, points_file = sys.argv[1], sys.argv[2]

    # Считываем параметры эллипса
    x_c, y_c, rx, ry = parse_ellipse_params(ellipse_file)

    # Считываем точки
    points = parse_points(points_file)

    # Проверяем каждую точку
    for x, y in points:
        res = check_point_in_ellipse(x, y, x_c, y_c, rx, ry)
        print(res)

if __name__ == "__main__":
    main()
