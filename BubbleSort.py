

from visualizer import DataVisualizer

sortables = [16,4,1,41,5,67,7,4,32,3]
example = DataVisualizer(sortables)
example.setup_counter()

print(example.datacount)

# Traverse through all array elements
for i in range(example.datacount):
    # print("in range")
    # Last i elements are already in place
    for j in range(0, example.datacount-i-1):
        # print("in inner range")
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        val_one = example.read_at(j)
        val_two = example.read_at(j+1)
        if val_one > val_two:
            example.update_at(j, val_two)
            example.update_at(j+1, val_one)


# print([ DataVisualizer.ref[i]['data'] for i in DataVisualizer.ref])

example.keep_running()