print("Welcome to my Python project")
print("I'm Amir")
print("Part 1")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")
    
print("Part 2")

width = int(input("Enter rectangle width: "))
height = int(input("Enter rectangle height: "))

for i in range(height):
    for j in range(width):
        print("*", end=" ")
    print()

print("Part 3")

while True:
    print("Project Report")
    print("part1: Completed")
    print("part2: Rectangle Drawn")
    print("part3: While is Running")

    stop = input("Press Enter to continue or type stop to exit: ")

    if stop == "stop":
        print("Program finished")
        break