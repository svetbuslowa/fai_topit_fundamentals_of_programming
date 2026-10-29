import sys
data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))
alias = data
print("После создания alias:", sys.getrefcount(data))
container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))
del alias
print("После del alias:", sys.getrefcount(data))
container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

# Эксперимент со слабой ссылкой
import weakref
class Record:
    pass

record = Record()
weak_record = weakref.ref(record)
print("До del:", weak_record())
del record
print("После del:", weak_record())

# Практическая задача
import weakref

class Record:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Record({self.name})"

registry = weakref.WeakValueDictionary()

r1 = Record("A")
r2 = Record("B")
r3 = Record("C")

registry["a"] = r1
registry["b"] = r2
registry["c"] = r3

# Сильные ссылки есть только на r1 и r2
print("До удаления:", list(registry.values()))

temp = r3
del r3
# r3 всё ещё жив через temp
del temp
# теперь сильных ссылок на r3 нет

print("После удаления r3:", list(registry.values()))

del r2
print("После удаления r2:", list(registry.values()))
