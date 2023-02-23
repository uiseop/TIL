n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# Binary search for the minimum possible Blu-ray size
left, right = max(lectures), sum(lectures)
while left <= right:
    mid = (left + right) // 2
    
    # Try to allocate lectures to Blu-rays
    cnt = 1
    total = 0
    for lec in lectures:
        total += lec
        if total > mid:
            cnt += 1
            total = lec

    # Update the binary search range based on the result
    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        
print(left)
