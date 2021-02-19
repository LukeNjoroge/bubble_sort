def bubble_sort(arr): 
    arr_len = len(arr) 
  
    for m in range(arr_len-1): 
        for n in range(0, arr_len-m-1): 
            if arr[n] > arr[n+1] : 
                arr[j], arr[j+1] = arr[n+1], arr[n] 
  
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubble_sort(arr)
  
print(arr)