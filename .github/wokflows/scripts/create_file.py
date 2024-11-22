import random

random_value = random.randint(1, 100)
file_name = "random_value.txt"

with open(file_name, "a") as file:
    file.write(f"Случайное значение: {random_value}\n")

print(f"Случайное значение добавлено в файл '{file_name}'.")