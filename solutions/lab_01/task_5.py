"""
task_5.py - информационная карточка вычислительного эксперимента.

Запрашивает параметры эксперимента, вычисляет общее время,
комплексный коэффициент и квадрат модуля, выводит карточку.
"""

researcher = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs_str = input("Количество запусков: ")
duration_str = input("Длительность одного запуска (с): ")
real_str = input("Действительная часть коэффициента: ")
imag_str = input("Мнимая часть коэффициента: ")

runs = int(runs_str)
duration = float(duration_str)
real = float(real_str)
imag = float(imag_str)

total_seconds = runs * duration
total_minutes = total_seconds / 60
coefficient = complex(real, imag)
modulus_squared = real ** 2 + imag ** 2
has_runs = bool(runs)

print("=" * 40)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {modulus_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)

print("Типы введённых значений:")
print("  researcher:", type(researcher).__name__)
print("  experiment:", type(experiment).__name__)
print("  runs:      ", type(runs).__name__)
print("  duration:  ", type(duration).__name__)
print("  real:      ", type(real).__name__)
print("  imag:      ", type(imag).__name__)