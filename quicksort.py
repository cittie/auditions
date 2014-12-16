def quickSort(array):
    left, equal, right = ([] for i in range(3))

    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                equal.append(i)
        
        return quickSort(left) + equal + quickSort(right)
    else:
        return array
