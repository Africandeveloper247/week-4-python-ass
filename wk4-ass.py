#This is week 4 assignment on python

#QUESION 1
#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

#writing file 

with open("text.txt", "w") as file:
    file.write("This is my week 4 assignment on Python Programming. All tanks to PLP Africa")
    

#Read file
with open("text.txt", "r") as file:
    data = file.read()
    print(data)

# write a modified version
with open("text.txt", "a") as file:
    data = file.write("\n I was in my car learning")



#QUESTION 2
#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    with open("text.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("Found not found")
finally:
    print("file closed successfully")
    file.close()
