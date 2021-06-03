
def max_sum(arr, k):
    size = len(arr)
    if size < k :
        print("Invalid Operation")
        return -1
    
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum

    for i in range(size-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum,max_sum)

    return max_sum


arr= [80,-50,90,100]
k = 2
answer = max_sum(arr, k)
print(answer)