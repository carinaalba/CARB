"""
Let's read several lines from a text file.
"""
file = open("database.txt", "r")
lines = file.readlines()
file.close()
database = [
]
for line in lines:
    database += [line.split()]
