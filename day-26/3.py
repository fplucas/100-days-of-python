def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path) as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers


numbers_file_1 = read_numbers_from_file("file1.txt")
numbers_file_2 = read_numbers_from_file("file2.txt")

result = [number for number in numbers_file_1 if number in numbers_file_2]

# Write your code above 👆

print(result)
