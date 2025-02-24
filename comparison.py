import time
import random
import heapq

# DrabSort
def drab_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # For integer data with reasonable range, counting sort is O(n)
    try:
        # Check if all integers with manageable range
        all_ints = all(isinstance(x, int) for x in arr)
        min_val = min(arr)
        max_val = max(arr)
        range_size = max_val - min_val + 1
        
        # Use counting sort for integer data with reasonable range
        if all_ints and range_size <= 10 * len(arr):
            count = [0] * range_size
            for num in arr:
                count[num - min_val] += 1
                
            result = []
            for i in range(range_size):
                result.extend([i + min_val] * count[i])
            return result
    except:
        pass
    
    # For floating point or larger range integer data, use improved bucket sort
    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)
    
    # Early return for uniform arrays
    if min_val == max_val:
        return arr
        
    # Critical performance factor: bucket count and distribution strategy
    num_buckets = max(2, min(n, 1000))  # Cap to avoid excessive memory use
    
    # Pre-allocate buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Optimize bucket placement
    range_val = max_val - min_val
    if range_val == 0:
        return arr
        
    # Use integer math where possible for speed
    for val in arr:
        # Careful handling of max value edge case
        if val == max_val:
            buckets[-1].append(val)
        else:
            bucket_idx = min(int((val - min_val) * num_buckets / range_val), num_buckets - 1)
            buckets[bucket_idx].append(val)
    
    # Use in-place sort for each bucket and build result
    result = []
    for bucket in buckets:
        if bucket:  # Skip empty buckets
            bucket.sort()  # In-place sort is faster than creating new lists
            result.extend(bucket)
            
    return result



# QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# MergeSort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# HeapSort
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Benchmarking function
def benchmark(algorithms, test_cases):
    results = {}
    
    for name, func in algorithms.items():
        times = []
        for arr in test_cases:
            arr_copy = arr[:]  # Avoid modifying original array
            start_time = time.time()
            sorted_arr = func(arr_copy)
            end_time = time.time()
            assert sorted_arr == sorted(arr), f"{name} failed!"
            times.append(end_time - start_time)
        results[name] = sum(times) / len(times)  # Average time

    return results

# Test Cases
test_sizes = [1000, 5000, 10000]  # Different input sizes
test_cases = {
    "Random": [random.sample(range(1, 100000), size) for size in test_sizes],
    "Sorted": [list(range(size)) for size in test_sizes],
    "Reverse": [list(range(size, 0, -1)) for size in test_sizes],
    "Duplicate": [[5] * size for size in test_sizes],  # Same element repeated
}

# Sorting algorithms to compare
sorting_algorithms = {
    "DrabSort": drab_sort,
    "QuickSort": quick_sort,
    "MergeSort": merge_sort,
    "HeapSort": heap_sort,
    "Timsort (Python Sort)": sorted
}
