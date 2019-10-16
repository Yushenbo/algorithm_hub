Array = [4, 5, 3, 1, 8, 7, 2, 6]

def quick_sort(array):
    if len(array) < 2:
        return array
    
    pvoit = array[0]
    less_than_pvoit = [x for x in array if x <= pvoit]
    grater_than_pvoit = [x for x in array if x > pvoit]
    print("pvoit: ", pvoit)
    print("left :", less_than_pvoit)
    print("right :", grater_than_pvoit)
    return quick_sort(less_than_pvoit) + [pvoit] + quick_sort(grater_than_pvoit)

print(quick_sort(Array))