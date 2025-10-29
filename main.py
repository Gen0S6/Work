print("System boot successful. Welcome to Gen0S6")

for i in range(5):
    print("Loop number", i)

count = 0
while count < 5:
    print("Count:", count)
    count += 1

def greet(name):
    print(f"Hello, {name}!")

greet("Steve")
greet("Lucie")

name = input("Enter your name: ")
print("Hello", name)

with open("fill.txt","w") as file:
    file.write("first note.") 
with open("fill.txt","r") as file:
    content = file.read()
    print(content)