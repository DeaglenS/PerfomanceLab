import sys
import threading
from concurrent.futures import ThreadPoolExecutor

def find_circular_path(n, m):

    if n <= 0 or m <= 0:
        return []

    path = []
    current = 1
    visited = set() 

    while True:
        if current in visited:
            break
        visited.add(current)
        path.append(current)

        # Вычисляем следующую позицию
        next_pos = (current + m - 1) % n
        if next_pos == 0:
            next_pos = n


        if next_pos == 1 and len(path) > 1:
            break

        current = next_pos

    return path

def main():
    if len(sys.argv) != 5:
        print("Ошибка: неверное количество аргументов.")
        sys.exit(1)

    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])
        if any(x <= 0 for x in (n1, m1, n2, m2)):
            raise ValueError("Все аргументы должны быть положительными числами.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    
    with ThreadPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(find_circular_path, n1, m1)
        future2 = executor.submit(find_circular_path, n2, m2)
        path1, path2 = future1.result(), future2.result()

   
    result = ''.join(map(str, path1)) + ''.join(map(str, path2))
    print(result)

if __name__ == "__main__":
    main()
