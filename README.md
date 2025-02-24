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

Random: Arrays of random values.
Sorted: Arrays that are already sorted.
Reverse: Arrays sorted in descending order.
Duplicate: Arrays where all elements are the same.

## Usage
To run the benchmark, simply execute the sort.py script. The script will:

Define several test arrays.
Run the drab_sort function and measure the time it takes to sort each array.
Print the sorted arrays and the time taken for each test.
bash
Copy
Edit
python sort.py