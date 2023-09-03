print("\nTo-Do List.")

to_do = ["Coding Practice", "Basic Python", "Library", "Functions"]
for index, item in enumerate(to_do):
    print(f"{index}: {item}")

def todo():
    instructions = "\n1: Enter A to add a new TO-DO List. \n2: Enter D to delete a TO-DO List. \n3: Enter U to update a TO-DO List. \n4: Enter X to Exit the program. \n5: Enter L to check your TO-DO List. "
    print(instructions)

    while True:
        todo = input("Please choose any given operation (A, D, U, X, L): ")

        if todo == "A":
            A = input("Add your to-do list: ")
            to_do.append(A)
            for index, item in enumerate(to_do):
                print(f"{index}: {item}")
        elif todo == "D" and todo != "":
            B = int(input("Enter index value which you want to delete: "))
            if B in range(len(to_do)):
                del to_do[B]
            else:
                print("Invalid index.")
            for index, item in enumerate(to_do):
                print(f"{index}: {item}")
        elif todo == "U":
            C = input("Enter a new task you want to replace with an existing item: ")
            D = int(input("Which item you want to replace/update: "))
            if D in range(len(to_do)):
                to_do[D] = C
                for index, item in enumerate(to_do):
                    print(f"{index}: {item}")
            else:
                print("Invalid index.")
        elif todo == "L":
            for index, item in enumerate(to_do):
                print(f"{index}: {item}")
        elif todo == "X":
            break
        else:
            print("Out of range")

# Call the todo function to start the program.
todo()
