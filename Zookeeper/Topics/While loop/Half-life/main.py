initial_atoms = int(input())
final_atoms = int(input())
number = 0
while initial_atoms > final_atoms:
    initial_atoms = 0.5 * initial_atoms
    number = number + 1
print(number * 12)
