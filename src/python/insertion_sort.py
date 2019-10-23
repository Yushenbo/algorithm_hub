Array = [8, 2, 4, 1, 5, 9, 7, 0]

def insertion_sort(p_array):
    for j in range(1, len(p_array)):
        print("j is: ", j)
        key = p_array[j]
        i = j - 1
        while(i >= 0 and p_array[i] >= key):
            print("i is: " , i, "key is: ", key)
            p_array[i+1], p_array[i] = p_array[i], p_array[i+1]
            i = i - 1
            key = p_array[i+1]
            print("change key is: ", key)
            print("")
        print("")
    return p_array

print("input: ", Array)
print("output: ", insertion_sort(Array))