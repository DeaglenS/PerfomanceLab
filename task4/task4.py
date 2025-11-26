import sys

def load_numbers(filename):
    nums = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    nums.append(int(line))
        if not nums:
            raise ValueError("Файл пуст или не содержит корректных данных.")
        return nums
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def quickselect(arr, k):
    """Находит k-й наименьший элемент в массиве (для поиска медианы)."""
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(pivots):
        return pivots[0]
    else:
        return quickselect(right, k - len(left) - len(pivots))

def find_min_moves(numbers):
    if not numbers:
        return 0

    n = len(numbers)
    median = quickselect(numbers.copy(), n // 2)

    moves = 0
    for num in numbers:
        moves += abs(num - median)

    return moves

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    filename = sys.argv[1]
    MAX_ALLOWED_MOVES = 20

    try:
        nums = load_numbers(filename)
        result = find_min_moves(nums)
        if result <= MAX_ALLOWED_MOVES:
            print(result)
        else:
            print(f"Требуется больше {MAX_ALLOWED_MOVES} ходов.")
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
