def search_binary(data, target, low=None, high=None):

    if low == None: low = 0 
    if high == None: high = len(data) - 1 
    if low > high: 
        return False 
    else: 
        mid = (low + high) // 2  #Or: mid = low + (high-low) // 2
        if target == data[mid]: 
            return True 
        elif target < data[mid]: 
            return search_binary(data, target, low, mid-1) 
        else: 
            return search_binary(data, target, mid+1, high) 
