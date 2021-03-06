import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

with open('names_1.txt', 'r') as file:
    names_1_list = file.read().split("\n")     # List containing 10000 names

with open('names_2.txt', 'r') as file:
    names_2_list = file.read().split("\n")     # List containing 10000 names

duplicates = []    # Return the list of duplicates in this data structure


def handle_duplicate(value, *rest):
    duplicates.append(value)


# Replace the nested for loops below with your improvements

names_1_bst = BinarySearchTree(
    value_iter=names_1_list,
    on_eq=handle_duplicate,
    error_on_eq=False,
)

# print(len(duplicates))     # there _are_ duplicates in the first file

for name_2 in names_2_list:
    names_1_bst.contains(name_2, on_eq=handle_duplicate)

end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

############################################################
#   STRETCH
############################################################
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
