# Sorting Algorithms Benchmark

This repository contains implementations of various sorting algorithms, including a custom sorting algorithm called `DrabSort`. The primary goal is to compare the performance of these algorithms across different test cases and array sizes.

## Sorting Algorithms

1. **DrabSort**: A custom sorting algorithm that uses adaptive bucket sorting and sorts oversized buckets using Python’s built-in Timsort.
2. **QuickSort**: A popular divide-and-conquer algorithm.
3. **MergeSort**: A stable, divide-and-conquer sorting algorithm.
4. **HeapSort**: A comparison-based sorting algorithm using a binary heap.
5. **Timsort (Python's built-in sort)**: Python's optimized built-in sorting function, based on merge sort and insertion sort.

## Requirements

To run the benchmark tests, you'll need the following Python packages:

- `numpy`
- `matplotlib`
- `tabulate`

Install them using pip:

```bash
pip install -r requirements.txt

```


## Benchmarking

The benchmark function runs each sorting algorithm on multiple test cases of varying array sizes, measuring the time taken to sort each array. The test cases include:

* **Random** : Arrays of random values.
* **Sorted** : Arrays that are already sorted.
* **Reverse** : Arrays sorted in descending order.
* **Duplicate** : Arrays where all elements are the same.

## Usage

To run the benchmark, simply execute the `benchmark.py` script. The script will:

1. Define several test arrays.
2. Run the `drab_sort` function and measure the time it takes to sort each array.
3. Print the sorted arrays and the time taken for each test.

<pre class="!overflow-visible" data-start="1763" data-end="1794"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-[5px] h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none px-4 py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></span><span class="" data-state="closed"><button class="flex select-none items-center gap-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path d="M2.5 5.5C4.3 5.2 5.2 4 5.5 2.5C5.8 4 6.7 5.2 8.5 5.5C6.7 5.8 5.8 7 5.5 8.5C5.2 7 4.3 5.8 2.5 5.5Z" fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.66282 16.5231L5.18413 19.3952C5.12203 19.7678 5.09098 19.9541 5.14876 20.0888C5.19933 20.2067 5.29328 20.3007 5.41118 20.3512C5.54589 20.409 5.73218 20.378 6.10476 20.3159L8.97693 19.8372C9.72813 19.712 10.1037 19.6494 10.4542 19.521C10.7652 19.407 11.0608 19.2549 11.3343 19.068C11.6425 18.8575 11.9118 18.5882 12.4503 18.0497L20 10.5C21.3807 9.11929 21.3807 6.88071 20 5.5C18.6193 4.11929 16.3807 4.11929 15 5.5L7.45026 13.0497C6.91175 13.5882 6.6425 13.8575 6.43197 14.1657C6.24513 14.4392 6.09299 14.7348 5.97903 15.0458C5.85062 15.3963 5.78802 15.7719 5.66282 16.5231Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 7L18.5 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>Edit</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre language-bash"><span>python benchmark.py
</span></code></div></div></pre>

## Design Choices Behind `DrabSort`

### 1. **Bucket-Based Sorting with Adaptive Tuning**

Instead of sorting the entire array directly, `DrabSort` divides the data into a series of buckets based on a calculated range. This helps avoid unnecessary comparisons across the entire dataset. However, rather than sorting all buckets, it only sorts oversized buckets using Python's built-in Timsort, which helps optimize performance in datasets with a natural distribution.

### 2. **Handling of Uniform Data**

If all elements in the array are the same, `DrabSort` detects this early and immediately returns the original array without processing, making it efficient for such cases.

### 3. **Selective Sorting**

Instead of sorting every bucket, `DrabSort` only sorts buckets that exceed twice the average bucket size. This allows it to avoid sorting small, already ordered subsets, improving efficiency.

### 4. **Fixed Bucket Count Tuning**

The algorithm uses a tunable constant (`k = 0.5`) to determine the number of buckets based on the input size. This parameter can be adjusted to balance bucket size and sorting efficiency.

## Limitations Compared to Timsort

### 1. **Bucket Allocation Overhead**

Unlike Timsort, which works directly on the array using an optimized merge-insertion approach, `DrabSort` incurs additional overhead by allocating multiple lists (buckets) before sorting begins. This makes it inefficient for small datasets.

### 2. **Worst-Case Performance**

For adversarial inputs (e.g., arrays where all values cluster into a single bucket), `DrabSort` effectively degrades to `O(n log n)`, losing any advantage over Timsort.

### 3. **Suboptimal for Nearly Sorted Data**

Timsort is explicitly designed to take advantage of already sorted or nearly sorted data, running in `O(n)` time in the best case. `DrabSort` does not have the same optimizations for such cases and may still incur bucket allocation and merging overhead.

### 4. **Memory Usage**

Since `DrabSort` relies on multiple buckets, it requires additional memory allocations. Timsort, being an in-place sorting algorithm, has a clear advantage in terms of space efficiency.

## When to Use `DrabSort`

`DrabSort` can be beneficial when:

* Sorting datasets with a known range and relatively uniform distribution.
* Sorting large datasets where bucket sorting reduces unnecessary comparisons.
* Handling cases where duplicate values are common, as it avoids unnecessary sorting in such cases.

However, for general-purpose sorting, Python’s built-in Timsort remains the superior choice due to its optimizations for real-world datasets.

---

## Example Output

<pre class="!overflow-visible" data-start="4435" data-end="4648"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-[5px] h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">plaintext</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none px-4 py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></span><span class="" data-state="closed"><button class="flex select-none items-center gap-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path d="M2.5 5.5C4.3 5.2 5.2 4 5.5 2.5C5.8 4 6.7 5.2 8.5 5.5C6.7 5.8 5.8 7 5.5 8.5C5.2 7 4.3 5.8 2.5 5.5Z" fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.66282 16.5231L5.18413 19.3952C5.12203 19.7678 5.09098 19.9541 5.14876 20.0888C5.19933 20.2067 5.29328 20.3007 5.41118 20.3512C5.54589 20.409 5.73218 20.378 6.10476 20.3159L8.97693 19.8372C9.72813 19.712 10.1037 19.6494 10.4542 19.521C10.7652 19.407 11.0608 19.2549 11.3343 19.068C11.6425 18.8575 11.9118 18.5882 12.4503 18.0497L20 10.5C21.3807 9.11929 21.3807 6.88071 20 5.5C18.6193 4.11929 16.3807 4.11929 15 5.5L7.45026 13.0497C6.91175 13.5882 6.6425 13.8575 6.43197 14.1657C6.24513 14.4392 6.09299 14.7348 5.97903 15.0458C5.85062 15.3963 5.78802 15.7719 5.66282 16.5231Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 7L18.5 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>Edit</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre language-plaintext"><span>Sorted array: [1, 2, 3, 4, 5]
Test 1: Sorted in 0.000031 seconds

Sorted array: [1, 2, 3, 4, 5]
Test 2: Sorted in 0.000024 seconds

Sorted array: [1, 2, 3, 4, 5]
Test 3: Sorted in 0.000017 seconds
</span></code></div></div></pre>

## Future Improvements

* Implement dynamic bucket tuning instead of using a fixed `k` value.
* Add optimizations for nearly sorted data to reduce overhead.
* Experiment with different bucket distribution strategies to improve worst-case behavior.
