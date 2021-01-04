"""
Project:practice file handling
Author:Devam A



"""
"""
file = open("file1.txt","r")
lines = file.readlines()
file.close()

print(lines)
"""
"""
import json

file = open("file1.txt","r")
file_contents = json.load(file)
file.close()

print(file_contents["friends"][0])
"""
def file_handling():
    with open("file1.txt", "r") as file:
       return file.read()
