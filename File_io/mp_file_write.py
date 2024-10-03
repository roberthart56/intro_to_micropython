# Import the os module to interact with the filesystem
import os

# Open the file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is saved on the RP2040.\n")

# To confirm the file has been written, you can read the file back
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
