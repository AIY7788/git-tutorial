
import os

path_file = "C:/Users/Trivico/OneDrive/Desktop/test.txt"

if os.path.exists(path_file):
    print(f"That location {path_file} exists")

    if os.path.isdir(path_file):
        print("That is a directory")
    elif os.path.isfile(path_file):
        print("That is a file")

else :
    print("That location doesn't exist")