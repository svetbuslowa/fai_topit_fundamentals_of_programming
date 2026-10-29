import copy
original = [
    ["Python", 5],
    ["Algorithms", 4],
]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

print("--- до изменений ---")
print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)

original.append(["Databases", 5])
print("\n--- после original.append(['Databases', 5]) ---")
print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)

original[0][1] = 3
print("\n--- после original[0][1] = 3 ---")
print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)

# Ошибочная матрица
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print("wrong:", wrong_matrix)

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print("correct:", correct_matrix)
