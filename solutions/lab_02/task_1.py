# Эксперимент A
a = 10
b = a
print(a, b)
print(id(a), id(b))
a += 1
print(a, b)
print(id(a), id(b))

# Эксперимент B
first = [10, 20]
second = first
print(first, second)
print(id(first), id(second))
second.append(30)
print(first, second)
print(id(first), id(second))

# Переназначение
second = [10, 20, 30]
print("После переназначения:")
print(first, second)
print("== :", first == second)
print("is :", first is second)
second.append(40)
print("После изменения нового second:")
print(first, second)

# Практическая задача
# Нежелательное совместное изменение
config_bad = {
    "name": "ML Project",
    "participants": ["Alice", "Bob"],
    "launch_params": [["--lr", "0.01"], ["--epochs", "10"]]
}
config_bad_clone = config_bad

config_bad_clone["participants"].append("Charlie")
config_bad_clone["launch_params"][0].append("--batch=32")

print("Плохой клон:", config_bad_clone)
print("Оригинал:   ", config_bad)
# Видно, что оригинал тоже изменился

# Независимая конфигурация
import copy
config_good = copy.deepcopy(config_bad)
config_good["participants"].append("Dave")
config_good["launch_params"][0].append("--gpu=1")

assert config_good["participants"] != config_bad["participants"]
assert config_good["launch_params"] != config_bad["launch_params"]
assert config_good is not config_bad

print("Независимая:", config_good)
print("Оригинал:   ", config_bad)
