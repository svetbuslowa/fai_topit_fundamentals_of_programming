# Часть 1
import sys
print("пустой список:      ", sys.getsizeof([]))
print("список из 10 int:   ", sys.getsizeof([1,2,3,4,5,6,7,8,9,10]))
print("кортеж из 10 int:   ", sys.getsizeof((1,2,3,4,5,6,7,8,9,10)))
print("строка из 10 симв.: ", sys.getsizeof("0123456789"))
print("целое число:        ", sys.getsizeof(42))
print("None:               ", sys.getsizeof(None))

# Часть 2
lst = []
last_size = sys.getsizeof(lst)
print(f"len=0, size={last_size}")
for i in range(100):
    lst.append(i)
    cur_size = sys.getsizeof(lst)
    if cur_size != last_size:
        print(f"len={len(lst)}, size={cur_size}")
        last_size = cur_size

# Часть 3
import tracemalloc

# Вариант 1: список
tracemalloc.start()
numbers = list(range(100_000))
cur1, peak1 = tracemalloc.get_traced_memory()
tracemalloc.stop()
del numbers

# Вариант 2: range
tracemalloc.start()
numbers = range(100_000)
cur2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()
del numbers

print(f"list:  current = {cur1/1024:.2f} KB, peak = {peak1/1024:.2f} KB")
print(f"range: current = {cur2/1024:.2f} KB, peak = {peak2/1024:.2f} KB")
print(f"Отношение пиков: {peak1/peak2:.1f}x")

# Практическая задача
def measure_list_of_n(n):
    tracemalloc.start()
    data = list(range(n))
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "scenario": f"list(range({n}))",
        "count": n,
        "outer_size": sys.getsizeof(data),
        "current_kb": cur / 1024,
        "peak_kb": peak / 1024,
    }

def measure_range_of_n(n):
    tracemalloc.start()
    data = range(n)
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "scenario": f"range({n})",
        "count": n,
        "outer_size": sys.getsizeof(data),
        "current_kb": cur / 1024,
        "peak_kb": peak / 1024,
    }

def main():
    sizes = [1_000, 10_000, 100_000]
    rows = []
    for n in sizes:
        rows.append(measure_list_of_n(n))
        rows.append(measure_range_of_n(n))

    print(f"{'Сценарий':<25} {'N':>8} {'outer':>8} {'curr KB':>10} {'peak KB':>10} {'ratio':>8}")
    print("-" * 75)
    for i in range(0, len(rows), 2):
        a, b = rows[i], rows[i+1]
        ratio = a["peak_kb"] / b["peak_kb"] if b["peak_kb"] > 0 else float("inf")
        for r in (a, b):
            print(f"{r['scenario']:<25} {r['count']:>8} {r['outer_size']:>8} "
                  f"{r['current_kb']:>10.2f} {r['peak_kb']:>10.2f} {'':>8}")
        print(f"{'':>53} ratio list/range: {ratio:.1f}x")
        print()

if __name__ == "__main__":
    main()
