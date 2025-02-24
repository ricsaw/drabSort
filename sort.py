import time

def drab_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr  # Already sorted
    
    min_val, max_val = min(arr), max(arr)
    range_width = max_val - min_val

    if range_width == 0:  # All elements are the same
        return arr

    # Adaptive Bucket Creation
    k = 0.5  # Tuning parameter (can be adjusted)
    num_buckets = max(1, int(k * n))  # Ensure at least 1 bucket
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for val in arr:
        bucket_index = int(((val - min_val) / range_width) * (num_buckets - 1))
        buckets[bucket_index].append(val)

    # Refinement: Sort only oversized buckets
    avg_bucket_size = n / num_buckets
    for bucket in buckets:
        if len(bucket) > 2 * avg_bucket_size:  # Only sort large buckets
            bucket.sort()  # Using Python's Timsort

    # Collect sorted elements
    return [val for bucket in buckets for val in bucket]  # Flatten the sorted buckets

# Benchmark function
def benchmark(sort_func, test_cases):
    for i, arr in enumerate(test_cases, 1):
        start_time = time.time()
        sorted_arr = sort_func(arr)
        end_time = time.time()
        print('Sorted array:', sorted_arr)
        print(f"Test {i}: Sorted in {end_time - start_time:.6f} seconds")

# Example test cases
test_arrays = [
    [5, 2, 8, 1, 9, 4],
    [1, 2, 3, 4, 5],  # Already sorted
    [5, 4, 3, 2, 1],  # Reverse sorted
    [1, 1, 1, 1, 1],  # All same elements
    [1, 5, 2, 8, 9, 4] * 100  # Large dataset
]

# Run benchmark
benchmark(drab_sort, test_arrays)
