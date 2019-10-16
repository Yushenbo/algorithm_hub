Array = [6, 5, 3, 1, 8, 7, 2, 4]

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0 :
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    print("result is:", result)
    return result


def merge_sort(arry):
    if len(arry) == 1:
        return arry
    center = len(arry) // 2
    left = arry[:center]
    right = arry[center:]
    
    l1 = merge_sort(left)
    r1 = merge_sort(right)

    return merge(l1, r1)

print(merge_sort(Array))
