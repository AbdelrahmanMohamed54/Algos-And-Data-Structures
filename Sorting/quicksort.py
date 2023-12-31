def quick_sort(S):
    if len(S) <= 1: 
        return S 
    left = [] 
    right = [] 
    pivot = S[0] 
    for element in S: 
        if element >= pivot: 
            right.append(element) 
        else: 
            left.append(element) 
    left = quick_sort(left) 
    right = quick_sort(right[1:]) 
    return left + [pivot] + right 
