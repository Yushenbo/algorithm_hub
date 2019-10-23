import random

Array = [6, 5, 3, 1, 8, 7, 2, 4, 6, 10]

def quick_sort(array):
    if len(array) < 2:
        return array

    pvoit = array[0]
    #pvoit = array.pop(0)
    print("pvoit: ", pvoit)
    less_than_pvoit = [x for x in array[1:] if x <= pvoit]
    #less_than_pvoit = filter(lambda ele: ele <= pvoit, array[1:])
    grater_than_pvoit = [x for x in array[1:] if x > pvoit]
    #grater_than_pvoit = filter(lambda  ele: ele > pvoit, array[1:])
    print("left :", less_than_pvoit)
    print("right :", grater_than_pvoit)
    return quick_sort(less_than_pvoit) + [pvoit] + quick_sort(grater_than_pvoit)

print("result is:", quick_sort(Array))