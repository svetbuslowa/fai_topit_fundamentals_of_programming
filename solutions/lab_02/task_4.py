# Эксперимент с циклом
import gc
first = []
second = []
first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("GC enabled:", gc.isenabled())
print("Thresholds:", gc.get_threshold())
print("Stats:", gc.get_stats())

id_first = id(first)
id_second = id(second)
print("id(first):", id_first)
print("id(second):", id_second)

del first
del second

collected = gc.collect()
print("Собрано объектов:", collected)

# Дополнительный эксперимент
import gc

gc.disable()
print("GC отключён:", not gc.isenabled())

cycles = []
for _ in range(5):
    a = []
    b = []
    a.append(b)
    b.append(a)
    cycles.append(a)

del cycles  # удаляем внешние ссылки

collected_manual = gc.collect()
print("Собрано вручную:", collected_manual)

gc.enable()
print("GC снова включён:", gc.isenabled())

# Практическая задача
import gc

# Три узла в цикле, четвёртый — независимый
n1 = {"name": "n1"}
n2 = {"name": "n2"}
n3 = {"name": "n3"}
n4 = {"name": "n4"}

n1["next"] = n2
n2["next"] = n3
n3["next"] = n1   # цикл замкнут
# n4 не участвует в цикле

print("Связи:")
print(" n1 ->", n1["next"]["name"])
print(" n2 ->", n2["next"]["name"])
print(" n3 ->", n3["next"]["name"])
print(" n4 изолирован:", n4)

before = len(gc.get_objects())

del n1, n2, n3

collected = gc.collect()
print("Собрано объектов:", collected)

print("n4 доступен:", n4)
