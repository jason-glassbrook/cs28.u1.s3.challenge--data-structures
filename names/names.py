import time

start_time = time.time()

with open('names_1.txt', 'r') as file:
    names_1 = file.read().split("\n")  # List containing 10000 names

with open('names_2.txt', 'r') as file:
    names_2 = file.read().split("\n")  # List containing 10000 names

duplicates = []    # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

############################################################
#   STRETCH
############################################################
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
