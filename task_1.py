import random
import time
import matplotlib.pyplot as plt


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def average_time(sort_func, array, repeats=5):
    times = []
    for _ in range(repeats):
        copy = list(array)
        start = time.perf_counter()
        sort_func(copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    rand_times = []
    det_times = []

    for size in sizes:
        array = [random.randint(-1_000_000, 1_000_000) for _ in range(size)]
        print(f"\nРозмір масиву: {size}")

        rt = average_time(randomized_quick_sort, array)
        dt = average_time(deterministic_quick_sort, array)

        rand_times.append(rt)
        det_times.append(dt)

        print(f"  Рандомізований QuickSort: {rt:.4f} секунд")
        print(f"  Детермінований QuickSort: {dt:.4f} секунд")

    print("\nВисновки:")
    for i, size in enumerate(sizes):
        faster = "рандомізований" if rand_times[i] < det_times[i] else "детермінований"
        diff = abs(rand_times[i] - det_times[i])
        print(
            f"  ▸ При розмірі {size:,} швидшим був {faster} QuickSort на {diff:.4f} секунд.")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, marker='o', label='Рандомізований QuickSort')
    plt.plot(sizes, det_times, marker='s', label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Середній час (секунди)')
    plt.title('Порівняння QuickSort алгоритмів')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
