import os

source = input("Which file do you wish to rename? (Remember to include the source path) ")
destination = input("What should it be renamed to? (Don't forget the path!) ")

os.rename(source,destination)
print(f"{source} renamed to {destination} successfully.")